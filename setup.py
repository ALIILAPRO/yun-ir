from setuptools import setup, find_packages

setup(
	name='yun-ir',
	version='1.0',
	description='A Python client for Yun.ir URL shortener API',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='ALIILAPRO',
	author_email='aliilapro@pm.me',
	url='https://github.com/ALIILAPRO/yun-ir',
	packages=find_packages(),
	install_requires=['requests'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
	],
	license='MIT',
)