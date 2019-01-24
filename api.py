#!usr/bin/python3


from re import compile, match, search
from math import cos, sin

"""
Skymap API
Astronomical functions and utils
"""

# Distances conversions --------------------------------------------------------
def parsecToLightYear(p):
    return p * 3.262

def lightYearToParsec(ly):
    return ly * 0.3066


# Parsing ----------------------------------------------------------------------

def getRightAscension(_str):
    """
    Returns HourAngle instance
    NOTE : not needed for HYG as RA eand DEC are given in degrees
    """
    regex = compile("[\+\-](\d+.\d+)h(\d+.\d+)m(\d)+s" )
    match = search(regex, _str)
    h, m, s = match.group(1), match.group(2), match.group(3)

    return HourAngle(h, m, s)

def getDeclination(_str):
    return float(_str)

# Translations -----------------------------------------------------------------
def equatorialToCartesianCoords(_object, _observer):
    """
    Object is given with its right ascension and declination for epoch j2000.
    Observer is given with its latitude, longitude and time parameters.

    Returns 2d (x, y) coordinates for display onthe canvas
    see:
    http://www.geoastro.de/elevaz/basics/index.htm
    
    
    """
    # TODO : add observer and time
    x = cos(_object._ra) * cos(_object._dec)
    y = sin(_object._dec) * cos(_object._ra)
    return (x, y)
    
