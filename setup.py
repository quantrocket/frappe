#!/usr/bin/env python
#! -*- encoding: utf-8 -*-

__author__ = "joaonrb"

import os
#from distutils.core import setup
from setuptools import setup
from setuptools import find_packages


def get_requirements():
    with open("requirements.txt") as reqs_file:
        reqs = [x.replace("\n", "").strip() for x in reqs_file if bool(x.strip()) and not x.startswith("#") and
                not x.startswith("https://")]
        return reqs


with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="frappe",
    version="2.0",
    description="Frappe recommendation system implementation for FireFox system",
    author="Linas Baltrunas",
    author_email="linas@tid.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={
        "": ["*.txt"],
    },
    test_suite = "tests/suite",
    scripts=[],
    license="copyright.txt",
    include_package_data=True,
    install_requires=get_requirements()+["testfm"],
    dependency_links=[
        "git+ssh://git@github.com/grafos-ml/test.fm.git@v1.0.4#egg=testfm-1.0.4",
        #"git+https://github.com/grafos-ml/test.fm/archive/v1.0.4.tar.gz",
    ],
    long_description=README,
    classifiers=[
        "Development Status :: 2 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Firefox",
        "Operating System :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)