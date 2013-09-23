#!/usr/bin/env python
from setuptools import setup

setup(
    name="podcastdl",
    version="0.1",
    py_modules=['podcastdl'],
    author='Alexis Metaireau',
    author_email='alexis@notmyidea.org',
    description="A simple script to parse a rss and download its mp3 files",
    long_description=open('README.rst').read(),
    install_requires=['feedparser', 'progressbar', 'requests'],
    entry_points={'console_scripts': ['podcastdl = podcastdl:main']},
    classifiers=[
         'Environment :: Console',
         'License :: OSI Approved :: Common Public License',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 2.7',
         'Topic :: Internet :: WWW/HTTP',
    ]
)
