"""
Entry point module of the project
"""

import logging
import sys
import click

from my_python_template.cli import sas2505


LOGGER = logging.getLogger(__name__)


HELP_BLURB = (
    "To see help text, you can run:\n"
    "\n"
    "  sas2505 --help\n"
    "  sas2505 <command> --help\n"
    "  sas2505 <command> <subcommand> --help\n"
)

# generated from https://texteditor.com/ascii-art/
# pylint: disable=anomalous-backslash-in-string, line-too-long
LOGO = (
    "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄\n"
    "█░▄▄█░▄▄▀█░▄▄█░▄░█░▄▄█░▄▄░█░▄▄\n"
    "█▄▄▀█░▀▀░█▄▄▀██▀▄█▄▄▀█░▀▄░█▄▄▀\n"
    "█▄▄▄█▄██▄█▄▄▄█░▀▀█▀▀▄█░▀▀░█▀▀▄\n"
    "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\n"
)

USAGE = (
    "sas2505 [verbose options] <command> <subcommand> " "[parameters]\n" f"{HELP_BLURB}"
)


def main():
    """Main function"""
    try:
        click.echo(LOGO)
        ctx = sas2505.make_context("cli", sys.argv[1:])
        with ctx:
            result = sas2505.invoke(ctx)
            sys.exit(result)
    except click.exceptions.Exit as error:
        sys.exit(error.exit_code)
    except click.ClickException as error:
        LOGGER.error(error)
        LOGGER.debug(str(error))
        sys.exit(-1)
    except Exception as error:  # pylint: disable=broad-except
        LOGGER.critical(error)
        LOGGER.exception(error)
        LOGGER.debug(str(error))
        sys.exit(-2)


main()
