from setuptools import find_packages, setup

with open('README.md', 'r') as f:
	long_discription = f.read()

setup(
	name'pgbackup',
	version='0.1.0',
	author='Kyle Harris',
	author_email='kylebradlyharris@gmail.com',
	description='A utility for backing up PostgreSQL databases',
	long_discription = long_discription,
	long_discription_content_type='text/markdown',
	url='https://github.com/KBHarris/pgbackup',
	packages=find_packages('src')
)