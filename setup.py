from setuptools import setup, find_packages
setup(
    name = "mydjango",
    version = "0.0.1",
    url = "https://github.com/abelweiwencai/mydjango.git",
    license = 'BSD',
    description = "A short test for use biuldout in django",
    author = 'Abel Wei',
    packages = find_packages('weiwc'),
    package_dir = {'': 'weiwc'},
    install_requires = ['setuptools']
)
