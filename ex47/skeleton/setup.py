try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'ex47',
	'author': 'Daniel Ortega',
	'url': 'NA',
	'download_url': 'NA',
	'author_email': 'dortega88@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'ex47'
}

setup(**config)

