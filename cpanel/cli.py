import os
import sys
import textwrap
from configparser import ConfigParser
import logging
from logging import Logger
import cpanel
from typing import List, Mapping, Tuple
from .core import NullableStr, CPanelError


log: Logger = logging.getLogger(__name__)


def die(message: NullableStr = None) -> None:
	"""Print (optional) message and exit to shell with error."""
	if message:
		print("{}: {}".format(cpanel.__name__, message), file = sys.stderr)
	sys.exit(1)


def eatvalue(args: List[str], shortopt: str, longopt: str) -> Tuple[List[str], NullableStr]:
	"""Scan args list looking for a short or long option with a value.

	args       list of arguments passed to the command line
	shortopt   short option, e.g. -x VALUE
	longopt    long option, e.g. --xxx=VALUE

	Returns tuple:
		args with options and VALUE possibly removed,
		VALUE if option is found, None otherwise
	"""
	reargs: List[str] = []
	value: NullableStr = None
	n: int = len(longopt)

	for i in range(0, len(args)):
		# Eat [ ..., '-x', 'xvalue', ... ]
		if args[i] == shortopt and i + 1 < len(args):
			value = args[i + 1]
		# Eat [ ..., '--xxx=xvalue', ... ]
		elif len(args[i]) > n and args[i][0:n + 1] == longopt + '=':
			value = args[i][n + 1:]
		elif i == 0 or args[i - 1] != shortopt:
			reargs.append(args[i])

	return reargs, value


def eatflag(args: List[str], shortopt: str, longopt: str) -> Tuple[List[str], bool]:
	"""Scan args list looking for a short or long flag option.

	args       list of arguments passed to the command line
	shortopt   short flag option, e.g. -x
	longopt    long flag option, e.g. --xxx

	Returns tuple:
		args with options possibly removed,
		True if option is found, False otherwise
	"""
	reargs: List[str] = []
	flag: bool = False

	for arg in args:
		# Eat [ ..., '-x', ... ] or [ ..., '--xxx', ... ]
		if arg == shortopt or arg == longopt:
			flag = True
		else:
			reargs.append(arg)

	return reargs, flag


def configuration(args: List[str], env: Mapping[str, str], rcfile: str) \
		-> Tuple[List[str], NullableStr, NullableStr, NullableStr]:
	"""Return a tuple with credentials to hit the cPanel API.

	args       list of arguments passed to the command line
	env        dict of current environment variables
	rcfile     an .rc properties file, with name=value lines

	Returns tuple:
		args with option values possibly removed,
		hostname,
		username,
		UAPI token associated to username
	"""
	hostname: NullableStr = None
	username: NullableStr = None
	utoken: NullableStr = None

	# Parse optional CLI values (they override both environment variables and the .rc file).
	# I don’t like argparse, manual parsing is much simpler and readable.
	args, hostname = eatvalue(args, '-H', '--hostname')
	args, username = eatvalue(args, '-U', '--username')
	args, utoken = eatvalue(args, '-T', '--utoken')

	# Check environment variables (they override the .rc file).
	if hostname is None: hostname = env.get('CPANEL_HOSTNAME')
	if username is None: username = env.get('CPANEL_USERNAME')
	if utoken is None: utoken = env.get('CPANEL_UTOKEN')

	# Finally, parse the .rc file.
	if os.path.isfile(rcfile):
		config : ConfigParser = ConfigParser()
		with open(rcfile, 'r') as stream:
			config.read_string('[cpanel]\n' + stream.read())
		try:
			if hostname is None: hostname = config['cpanel']['hostname']
			if username is None: username = config['cpanel']['username']
			if utoken is None: utoken = config['cpanel']['utoken']
		except KeyError as e:
			raise CPanelError("missing property in {}, {}".format(rcfile, str(e)))

	return args, hostname, username, utoken


def version() -> str:
	"""Return package version."""
	return "{} client version {}".format(cpanel.__description__, cpanel.__version__)


