#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: R. Patrick Xian
"""

import numpy as np
import itertools as it


def boustrouphedon(nrow, ncol, rowstart=0, rowstep=1, colstart=0, colstep=1, zzdirection='row', dtyp='int'):
    """ Generating boustrouphedon index.
    """
    
    zzinds = []
    epsilon = 1e-5
    rowend = rowstart + nrow*rowstep + epsilon
    rowinds = np.arange(rowstart, rowend, dtype=dtyp)
    rowrem = rowinds % 2
    colend = colstart + ncol*colstep + epsilon
    colinds = np.arange(colstart, colend, dtype=dtyp)
    
    for r, rrem in zip(rowinds, rowrem): 
        zzinds.append(list(zip(it.repeat(r), altrange(colstart, colend, colstep, rrem))))
    
    zzinds = np.moveaxis(np.asarray(zzinds, dtype=dtyp), 2, 0)
    
    if zzdirection == 'row':
        return zzinds
    elif zzdirection == 'col':
        return np.roll(zzinds, shift=1, axis=0)