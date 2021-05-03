import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
  name='quarkz',
  version='0.0.1',
  url='github.com/quarkz-encryption/quarkz',
  author='tavivia',
  author_email='tavian@quarkz-encryption.com',
  packages=find_packages(),
  platforms='any',
  license='MIT',
  package_data={'': ['helpers/chi2_lookup_table.npy', 'templates/*']},
  ext_modules=[],
  description="An Encryption library",
  long_description='See https://github.com/quarkz-encryption/quarkz',
)
