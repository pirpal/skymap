#!usr/bin/python3

from constants import WIDTH, HEIGHT, CENTER_X, CENTER_Y
from re import compile, match, search
from math import cos, sin, sqrt, pi

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
    getRightAscension("16h2m54s")
    => HourAngle(16, 2, 54)
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
    http://www.geoastro.de/elevaz/basics/index.html
    """
    # TODO : add observer and time
    ra_degrees = _object._ra * 15
    x = _object._distance * cos(ra_degrees) * cos(_object._dec)
    y = _object._distance * sin(_object._dec) * cos(ra_degrees)
    z = _object._distance * sin(_object._distance)
    return (x, y, z)
    

def stereographicProjection(_object):
    """
    see http://www.astro.ro/~roaj/26_3/19-dvasilca.pdf
    r = radius
    sa = star right ascension
    sd = star declination
    ma = map projection pole right ascension
    md = map projection pole declination
    
    x = (2 * r * (cos(ma) * sin(sa) - sin(ma) * cos(sa) * cos(sd))) / (1 + (sin(ma) * sin(sa) + cos(ma) * cos(sa) * cos(sd)))
    y = (2 * r * cos(sa) * sin(sd)) / (1 + ( sin(ma) * sin(sa) + cos(ma) * cos(sa) * cos(sd)))
     
    """
    a = _object._ra * 15 # get right ascension in degrees
    d = _object._dec
    r = 1 # radius is not relevant
    x = (-2 * r * cos(a) * cos(d)) / (1 + sin(a))
    y = (2 * r * cos(a) * sin(d)) / (1 + sin(a))
    return (x, y)

def polarAzimuthalProjection(_object):
    a = _object._ra * 15
    d = _object._dec
    r = 1
    x = (-2 * r * cos(a) * cos(d)) / (1 + sin(a))
    y = (2 * r * cos(a) * sin(d)) / (1 + sin(a))
    return (x, y)

def azimuthalProjection(star):
    """
    https://www.projectpluto.com/project.htm
    """
    # Chart (canvas) center:
    ra0 = CENTER_X
    dec0 = CENTER_Y
    # object coordinates in degrees:
    ra = star._ra * 15
    dec = star._dec
    delta_ra = ra - CENTER_X
    x1 = cos(dec) * sin(delta_ra)
    y1 = sin(dec) * cos(dec0) - cos(dec) * cos(delta_ra) * sin(dec0)
    # here we could set x, y = x1, y1 for an orthographic projection

    # important : to save runtime, compute sines and cosines of ra0 and dec0
    # before plotting any star
    z1 = sin(dec) * sin(dec0) + cos(dec) * cos(dec0) * cos( delta_ra)
    # scaling factor d for sterographic projection:
    if z1 < -0.9:
        d = 20 * sqrt((1 - 0.81) / (1.00001 - z1 * z1))
    else:
        d = 2 / (z1 + 1)

    screen_height_degrees = 90
    scale = HEIGHT * (180 / pi) / screen_height_degrees
    
    x = x1 * d
    y = x1 * d

    pixel_x = CENTER_X + x * scale
    pixel_y = CENTER_Y + y * scale
    return (pixel_x, pixel_y)

def equidistantCylindrical(star):
    x = ((star._ra * 15) - CENTER_X) / sin(CENTER_Y)
    y = star._dec - CENTER_Y
    return (x, y)

# Time -------------------------------------------------------------------------
def getSideralDay(year, month, day, UT):
    """
    Works for march 1900 to february 2100
    """
    sd = 367 * y - 7 * ( + (m + 9) / 12) / 4 + 275 * m / 9 + d - 75030
    return d + UT / 24.0

def getSideralTime():
    pass
