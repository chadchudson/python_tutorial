#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : 'My Project',
    'author' : 'Chad Hudson',
    'url' : 'www.chad.tennhud.com',
    'download_url' : 'www.chad.tennhud.com/projects',
    'author_email' : 'chad@tennhud.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'projectname'
}

setup(**config)
