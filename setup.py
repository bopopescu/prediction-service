from setuptools import setup, find_packages

setup(
    name='Your Application',
    version='1.0',
    long_description=__doc__,
    packages=['application'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
    packages=find_packages()
)