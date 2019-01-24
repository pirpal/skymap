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

    Returns x, y, z coordinates for display on the canvas
    see:
    http://www.geoastro.de/elevaz/basics/index.htm
    
    XY is the plane of the equator
    Z points towards the zenith
    """
    # TODO : add observer and time
    ra_degrees = _object._ra * 15
    x = _object._distance * cos(ra_degrees) * cos(_object._dec)
    y = _object._distance * sin(_object._dec) * cos(ra_degrees)
    z = _object._distance * sin(_object._distance)
    return (x, y, z)
    

def equatorialToPolarCoords(_object,_observer):
    """
    Celestial zenith is at the center of the canvas
    By default North is up
    """
    # right ascension:
    pass
    # declination:


def rightAscensionToAzimut(ra):
    pass

# Time -------------------------------------------------------------------------
def getSideralDay(year, month, day, UT):
    """
    Works for march 1900 to february 2100
    """
    sd = 367 * y - 7 * ( + (m + 9) / 12) / 4 + 275 * m / 9 + d - 75030
    return d + UT / 24.0

def getSideralTime():
    pass
