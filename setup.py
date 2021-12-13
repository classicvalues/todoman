#!/usr/bin/env python3
from setuptools import setup

setup(
    name="todoman",
    description="A simple CalDav-based todo manager.",
    author="Hugo Osvaldo Barrera",
    author_email="hugo@barrera.io",
    url="https://github.com/pimutils/todoman",
    license="ISC",
    packages=["todoman"],
    include_package_data=True,
    entry_points={"console_scripts": ["todo = todoman.cli:cli"]},
    install_requires=[
        "atomicwrites",
        "click>=7.1,<9.0",
        "click-log>=0.2.1",
        "humanize",
        "icalendar>=4.0.3",
        "parsedatetime",
        "python-dateutil",
        "pyxdg",
        "urwid",
    ],
    long_description=open("README.rst").read(),
    use_scm_version={
        "version_scheme": "post-release",
        "write_to": "todoman/version.py",
    },
    setup_requires=["setuptools_scm"],
    tests_require=open("requirements-dev.txt").readlines(),
    extras_require={
        "docs": open("requirements-docs.txt").readlines(),
        "repl": ["click-repl>=0.1.6"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Office/Business :: Scheduling",
        "Topic :: Utilities",
    ],
)
