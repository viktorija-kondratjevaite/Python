from distutils.core import setup, Extension
from setuptools import setup, Extension

module = Extension("fibModule", sources = ["fibonacciModule.c"])

setup(name="fibonacciModule",
		version="1.0", 
		description="This is a package for fibonacci module",
		ext_modules = [module])
	
	
# ~$ python3 fibonacciSetup.py install --user
# ~$ python3
# >>> import fibModule
# >>> fibModule.fibonacci(10)
