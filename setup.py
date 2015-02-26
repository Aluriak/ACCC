# -*- coding: utf-8 -*-
#########################
#       SETUP.PY        #
#########################


#########################
# IMPORTS               #
#########################
from setuptools import setup, find_packages
from info import __version__, __name__



#########################
# SETUP                 #
#########################
setup(
    name = __name__,
    version = __version__,
    py_modules = ['info'],
    packages = find_packages(exclude=['accc/']), 
    package_data = {
        __name__ : ['README.mkd', 'LICENSE.txt']
    },
    include_package_data = True,
    zip_safe=False, # needed for avoided marshalling error

    author = "aluriak",
    author_email = "lucas.bourneuf@laposte.net",
    description = "Always Correct Correctness Compilator",
    long_description = open('README.mkd').read(),
    keywords = "compilation compiler correctness",
    url = "https://github.com/Aluriak/ACCC",

    classifiers = [
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Compilers",
    ]
)



