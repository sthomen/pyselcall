from setuptools import setup,find_packages

setup(
	name = 'pyselcall',
	version = '1.0',
	packages = find_packages(),

	entry_points = {
		'console_scripts': [
			'pyselcall = pyselcall.scripts.pyselcall:run'
		]
	},

	extras_require = {
		'Direct audio playback': [ 'pyaudio' ]
	},

	author = 'Staffan Thomen',
	author_email = 'staffan@thomen.fi',
	description = ('Generate SelCall tones with python'),

	long_description='file:README.md',

	keywords = 'SelCall tone generator',

	url = 'https://mercurial.shangtai.net/pyselcall',

	license = 'BSD',

	classifiers = [
		'Development Status :: 4 - Beta',
		'Programming Languge :: Python :: 3'
	])
