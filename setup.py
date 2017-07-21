from setuptools import setup, find_packages
setup(
    name = "testbuildout",
    version = "0.0.1",
    url = "https://github.com/abelweiwencai/learngit.git",
    license = 'BSD',
    description = "A short test for use biuldout in django",
    author = 'Abel Wei',
    packages = find_packages('wei'),
    package_dir = {'': 'wei'},
    install_requires = ['setuptools']
)
