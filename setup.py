#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="pyconsensus",
    version="0.1",
    description="Consensus mechanism for Truthcoin",
    author="Jack Peterson",
    author_email="<jack@dyffy.com>",
    maintainer="Jack Peterson",
    maintainer_email="<jack@dyffy.com>",
    license="GPL",
    url="https://github.com/tensorjack/pyconsensus",
    download_url = "https://github.com/tensorjack/pyconsensus/tarball/0.1",
    packages=["pyconsensus"],
    install_requires=["numpy"],
    keywords = ["consensus", "truthcoin", "svd", "oracle"]
)
