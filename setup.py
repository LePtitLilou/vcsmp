
#  Usage:
#
#    python setup.py install 
#
#
from numpy.distutils.core import setup, Extension
import os, sys, string, time, shutil
Version = "0.1"

setup (name = "vcsbm",
       version=Version,
       description = "Visualization and Control System for Matplotlib/Basemap",
       url = "http://leptitlilou.com",
       packages = ['vcsbm', ],
       package_dir = {'vcsbm': 'Lib',
                     },
       )

