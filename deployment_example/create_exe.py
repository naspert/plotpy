#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Deployment example
==================

Deployment script using `plotpy.disthelpers` (py2exe or cx_Freeze)
"""

from plotpy import disthelpers as dh

def create_exe():
    dist = dh.Distribution()
    dist.setup('example', '1.0', 'plotpy app example', 'simpledialog.pyw')
    dist.add_modules('plotpy')
    dist.build_cx_freeze()  # use `build_py2exe` to use py2exe instead

if __name__ == '__main__':
    create_exe()
    