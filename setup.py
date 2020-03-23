# coding: utf-8

from setuptools import setup

setup(
    name="pytestwait",
    packages=["pytestwait"],
    # the following makes a plugin available to pytest
    entry_points={"pytest11": ["name_of_plugin = pytestwait.plugin"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)