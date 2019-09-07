#!/usr/bin/env python3


from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
	name="webhook_script_execution",
	version="0.0.1",
	url="",  # Todo: set url
	license="MIT",
	author="autofelge1024",
	author_mail="mail@autofelge1024.de",
	description="A simpla and small webserver to react to wekhook-calls by executing scripts."
				"For simplicity, webhook-urls and scripts are configured in a configfile.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: POSIX",
	],
	packages=["webhook_script_execution"],
	python_requires=">=3.4",  # todo: check
)