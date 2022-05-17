import os
from setuptools import setup, find_packages
from pkg_resources import parse_requirements

here = os.path.abspath(os.path.dirname(__file__))

setup(
  name='quarkz',
  version='0.0.2',
  url='https://github.com/quarkz-encryption/Quarkz',
  author='tavivia',
  author_email='tavian@quarkz-encryption.com',
  packages=find_packages(exclude=("tests",)),
  install_reqs=['pycryptodome'],
  platforms='any',
  license='MIT',
  ext_modules=[],
  description="An Encryption library",
  long_description='See https://github.com/quarkz-encryption/quarkz',
)
