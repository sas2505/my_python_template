"""
command module of the project
"""

from importlib import metadata
import logging
import sys
import click

from my_python_template.main import main

LOGGER = logging.getLogger(__name__)

__version__ = metadata.version("my_python_template")


@click.group()
@click.version_option(__version__)
@click.option("-v", "--verbose", count=True)
@click.option(
    "-s",
    "--something",
    required=True,
    help="This is a demo argument",
)
def sas2505(verbose, something):  # pylint: disable= unused-argument
    """Set the verbose to Info debug or warning

    Args:
        verbose ([int]): verbose level
    """
    if verbose == 1:
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    elif verbose > 1:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        logging.basicConfig(stream=sys.stdout, level=logging.WARNING)

    main()


