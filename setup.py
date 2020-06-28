from distutils.core import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
with open('corecon/version.py') as fh: 
    exec(fh.read())

setup(
  name = 'corecon',
  packages = find_packages(exclude=["docs"]),
  version = __version__,
  license='gpl-3.0',
  description = 'an open collection of constraints on the Epoch of Reionization',
  long_description=long_description,
  author = 'Enrico Garaldi',
  author_email = 'enrico.garaldi@gmail.com', 
  url = 'https://github.com/EGaraldi/corecon',
  download_url = 'https://github.com/EGaraldi/corecon/archive/v'+__version__+'.tar.gz',
  keywords = ['constraints', 'reionization', 'cosmic', 'observations', 'data'],
  install_requires=['numpy'],
  classifiers=[
    'Development Status :: 4 - Beta', 
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
