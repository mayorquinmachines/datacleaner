from setuptools import setup, find_packages

import os


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='datacleaner',
      version='1.0',
      description='data cleaning library for sequences of images',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/mayorquinmachines/datacleaner',
      author='Salma Mayorquin',
      license='MIT',
      entry_points={
          'console_scripts': [
              'datacleaner=datacleaner.base:execute_from_command_line',
          ],
      },
      install_requires=['pillow',
                        'docopt',
                        'tornado==4.5.3',
                        'requests',
                        'h5py',
                        'python-socketio',
                        'flask',
                        'eventlet'
                        ],

      extras_require={
                      'dev': [
                          'pytest',
                          'pytest-cov',
                          'responses'
                          ],
                      'ci': ['codecov']
                  },

      include_package_data=True,

      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          # Indicate who your project is intended for
          'Intended Audience :: Developers',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',

          # Pick your license as you wish (should match "license" above)
          'License :: OSI Approved :: MIT License',

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.

          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='datacleaning machinelearning deeplearning data',

      packages=find_packages(exclude=(['tests', 'docs', 'site', 'env'])),
      )
