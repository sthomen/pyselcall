from setuptools import setup,find_packages

setup(
	name = 'pyselcall',
	version = '1.0',
	packages = find_packages(),

	author = 'Staffan Thomen',
	author_email = 'staffan@thomen.fi',
	description = ('Generate SelCall tones with python'),
	license = 'BSD',
	keywords = 'SelCall tone generator',
	url = 'https://mercurial.shangtai.net/pyselcall',
	long_description='file:README.md',
	classifiers = [
		'Development Status :: 4 - Beta',
		'Programming Languge :: Python :: 3'
	])
