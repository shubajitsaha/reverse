from setuptools import setup

setup(name='reverse',
      version='1.0',
      # list folders, not files
      packages=['reverse',
                'reverse.test'],
      scripts=['bin/reverse_file.py'],
      )