import re
import unittest
from collections.abc import Callable
from unittest.mock import Mock

from cpanel.core import CPanelError
from cpanel.dispatcher import CommandSpec, dispatch


class TestDispatch(unittest.TestCase):

	def setUp(self) -> None:
		self.host = Mock()


	def test_declared_plural_alias_is_dispatched(self) -> None:
		self.host.dump.return_value = 'features'
		result = dispatch(self.host, ['list', 'features'])
		self.assertEqual(result, 'features')
		self.host.dump.assert_called_once()


	def test_prefix_lookalike_is_rejected(self) -> None:
		with self.assertRaisesRegex(CPanelError, '^unrecognized command, list featuresXYZ$'):
			dispatch(self.host, ['list', 'featuresXYZ'])


	def test_missing_argument_is_validated_before_handler(self) -> None:
		with self.assertRaisesRegex(CPanelError, '^missing arguments for set locale'):
			dispatch(self.host, ['set', 'locale'])
		self.host.check.assert_not_called()


	def test_extra_argument_is_rejected(self) -> None:
		with self.assertRaisesRegex(CPanelError, '^too many arguments for get quota$'):
			dispatch(self.host, ['get', 'quota', 'extra'])


	def test_command_spec_exposes_aliases_arity_and_handler(self) -> None:
		handler = Mock(return_value = 'OK')
		specification = CommandSpec(('do thing', 'perform thing'), 1, 2, handler)
		self.assertEqual(specification.match(['perform', 'thing', 'value']), ('perform thing', 2))
		self.assertEqual(specification.min_arguments, 1)
		self.assertEqual(specification.max_arguments, 2)


class TestSubaccountDispatch(unittest.TestCase):

	def setUp(self) -> None:
		self.host = Mock()
		self.host.check.side_effect = self.run_check


	@staticmethod
	def run_check(apicall: Callable[[], object]) -> str:
		apicall()
		return 'OK'


	def test_create_subaccount_forwards_required_parameters(self) -> None:
		result = dispatch(
			self.host,
			['create', 'subaccount', 'new.user@example.test', 'secret-password'],
		)

		self.assertEqual(result, 'OK')
		self.host.client.uapi.UserManager.create_user.assert_called_once_with(
			username = 'new.user',
			domain = 'example.test',
			password = 'secret-password',
		)


	def test_delete_subaccount_aliases_forward_identity(self) -> None:
		for verb in ('delete', 'rm', 'remove'):
			with self.subTest(verb = verb):
				self.host.client.uapi.UserManager.delete_user.reset_mock()
				result = dispatch(self.host, [verb, 'subaccount', 'old.user@example.test'])
				self.assertEqual(result, 'OK')
				self.host.client.uapi.UserManager.delete_user.assert_called_once_with(
					username = 'old.user',
					domain = 'example.test',
				)


	def test_create_subaccount_requires_password_before_api_call(self) -> None:
		with self.assertRaisesRegex(CPanelError, '^missing arguments for create subaccount'):
			dispatch(self.host, ['create', 'subaccount', 'new.user@example.test'])
		self.host.check.assert_not_called()


	def test_edit_subaccount_forwards_only_requested_settings(self) -> None:
		result = dispatch(self.host, [
			'edit', 'subaccount', 'existing.user@example.test',
			'real_name=Existing User',
			'password=new-secret',
			'services.email.enabled=1',
			'services.email.quota=unlimited',
			'services.webdisk.enabled=1',
			'services.webdisk.homedir=/webdisk',
			'services.webdisk.perms=ro',
		])

		self.assertEqual(result, 'OK')
		self.host.client.uapi.UserManager.edit_user.assert_called_once_with(
			real_name = 'Existing User',
			password = 'new-secret',
			**{
				'services.email.enabled': 1,
				'services.email.quota': 'unlimited',
				'services.webdisk.enabled': 1,
				'services.webdisk.homedir': '/webdisk',
				'services.webdisk.perms': 'ro',
				'username': 'existing.user',
				'domain': 'example.test',
			},
		)


	def test_edit_subaccount_requires_a_setting_before_api_call(self) -> None:
		with self.assertRaisesRegex(CPanelError, '^missing arguments for edit subaccount'):
			dispatch(self.host, ['edit', 'subaccount', 'existing.user@example.test'])
		self.host.check.assert_not_called()


	def test_edit_subaccount_rejects_malformed_and_unsupported_settings(self) -> None:
		invalid_arguments = (
			(['real_name'], 'expected SETTING=VALUE for edit subaccount'),
			(['not_a_setting=value'], 'unsupported subaccount setting'),
			(['real_name=First', 'real_name=Second'], 'duplicate subaccount setting, real_name'),
		)
		for setting_arguments, message in invalid_arguments:
			with self.subTest(setting_arguments = setting_arguments):
				self.host.check.reset_mock()
				with self.assertRaisesRegex(CPanelError, '^{}$'.format(re.escape(message))):
					dispatch(self.host, [
						'edit', 'subaccount', 'existing.user@example.test', *setting_arguments,
					])
				self.host.check.assert_not_called()


	def test_edit_subaccount_validates_structured_setting_values(self) -> None:
		invalid_settings = (
			('services.email.enabled=yes', 'services.email.enabled must be 0 or 1'),
			('services.email.quota=-1', 'services.email.quota must be a number or unlimited'),
			('services.webdisk.perms=write', 'services.webdisk.perms must be ro or rw'),
			('password=', 'password must not be empty'),
			('services.ftp.homedir=', 'services.ftp.homedir must not be empty'),
			('services.ftp.enabled=1', 'services.ftp.homedir is required when enabling FTP'),
			('services.webdisk.enabled=1', 'services.webdisk.homedir is required when enabling Web Disk'),
		)
		for setting, message in invalid_settings:
			with self.subTest(setting = setting):
				self.host.check.reset_mock()
				with self.assertRaisesRegex(CPanelError, '^{}$'.format(re.escape(message))):
					dispatch(self.host, [
						'edit', 'subaccount', 'existing.user@example.test', setting,
					])
				self.host.check.assert_not_called()


	def test_subaccount_identity_requires_domain(self) -> None:
		with self.assertRaisesRegex(CPanelError, '^invalid email, local-only$'):
			dispatch(self.host, ['delete', 'subaccount', 'local-only'])
		self.host.client.uapi.UserManager.delete_user.assert_not_called()


class TestAccountDispatch(unittest.TestCase):

	def setUp(self) -> None:
		self.host = Mock()
		self.host.check.side_effect = TestSubaccountDispatch.run_check


	def test_set_account_password_forwards_required_parameters(self) -> None:
		result = dispatch(self.host, ['set', 'account', 'password', 'old-secret', 'new-secret'])

		self.assertEqual(result, 'OK')
		self.host.client.uapi.UserManager.change_password.assert_called_once_with(
			oldpass = 'old-secret',
			newpass = 'new-secret',
		)


	def test_change_account_password_alias_is_supported(self) -> None:
		result = dispatch(self.host, ['change', 'account', 'password', 'old-secret', 'new-secret'])

		self.assertEqual(result, 'OK')
		self.host.client.uapi.UserManager.change_password.assert_called_once()


	def test_set_account_password_requires_both_passwords(self) -> None:
		with self.assertRaisesRegex(CPanelError, '^missing arguments for set account password'):
			dispatch(self.host, ['set', 'account', 'password', 'old-secret'])
		self.host.check.assert_not_called()
