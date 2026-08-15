from collections.abc import Mapping, Sequence
from typing import Any

from .core import CPanelError


REDACTED = "<redacted>"


def redact(value: Any) -> Any:
	"""Return a logging-safe representation of potentially sensitive data.

	Command arguments and API parameter values may contain credentials, message
	bodies, or filter rules.  Preserve only container shape and mapping keys so a
	debug log can still identify the kind of value without exposing its contents.
	"""
	if isinstance(value, Mapping):
		return {str(key): redact(item) for key, item in value.items()}
	if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
		return [REDACTED for _ in value]
	return REDACTED

def cmd_is(command: str, *arglist: str) -> bool:
	"""Return whether *command* is one of the explicitly declared aliases."""
	return command in arglist


def username(email: str) -> str:
	n: int = email.find("@")
	if n < 0:
		raise CPanelError("invalid email, {}".format(email))
	return email[:n]


def domain(email: str) -> str:
	n: int = email.find("@")
	if n < 0:
		raise CPanelError("invalid email, {}".format(email))
	return email[n + 1:]
