# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 10:25:22 2019

@author: lealp
"""

from setuptools import setup, find_packages
import os
import glob
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    
    path_file = glob.glob(os.path.join(os.path.dirname(__file__), fname + '*'))
    
    
    return open(path_file[0]).read()







setup(
    name = "gcdistance",
    version = "0.0.1",
    author = "Philipe Leal",
    
    # adicionando manualmente cada um dos packages da lib:
        #packages=['gcdistance'], 
        
    # se tivermos vários packages, podemos usar: 
    
    packages=find_packages(),
    #package_dir={'':'gcdistance'} ,
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['numpy', 'docutils>=0.3', 
                      'nose', 'nose-cover3' # these two packages are for testing
                      
                      ],
    
    url='https://github.com/PhilipeRLeal/geoscience_operations',
    
    scripts=['gcdistance/gcdistance.py'],
    
    # In order for these files to be copied at install 
    # time to the package’s folder inside site-packages, 
        # it is mandatory to supply  "include_package_data
    
    include_package_data=True,
    
    author_email="leal.philipe@gmail.com",
    description="This is an Example Package to calculate distances between points in a sphere with settable radius",
    keywords="sphere two point distances",
    
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: geographical distances estimation :: Geosciences',
    ],
    
    long_description=read('README'),
    
)