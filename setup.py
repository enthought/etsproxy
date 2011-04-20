#!/usr/bin/env python

from setuptools import setup, find_packages


version = '0.1.0'


setup(
    name = 'etsproxy',
    version = version,
    packages = find_packages(),
    author = 'Enthought, Inc.',
    author_email = 'info@enthought.com',
    download_url = ('http://www.enthought.com/repo/ets/etsproxy-%s.tar.gz' %
                    version),
    license = 'BSD',
    maintainer = 'ETS Developers',
    maintainer_email = 'enthought-dev@enthought.com',
)
