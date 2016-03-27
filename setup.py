"""Setuptools configuration for interfaces."""

from setuptools import setup
from setuptools import find_packages


with open('README.rst', 'r') as readmefile:

    README = readmefile.read()

setup(
    name='asyncdef.interfaces',
    version='0.1.0',
    url='https://github.com/asyncdef/interfaces',
    description='Public APIs for the core asyncdef components.',
    author="Kevin Conway",
    author_email="kevinjacobconway@gmail.com",
    long_description=README,
    license='Apache 2.0',
    packages=find_packages(exclude=['build', 'dist', 'docs']),
    install_requires=[
        'iface',
    ],
    extras_require={
        'testing': [
            'pep257',
            'pep8',
            'pyenchant',
            'pyflakes',
            'pylint',
            'pytest',
            'pytest-cov',
        ],
    },
    entry_points={
        'console_scripts': [

        ],
    },
    include_package_data=True,
    zip_safe=False,
)