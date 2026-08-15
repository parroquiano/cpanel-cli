import unittest
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
