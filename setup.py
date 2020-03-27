from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='timetree-sdk',
    packages=['timetree_sdk', 'timetree_sdk/models/'],
    version='0.1.1',
    license='MIT',
    install_requires=['requests'],
    author='Shoya Shiraki',
    author_email='shoya.shiraki@gmail.com',
    url='https://github.com/morugu/timetree-sdk-python',
    description='TimeTree API SDK for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='TimeTree timetree time-tree api sdk',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
)
