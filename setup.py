from distutils.core import setup # Need this to handle modules
import py2exe 
import math # We have to import all modules used in our program

setup(
    options={'py2exe': {'bundle_files': 1, 'compressed': True}},
    console=['client.py'],
    zipfile=None
)