def usage(cmd: NullableStr = None) -> str:
	help: str

	if cmd == "features":
		help = """\
		Usage: cpanel list features

		List a cPanel account’s features. Output is JSON-formatted.

		For a full User’s Guide go to: https://cpanelcli.readthedocs.io/en/latest/
		"""
	elif cmd == "mail":
		help = """\
		Usage:
		    cpanel list mail accounts
		    cpanel list mail filters ACCOUNT
		    cpanel get mail filter ACCOUNT FILTERNAME
		    cpanel set mail filter ACCOUNT FILE
		    cpanel delete mail filter ACCOUNT FILTERNAME

		For a full User’s Guide go to: https://cpanelcli.readthedocs.io/en/latest/

		COMMANDS

		list mail accounts
		    Lists cPanel email accounts. Output is JSON-formatted.

		    EXAMPLE
		        cpanel list mail accounts

		list mail filters ACCOUNT
		    Lists mail filters associated to ACCOUNT. Output is a JSON-formatted
		    array of filter names.
		    ACCOUNT is the name of a cPanel email account, usually user@domain

		    EXAMPLE
		        cpanel list mail filters scott@example.com

		get mail filter ACCOUNT FILTERNAME
		    Return a JSON-formatted description of email filter FILTERNAME associated
		    to email ACCOUNT. To get a list of current filter names, use
		    ‘cpanel list mail filters ACCOUNT’

		    EXAMPLE
		        cpanel get mail filter scott@example.com spamkiller

		set mail filter ACCOUNT FILE
		    Create or update an email filter associated to email ACCOUNT.
		    If the filter already exists, it’s updated, otherwise a new filter is created.
		    The filter rules are described using a JSON FILE. This FILE has the same
		    textual format as the output from ‘cpanel get mail filter’, so the
		    easiest way to create a new filter is to dump an existing filter into a
		    filter.json file, edit it and then upload it with ‘cpanel set mail filter’.
		    See the EXAMPLE below.

		    EXAMPLE
		        cpanel get mail filter scott@example.com spamkiller > filter.json
		        # Edit filter.json, and then run:
		        cpanel set mail filter scott@example.com filter.json

		delete mail filter ACCOUNT FILTERNAME
		    Delete email filter FILTERNAME associated to ACCOUNT.

		    EXAMPLE
		         cpanel delete mail filter scott@example.com spamkiller
		"""
	else:
		help = """\
		Usage: cpanel [OPTIONS] COMMAND...

		A general CLI utility to run common tasks on a website controlled with cPanel.

		For a full User’s Guide go to: https://cpanelcli.readthedocs.io/en/latest/

		OPTIONS
		    -h, --help                  print this help and exit
		    -V, --version               print version information and exit
		    -H HOST, --hostname=HOST    cPanel server hostname
		    -U USER, --username=USER    username on cPanel server
		    -T UTOKEN, --utoken=UTOKEN  UAPI token associated to USER

		AUTHENTICATION
		You can pass the HOST, USER and UTOKEN credentials directly as options, as
		shown above, or, for your convenience, write a .cpanelrc file on your $HOME
		directory. See the User’s Guide at https://cpanel-api.readthedocs.io/ for
		more information.

		COMMAND is a sequence of two or more keywords describing a task; the general
		form of the command keyword list is:

		    cpanel VERB MODULE TARGET [ARGUMENTS...]

		EXAMPLES
		    cpanel list features
		    cpanel list mail accounts
		    cpanel get mail filter scott@example.com spamkiller

		Notice the way the keywords are arranged form a natural English sentence, i.e.,
		‘list features’, ‘get mail filter’, etc. This is done on purpose so the keyword
		order is easy to remember.

		MODULES
		The currently implemented modules are:

		‘features‘ (use ‘cpanel help features’ for more information):
		    cpanel list features

		‘mail’ (use ‘cpanel help mail’ for more information):
		    cpanel list mail accounts
		    cpanel list mail filters ACCOUNT
		    cpanel get mail filter ACCOUNT FILTERNAME
		    cpanel set mail filter ACCOUNT FILE
		    cpanel delete mail filter ACCOUNT FILTERNAME

		DEVELOPMENT
		    Visit the project page at: https://github.com/layfellow/cpanel-cli/
		"""
	return textwrap.dedent(help)
