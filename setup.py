from setuptools import setup, find_packages

setup(
    name="Nooploop-UWB",
    version='0.0.1',
    author="JaySurplus",
    author_email="znznbest2004@gmail.com",
    description="Nooploop LinkTrack UWB Products Python API.",
    packages=['nooploop_uwb', 'nooploop_uwb.utils'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: None",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pyserial>=3.4',
    ],
)