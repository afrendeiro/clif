#! /usr/bin/env python

"""
Installer script for the ``clif`` package.

Install with ``pip install .``.
"""

from setuptools import setup, find_packages


def parse_requirements(req_file):
    """Parse requirements.txt files."""
    reqs = open(req_file).read().strip().split("\n")
    reqs = [r for r in reqs if not r.startswith("#")]
    return [r for r in reqs if "#egg=" not in r]


REQUIREMENTS_FILE = "requirements.txt"
DEV_REQUIREMENTS_FILE = "requirements.dev.txt"
README_FILE = "README.md"

# Requirements
requirements = parse_requirements(REQUIREMENTS_FILE)
requirements_dev = parse_requirements(DEV_REQUIREMENTS_FILE)

# Description
long_description = open(README_FILE).read()


# setup
setup(
    name="clif",
    packages=find_packages(),
    use_scm_version={
        "write_to": "clif/_version.py",
        "write_to_template": '__version__ = "{version}"\n',
    },
    description="A simple type hint aware package for calling a function from the command-line.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 3 - Alpha",
        "Typing :: Typed",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    keywords=",".join(["command line interface", "type hinting",]),
    url="https://github.com/afrendeiro/clif",
    project_urls={
        "Bug Tracker": "https://github.com/afrendeiro/clif/issues",
        # "Documentation": "https://clif.readthedocs.io",
        "Source Code": "https://github.com/afrendeiro/clif",
    },
    author=u"Andre Rendeiro",
    author_email="andre.rendeiro@pm.me",
    license="GPL3",
    setup_requires=["setuptools_scm"],
    install_requires=requirements,
    tests_require=requirements_dev,
    extras_require={"dev": requirements_dev},
    # package_data={"clif": ["config/*.yaml", "templates/*.html", "_models/*"]},
    data_files=[
        REQUIREMENTS_FILE,
        # "requirements/requirements.test.txt",
    ],
)
