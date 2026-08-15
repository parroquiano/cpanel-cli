import os
import tempfile
import unittest
from unittest.mock import patch

from cpanel.__main__ import main
from cpanel.cli import configuration, eatflag, eatvalue
from cpanel.util import REDACTED, redact


class TestOptionParsing(unittest.TestCase):

	def test_eatvalue_supports_short_and_long_forms(self) -> None:
		args, value = eatvalue(['list', '-H', 'short.test'], '-H', '--hostname')
		self.assertEqual(args, ['list'])
		self.assertEqual(value, 'short.test')

		args, value = eatvalue(['--hostname=long.test', 'list'], '-H', '--hostname')
		self.assertEqual(args, ['list'])
		self.assertEqual(value, 'long.test')


	def test_eatflag_removes_all_occurrences(self) -> None:
		args, enabled = eatflag(['-h', 'list', '--help'], '-h', '--help')
		self.assertEqual(args, ['list'])
		self.assertTrue(enabled)


class TestConfiguration(unittest.TestCase):

	def test_cli_overrides_environment_and_file(self) -> None:
		with tempfile.NamedTemporaryFile('w') as stream:
			stream.write('hostname=file.test\nusername=file-user\nutoken=file-token\n')
			stream.flush()
			args, hostname, username, token = configuration(
				['-H', 'cli.test', '-U', 'cli-user', '-T', 'cli-token', 'list', 'features'],
				{'CPANEL_HOSTNAME': 'env.test', 'CPANEL_USERNAME': 'env-user', 'CPANEL_UTOKEN': 'env-token'},
				stream.name,
			)
		self.assertEqual(args, ['list', 'features'])
		self.assertEqual((hostname, username, token), ('cli.test', 'cli-user', 'cli-token'))


	def test_environment_overrides_file(self) -> None:
		with tempfile.NamedTemporaryFile('w') as stream:
			stream.write('hostname=file.test\nusername=file-user\nutoken=file-token\n')
			stream.flush()
			_, hostname, username, token = configuration(
				[],
				{'CPANEL_HOSTNAME': 'env.test', 'CPANEL_USERNAME': 'env-user', 'CPANEL_UTOKEN': 'env-token'},
				stream.name,
			)
		self.assertEqual((hostname, username, token), ('env.test', 'env-user', 'env-token'))


	def test_reading_default_configuration_does_not_create_directory(self) -> None:
		with tempfile.TemporaryDirectory() as home:
			config_home = os.path.join(home, 'not-created')
			with patch('cpanel.cli.os.path.expanduser', return_value = home):
				configuration([], {'XDG_CONFIG_HOME': config_home})
			self.assertFalse(os.path.exists(config_home))


class TestRedaction(unittest.TestCase):

	def test_redacts_tokens_passwords_and_message_bodies(self) -> None:
		secret_values = {
			'utoken': 'TOKEN-123',
			'password': 'password-123',
			'body': 'private message',
			'nested': ['address@example.test'],
		}
		redacted = redact(secret_values)
		self.assertEqual(redacted['utoken'], REDACTED)
		self.assertEqual(redacted['password'], REDACTED)
		self.assertEqual(redacted['body'], REDACTED)
		self.assertEqual(redacted['nested'], [REDACTED])
		self.assertNotIn('TOKEN-123', repr(redacted))


	def test_debug_logging_does_not_expose_credentials_or_command_values(self) -> None:
		argv = [
			'cpanel', '-H', 'server.test', '-U', 'api-user', '-T', 'TOKEN-123',
			'create', 'ftp', 'account@example.test', 'PASSWORD-123', '100',
		]
		with patch('cpanel.__main__.sys.argv', argv), \
				patch('cpanel.__main__.endpoint', return_value = object()), \
				patch('cpanel.__main__.dispatch', return_value = 'OK'), \
				patch('builtins.print') as print_result, \
				self.assertLogs('cpanel', level = 'DEBUG') as captured:
			main()
		print_result.assert_called_once_with('OK')
		output = '\n'.join(captured.output)
		self.assertNotIn('TOKEN-123', output)
		self.assertNotIn('PASSWORD-123', output)
		self.assertNotIn('account@example.test', output)


if __name__ == '__main__':
	unittest.main()
