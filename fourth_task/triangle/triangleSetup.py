from distutils.core import setup, Extension
from setuptools import setup, Extension

module = Extension("triangle", sources = ["triangleModule.c"])

setup(name="triangleModule",
		version="1.0", 
		description="This is a package for a triangle.",
		ext_modules = [module])
		
		
# ~$ python3 triangleSetup.py install --user
# ~$ python3
# >>> import triangle
# >>> t=triangle.Triangle(3,4,5)
# >>> t.perimeter()
# >>> t.area()

