#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 17:09:19 2017

@author: Ray
"""

import sys

major_version = sys.version_info[0]

def cprint(content):
    if major_version == 2:
        print content
    else:
        print(content)