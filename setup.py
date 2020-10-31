import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
	name='projectalice-unittest',
	author='ProjectAlice',
	version='0.0.1',
	maintainer='Psychokiller1888',
	maintainer_email='laurentchervet@bluewin.ch',
	description='Package to run unittests on skills',
	long_description=readme,
	long_description_content_type='text/markdown',
	url='https://github.com/project-alice-assistant/ProjectAliceSkillKit',
	license='GPL-3.0',
	packages=find_packages(),
	include_package_data=True,
	use_scm_version=False,
	setup_requires=['setuptools_scm'],
	install_requires=[],
	classifiers=[
		"Development Status :: 1 - Planning",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.7",
		"Topic :: Software Development :: Testing"
	]
)
