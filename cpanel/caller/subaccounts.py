from cpanel_api import Api
from ..core import CPanelEndpoint, CPanelError
from ..util import cmd_is, domain, username


EDIT_SETTINGS = frozenset((
	'alternate_email',
	'password',
	'real_name',
	'services.email.enabled',
	'services.email.quota',
	'services.ftp.enabled',
	'services.ftp.homedir',
	'services.webdisk.enabled',
	'services.webdisk.enabledigest',
	'services.webdisk.homedir',
	'services.webdisk.perms',
	'services.webdisk.private',
))
BINARY_EDIT_SETTINGS = frozenset((
	'services.email.enabled',
	'services.ftp.enabled',
	'services.webdisk.enabled',
	'services.webdisk.enabledigest',
	'services.webdisk.private',
))
PATH_EDIT_SETTINGS = frozenset((
	'services.ftp.homedir',
	'services.webdisk.homedir',
))


def edit_settings(arguments: list[str]) -> dict[str, str | int]:
	"""Validate and normalize UserManager::edit_user settings."""
	settings: dict[str, str | int] = {}
	for argument in arguments:
		name, separator, value = argument.partition('=')
		if not separator:
			raise CPanelError("expected SETTING=VALUE for edit subaccount")
		if name not in EDIT_SETTINGS:
			raise CPanelError("unsupported subaccount setting")
		if name in settings:
			raise CPanelError("duplicate subaccount setting, {}".format(name))

		if name in BINARY_EDIT_SETTINGS:
			if value not in ('0', '1'):
				raise CPanelError("{} must be 0 or 1".format(name))
			settings[name] = int(value)
		elif name == 'services.email.quota':
			if value != 'unlimited' and not (value.isascii() and value.isdecimal()):
				raise CPanelError("services.email.quota must be a number or unlimited")
			settings[name] = value if value == 'unlimited' else int(value)
		elif name == 'services.webdisk.perms':
			if value not in ('ro', 'rw'):
				raise CPanelError("services.webdisk.perms must be ro or rw")
			settings[name] = value
		elif name == 'password' and not value:
			raise CPanelError("password must not be empty")
		elif name in PATH_EDIT_SETTINGS and not value:
			raise CPanelError("{} must not be empty".format(name))
		else:
			settings[name] = value

	if settings.get('services.ftp.enabled') == 1 and 'services.ftp.homedir' not in settings:
		raise CPanelError("services.ftp.homedir is required when enabling FTP")
	if settings.get('services.webdisk.enabled') == 1 and 'services.webdisk.homedir' not in settings:
		raise CPanelError("services.webdisk.homedir is required when enabling Web Disk")
	return settings


def call(host: CPanelEndpoint, cmd: str, args: list[str]) -> str:
	r: str = ""
	uapi: Api = host.client.uapi

	if cmd_is(cmd, "list subaccount"):
		r = host.dump(lambda: uapi.UserManager.list_users())

	elif cmd_is(cmd, "get subaccount"):
		r = host.dump(lambda: uapi.UserManager.lookup_user(guid = args[2]))

	elif cmd_is(cmd, "get service subaccount"):
		r = host.dump(lambda: uapi.UserManager.lookup_service_account(full_username = args[3], type = args[4]))
		
	elif cmd_is(cmd, "check subaccount conflicts"):
		r = host.dump(lambda: uapi.UserManager.check_account_conflicts(full_username=args[3]))

	elif cmd_is(cmd, "create subaccount"):
		r = host.check(lambda: uapi.UserManager.create_user(
			username = username(args[2]), domain = domain(args[2]), password = args[3]))

	elif cmd_is(cmd, "edit subaccount"):
		settings = edit_settings(args[3:])
		settings['username'] = username(args[2])
		settings['domain'] = domain(args[2])
		r = host.check(lambda: uapi.UserManager.edit_user(**settings))

	elif cmd_is(cmd, "delete subaccount", "rm subaccount", "remove subaccount"):
		r = host.check(lambda: uapi.UserManager.delete_user(
			username = username(args[2]), domain = domain(args[2])))

	return r
