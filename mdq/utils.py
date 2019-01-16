#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: R. Patrick Xian
"""

#import numpy as np

def altrange(start, stop, step, flag):
    """ Reversible range operator.
    """
    
    if flag == 1:
        return np.arange(start, stop, step)
    elif flag == 0:
        return reversed(np.arange(start, stop, step))