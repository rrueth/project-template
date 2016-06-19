import codecs
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='<package name>',
    version='<package version>', # e.g. "1.0.0"
    description='<short description>',
    long_description=long_description,
    url='<url to repo (e.g. github)>',
    license='MIT',
    author='<your name>',
    author_email='<your email>',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ], # Add any additional classifiers as defined at https://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords="<keyword1> <keyword2> <keyword3>",
    packages=find_packages(exclude=['tests*']),
    install_requires=["<dependency1>, <dependency2>"],
)

# Some common classifiers:
# 'Development Status :: 3 - Alpha',
# 'Intended Audience :: Developers',
# 'Topic :: Software Development :: Libraries :: Python Modules',