from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='nooploop-uwb',
    license='MIT',
    version='0.0.1',
    author="JaySurplus",
    author_email="znznbest2004@gmail.com",
    description="Nooploop LinkTrack UWB Products Python API.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JaySurplus/nooploop_uwb',
    download_url='https://github.com/JaySurplus/nooploop_uwb/releases',
    packages=['nooploop_uwb', 'nooploop_uwb.utils'],
    platforms=['Ubuntu 20.04','Ubuntu 18.04*', 'Ubuntu 16.04*', 'Windows 10'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyserial>=3.4',
    ],
)