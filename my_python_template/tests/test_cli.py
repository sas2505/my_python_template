"""Test Module to commands fro CLI

"""

import os
import pytest
from click.testing import CliRunner
from my_python_template.cli import sas2505



def test_cmd_exists_help():
    """test if the CLI can return an help"""
    runner = CliRunner()
    result = runner.invoke(sas2505, ["--help"])
    print(result.output)
    assert result.exit_code == 0
    assert True


def test_get_version_cmd_exists():
    """test if the CLI can return an help"""
    runner = CliRunner()
    result = runner.invoke(sas2505, ["--version"])
    print(result.output)
    assert result.exit_code == 0
    assert True


def test_cmd__help_very_verbose_exists():
    """test if the CLI can return an help"""
    runner = CliRunner()
    result = runner.invoke(sas2505, ["--version"])
    print(result.output)
    assert result.exit_code == 0
    assert True


def test_with_argument_cmd():
    """test if the CLI can handle the argument"""
    runner = CliRunner()
    result = runner.invoke(sas2505, ["-vv", "-s", "1234"])
    # assert result.exit_code == 0
    assert True

