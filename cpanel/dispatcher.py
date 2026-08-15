import logging
from collections.abc import Callable
from dataclasses import dataclass
from logging import Logger

from .caller import (
	accounts, addons, backup, bandwidth, cache, dir, dns, domains, features,
	files, ftp, ip, locale, logmanager, mail_accounts, mail_autoresponders,
	mail_boxes, mail_filters, mail_forwarders, mail_incoming, mail_login,
	mail_outgoing, mail_quota, mail_settings, mail_usage, mailman, mysql,
	postgres, quota, spam, ssh, stats, subaccounts, themes, usage, webmail,
)
from .core import CPanelEndpoint, CPanelError


log: Logger = logging.getLogger(__name__)
Handler = Callable[[CPanelEndpoint, str, list[str]], str]


@dataclass(frozen = True)
class CommandSpec:
	"""A command's exact aliases, positional argument bounds, and handler."""

	aliases: tuple[str, ...]
	min_arguments: int
	max_arguments: int | None
	handler: Handler

	@property
	def canonical(self) -> str:
		return self.aliases[0]

	@property
	def command_length(self) -> int:
		return len(self.canonical.split())

	def match(self, args: list[str]) -> tuple[str, int] | None:
		for alias in self.aliases:
			words = alias.split()
			if args[:len(words)] == words:
				return alias, len(words)
		return None


def command(
	handler: Handler,
	aliases: str,
	min_arguments: int = 0,
	max_arguments: int | None = 0,
) -> CommandSpec:
	return CommandSpec(tuple(aliases.split('|')), min_arguments, max_arguments, handler)


