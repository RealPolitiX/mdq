#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
@author: R. Patrick Xian
"""

from . import utils as u
import numpy as np
import itertools as it


def boustrouphedon(nrow, ncol, rowstart=0, rowstep=1, colstart=0, colstep=1,
                    move_direction='row', dtyp='int'):
    """ Generating 2D indices in boustrouphedon ordering.

    :Parameters:
        nrow, ncol : int, int
            Number of rows and columns.
        rowstart, rowstep : int, int | 0, 1
            Start and step of row index.
        colstart, colstep : int, int | 0, 1
            Start and step of column index.
        move_direction : str | 'row'
            Moving direction, along the row ('row') or column ('col').
        dtyp : str | 'int'
            Index data type.

    :Return:
        indices : array/list
            Indices in boustrouphedon ordering.
    """

    indices = []
    epsilon = 1e-5

    rowend = rowstart + nrow*rowstep + epsilon
    rowinds = np.arange(rowstart, rowend, dtype=dtyp)
    rowrem = rowinds % 2
    colend = colstart + ncol*colstep + epsilon
    colinds = np.arange(colstart, colend, dtype=dtyp)

    for r, rrem in zip(rowinds, rowrem):
        indices.append(list(zip(it.repeat(r), u.altrange(colstart, colend, colstep, rrem))))

    indices = np.moveaxis(np.asarray(indices, dtype=dtyp), 2, 0)

    if move_direction == 'row':
        return indices
    elif move_direction == 'col':
        return np.roll(indices, shift=1, axis=0)
