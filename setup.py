#!/usr/bin/env python

#-----------------------------------------------------------------------------
#  Copyright (C) 2013 Bradley Froehle
#
#  Distributed under the terms of the Modified BSD License.
#
#  The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

from distutils.core import setup

setup(
    name='simpletimer',
    version='1.0',
    description='Timing functions and context manager',
    author='Bradley M. Froehle',
    author_email='brad.froehle@gmail.com',
    license='BSD'
    url='http://github.com/bfroehle/simpletimer',
    py_modules=['simpletimer'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
    ],
)
