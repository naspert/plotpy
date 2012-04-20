#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Setup script for distributing SIFT as a stand-alone executable
# SIFT is the Signal and Image Filtering Tool
# Simple signal and image processing application based on guiqwt and guidata
# (see guiqwt/tests/sift.py)

"""Create a stand-alone executable"""

try:
    from guidata.disthelpers import Distribution
except ImportError:
    raise ImportError, "This script requires guidata 1.4+"

# Importing modules to be bundled
from guiqwt.tests import sift


def create_executable():
    """Build executable using ``guidata.disthelpers``"""
    dist = Distribution()
    dist.setup(name=u"Sift", version=sift.VERSION,
               description=u"Signal and Image Filtering Tool",
               script="sift.pyw", target_name="sift.exe", icon="sift.ico")
    dist.add_modules('guidata', 'guiqwt')
    try:
        import spyderlib
        spyderlib.add_to_distribution(dist)
    except ImportError:
        pass
    dist.excludes += ['IPython']

    # Building executable
    dist.build('cx_Freeze')


if __name__ == '__main__':
    create_executable()