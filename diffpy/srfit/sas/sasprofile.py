#!/usr/bin/env python
########################################################################
#
# diffpy.srfit      by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2008 Trustees of the Columbia University
#                   in the City of New York.  All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
########################################################################
"""Class for adapting a sans DataInfo objects to the Profile interface.

"""

from numpy import ones_like

from diffpy.srfit.fitbase.profile import Profile
from diffpy.srfit.util import public

@public
class SASProfile(Profile):
    """Observed and calculated profile container for SAS data.

    This wraps a sans DataInfo object as a Profile object. Use this when you
    want to use and manipulate a DataProfile before using it with SrFit.
    Otherwise, use the SASParser class and load the data into a base Profile
    object.

    Attributes

    xobs    --  A numpy array of the observed independent variable (default
                None)
    yobs    --  A numpy array of the observed signal (default None)
    dyobs   --  A numpy array of the uncertainty of the observed signal (default
                None, optional).
    x       --  A numpy array of the calculated independent variable (default
                None, property for xpar accessors).
    y       --  The profile over the calculation range (default None, property
                for ypar accessors).
    dy      --  The uncertainty in the profile over the calculation range
                (default None, property for dypar accessors).
    ycalc   --  A numpy array of the calculated signal (default None).
    xpar    --  A ProfileParameter that stores x (named "x").
    ypar    --  A ProfileParameter that stores y (named "y").
    dypar   --  A ProfileParameter that stores dy (named "dy").
    meta    --  A dictionary of metadata. This is only set if provided by a
                parser.

    _datainfo   --  The DataInfo object this wraps.

    """

    def __init__(self, datainfo):
        """Initialize the attributes.
        
        datainfo   --  The DataInfo object this wraps.
        
        """
        self._datainfo = datainfo
        Profile.__init__(self)

        self.xobs = self._datainfo.x
        self.yobs = self._datainfo.y
        self.dyobs = self._datainfo.dy or ones_like(self.xobs)
        return

__id__ = "$Id$"