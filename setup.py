#! /usr/bin/python
from setuptools import setup

setup(name='kerry_dash',
      version='1.0',
      description='Creates dynamic subgroups of a customer group within LogicMonitor and automatically imports dashboards',
      url='https://github.com/ianbloom/kerry_dash',
      author='ianbloom',
      author_email='ian.bloom@gmail.com',
      license='MIT',
      packages=['api_helpers'],
      install_requires=[
          'requests',
          'argparse',
          'pprint'
      ],
      zip_safe=False)