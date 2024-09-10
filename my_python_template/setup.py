""" Setup Module
"""

import os
import io

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


def load_version(file_name):
    """Read a text file and return the content as a string."""
    version_file_path = os.path.join(here, file_name)
    with io.open(version_file_path, encoding="utf-8") as version_file:
        return version_file.read()


__version__ = load_version("../VERSION.txt")

setup(
    name="my_python_template",
    version=__version__,
    description="Basic python project",
    author="Md Saiful Ambia Chowdhury",
    url="",
    license="",
    author_email="sas2505@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": ["sas2505=my_python_template.command_line:main"],
    },
    install_requires=[
        "click"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "pylint",
            "pytest-mock",
            "python-dotenv",
            "pytest-dotenv"
        ],
        "doc": [],
    },
)