# Singular and plural spellings accepted by earlier releases are declared
# explicitly.  Positional bounds are relative to the command words themselves.
COMMANDS: tuple[CommandSpec, ...] = (
	command(features.call, 'list feature|list features'),
	command(features.call, 'get feature detail|get feature details'),
	command(features.call, 'has feature', 1, 1),
	command(quota.call, 'get quota'), command(usage.call, 'get usage'),
	command(stats.call, 'list stats domain|list stats domains'),
	command(stats.call, 'get stats bandwidth'),
	command(stats.call, 'get stats domain', 1, 3),
	command(stats.call, 'get stats', 0, None),
	command(ssh.call, 'get ssh port'),
	command(ip.call, 'block ip', 1, 1), command(ip.call, 'unblock ip', 1, 1),
	command(accounts.call, 'list account|list accounts'), command(accounts.call, 'get account'),
	command(addons.call, 'list addon instance|list addon instances', 1, 1),
	command(addons.call, 'list addon|list addons'), command(addons.call, 'get addon instance', 1, 1),
	command(subaccounts.call, 'list subaccount|list subaccounts'),
	command(subaccounts.call, 'get subaccount', 1, 1),
	command(subaccounts.call, 'get service subaccount', 2, 2),
	command(subaccounts.call, 'check subaccount conflicts', 1, 1),
	command(subaccounts.call, 'create subaccount', 2, 2),
	command(subaccounts.call, 'delete subaccount|rm subaccount|remove subaccount', 1, 1),
	command(backup.call, 'create backup', 1, 6), command(backup.call, 'list backup|list backups'),
	command(backup.call, 'restore backup', 1, 1),
	command(cache.call, 'update cache'), command(cache.call, 'read cache'),
	command(locale.call, 'list locale|list locales'), command(locale.call, 'get locale'),
	command(locale.call, 'set locale', 1, 1),
	command(themes.call, 'list theme|list themes'), command(themes.call, 'get theme'),
	command(themes.call, 'set theme', 1, 1),
	command(dir.call, 'list dir indexing', 1, 1), command(dir.call, 'get dir indexing', 1, 1),
	command(dir.call, 'set dir indexing', 2, 2),
	command(dir.call, 'list dir privacy', 1, 1), command(dir.call, 'get dir privacy', 1, 1),
	command(dir.call, 'enable dir privacy', 1, 1), command(dir.call, 'disable dir privacy', 1, 1),
	command(dir.call, 'add dir user', 3, 3),
	command(dir.call, 'delete dir user|rm dir user|remove dir user', 2, 2),
	command(dir.call, 'list dir users', 1, 1), command(dir.call, 'list dir protection', 1, 1),
	command(dns.call, 'check dns', 1, 1), command(dns.call, 'authoritative dns', 1, 1),
	command(dns.call, 'lookup dns', 1, 1), command(dns.call, 'list dynamic dns'),
	command(dns.call, 'create dynamic dns', 1, 2), command(dns.call, 'recreate dynamic dns', 1, 1),
	command(dns.call, 'update dynamic dns', 2, 2),
	command(dns.call, 'delete dynamic dns|rm dynamic dns|remove dynamic dns', 1, 1),
	command(domains.call, 'list domain data'), command(domains.call, 'list domain|list domains'),
	command(domains.call, 'get domain data', 1, 1), command(domains.call, 'get domain aliases'),
	command(logmanager.call, 'get log settings'),
	command(logmanager.call, 'set log settings', 1, None), command(logmanager.call, 'unset log settings', 1, None),
	command(logmanager.call, 'list log archives'), command(logmanager.call, 'get log', 2, 2),
	command(bandwidth.call, 'get bandwidth services'), command(bandwidth.call, 'get bandwidth retention'),
	command(files.call, 'list files', 0, 1), command(files.call, 'glob files', 1, 1),
	command(files.call, 'get file info', 1, 1), command(files.call, 'cat file', 1, 1),
	command(files.call, 'write file', 2, 2), command(files.call, 'upload file', 2, 2),
	command(files.call, 'delete file trash|rm file trash|remove file trash', 0, 1),
	command(mail_accounts.call, 'count mail account|count mail accounts'),
	command(mail_accounts.call, 'list mail account|list mail accounts'),
	command(mail_settings.call, 'get mail setting|get mail settings', 1, 1),
	command(mail_incoming.call, 'suspend mail incoming', 1, 1), command(mail_incoming.call, 'unsuspend mail incoming', 1, 1),
	command(mail_outgoing.call, 'suspend mail outgoing', 1, 1), command(mail_outgoing.call, 'unsuspend mail outgoing', 1, 1),
	command(mail_login.call, 'suspend mail login', 1, 1), command(mail_login.call, 'unsuspend mail login', 1, 1),
	command(mail_boxes.call, 'list mail box|list mail boxes', 0, 2),
	command(mail_autoresponders.call, 'list mail autoresponder|list mail autoresponders', 1, 1),
	command(mail_autoresponders.call, 'count mail autoresponder|count mail autoresponders'),
	command(mail_autoresponders.call, 'get mail autoresponder', 1, 1),
	command(mail_autoresponders.call, 'set mail autoresponder', 1, 6),
	command(mail_autoresponders.call, 'delete mail autoresponder|rm mail autoresponder|remove mail autoresponder', 1, 1),
	command(mail_forwarders.call, 'add mail forwarder', 2, None),
	command(mail_forwarders.call, 'list mail forwarder|list mail forwarders', 0, 1),
	command(mail_forwarders.call, 'count mail forwarder|count mail forwarders'),
	command(mail_forwarders.call, 'delete mail forwarder|rm mail forwarder|remove mail forwarder', 1, 1),
	command(mail_filters.call, 'list mail filter|list mail filters', 1, 1),
	command(mail_filters.call, 'count mail filter|count mail filters'),
	command(mail_filters.call, 'get mail filter', 2, 2), command(mail_filters.call, 'set mail filter', 2, 2),
	command(mail_filters.call, 'enable mail filter', 2, 2), command(mail_filters.call, 'disable mail filter', 2, 2),
	command(mail_filters.call, 'delete mail filter|rm mail filter|remove mail filter', 2, 2),
	command(mail_filters.call, 'move mail filter', 3, 4), command(mail_filters.call, 'trace mail filter', 2, 2),
	command(mail_filters.call, 'list filter domain|list filter domains'),
	command(mail_quota.call, 'get mail quota', 1, 1), command(mail_quota.call, 'set mail quota', 2, 2),
	command(mail_usage.call, 'get mail usage', 1, 1),
	command(webmail.call, 'get webmail setting|get webmail settings', 0, 1),
	command(webmail.call, 'list webmail app|list webmail apps'),
	command(spam.call, 'enable spam assassin'), command(spam.call, 'disable spam assassin'),
	command(spam.call, 'enable spam box'), command(spam.call, 'clear spam box'), command(spam.call, 'disable spam box'),
	command(spam.call, 'get spam settings'), command(spam.call, 'set spam score', 1, 1),
	command(spam.call, 'add spam denylist', 1, None),
	command(spam.call, 'delete spam denylist|rm spam denylist|remove spam denylist', 1, None),
	command(spam.call, 'add spam allowlist', 1, None),
	command(spam.call, 'delete spam allowlist|rm spam allowlist|remove spam allowlist', 1, None),
	command(spam.call, 'set spam autodelete score', 1, 1), command(spam.call, 'disable spam autodelete'),
	command(spam.call, 'list spam rule|list spam rules'), command(spam.call, 'set spam rule score', 2, 2),
	command(mailman.call, 'add mailman list', 2, 3),
	command(mailman.call, 'delete mailman list', 1, 1),
	command(mailman.call, 'count mailman list|count mailman lists'),
	command(mailman.call, 'list mailman list|list mailman lists'),
	command(mailman.call, 'add mailman delegate', 2, None),
	command(mailman.call, 'delete mailman delegate|rm mailman delegate|remove mailman delegate', 2, None),
	command(mailman.call, 'list mailman delegate|list mailman delegates', 1, 1),
	command(mailman.call, 'check mailman delegate', 1, 1),
	command(mailman.call, 'generate mailman password', 1, 1),
	command(mailman.call, 'set mailman password', 2, 2), command(mailman.call, 'get mailman usage'),
	command(mailman.call, 'set mailman private', 1, 1), command(mailman.call, 'set mailman public', 1, 1),
	command(ftp.call, 'create ftp', 3, 4), command(ftp.call, 'check ftp', 1, 1),
	command(ftp.call, 'get ftp quota', 1, 1), command(ftp.call, 'get ftp anon', 0, 1),
	command(ftp.call, 'get ftp welcome'), command(ftp.call, 'get ftp port'), command(ftp.call, 'get ftp server'),
	command(ftp.call, 'get ftp', 1, 1),
	command(ftp.call, 'set ftp quota', 2, 2), command(ftp.call, 'set ftp dir', 2, 2),
	command(ftp.call, 'set ftp password', 2, 2),
	command(ftp.call, 'set ftp welcome', 1, 1),
	command(ftp.call, 'list ftp account|list ftp accounts'), command(ftp.call, 'list ftp session|list ftp sessions'),
	command(ftp.call, 'kill ftp session', 1, 1),
	command(ftp.call, 'delete ftp|rm ftp|remove ftp', 1, 1),
	command(ftp.call, 'enable ftp anon', 0, 1), command(ftp.call, 'disable ftp anon', 0, 1),
	command(mysql.call, 'create mysql user', 2, 2), command(mysql.call, 'list mysql user|list mysql users'),
	command(mysql.call, 'rename mysql user', 2, 2), command(mysql.call, 'set mysql password', 2, 2),
	command(mysql.call, 'delete mysql user|rm mysql user|remove mysql user', 1, 1),
	command(mysql.call, 'create mysql database', 1, 1), command(mysql.call, 'list mysql database|list mysql databases'),
	command(mysql.call, 'rename mysql database', 2, 2),
	command(mysql.call, 'delete mysql database|rm mysql database|remove mysql database', 1, 1),
	command(mysql.call, 'check mysql database', 1, 1), command(mysql.call, 'repair mysql database', 1, 1),
	command(mysql.call, 'set mysql privilege', 3, None), command(mysql.call, 'list mysql privilege', 2, 2),
	command(mysql.call, 'delete mysql privilege|rm mysql privilege|remove mysql privilege', 2, 2),
	command(mysql.call, 'list mysql routine|list mysql routines', 0, 1), command(mysql.call, 'get mysql schema', 1, 1),
	command(mysql.call, 'add mysql host', 1, 2), command(mysql.call, 'annotate mysql host', 2, 2),
	command(mysql.call, 'list mysql host|list mysql hosts'),
	command(mysql.call, 'delete mysql host|rm mysql host|remove mysql host', 1, 1),
	command(mysql.call, 'get mysql server'), command(mysql.call, 'get mysql restriction'),
	command(postgres.call, 'create postgres user', 2, 2), command(postgres.call, 'list postgres user|list postgres users'),
	command(postgres.call, 'rename postgres user', 3, 3), command(postgres.call, 'set postgres password', 2, 2),
	command(postgres.call, 'delete postgres user|rm postgres user|remove postgres user', 1, 1),
	command(postgres.call, 'create postgres database', 1, 1),
	command(postgres.call, 'list postgres database|list postgres databases'),
	command(postgres.call, 'rename postgres database', 2, 2),
	command(postgres.call, 'delete postgres database|rm postgres database|remove postgres database', 1, 1),
	command(postgres.call, 'set postgres privilege', 2, 2),
	command(postgres.call, 'delete postgres privilege|rm postgres privilege|remove postgres privilege', 2, 2),
	command(postgres.call, 'sync postgres grant'), command(postgres.call, 'get postgres restriction'),
)


def dispatch(host: CPanelEndpoint, args: list[str]) -> str:
	"""Validate and execute the command represented by *args*."""
	matches: list[tuple[CommandSpec, str, int]] = []
	for specification in COMMANDS:
		matched = specification.match(args)
		if matched is not None:
			alias, length = matched
			matches.append((specification, alias, length))

	if not matches:
		command_text = " ".join(args[:4])
		raise CPanelError("unrecognized command, {}".format(command_text))

	# Prefer the most specific alias when one command is a prefix of another.
	specification, alias, command_length = max(matches, key = lambda item: item[2])
	argument_count = len(args) - command_length
	if argument_count < specification.min_arguments:
		raise CPanelError(
			"missing arguments for {}, please use ‘cpanel help {}’".format(
				alias, args[1] if len(args) > 1 else '--help'))
	if specification.max_arguments is not None and argument_count > specification.max_arguments:
		raise CPanelError("too many arguments for {}".format(alias))

	log.debug("dispatching command=%s argument_count=%d", alias, argument_count)
	return specification.handler(host, specification.canonical, args)
