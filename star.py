#!usr/bin/python3

from api import *

#-------------------------------------------------------------------------------        
class SkyObject:
    """
    A SkyObject is initialized with a HygCatalogEntry, see db_reader.py
    RA and DEC are given in degrees
    Distance is given in parsecs
    """
    def __init__(self, data = {}):
        self._star_id     = int(data["star_id"])
        self._draper_id   = int(data["hd_id"]) if data["hd_id"] != "" else 0
        self._harvard_id  = int(data["hr_id"]) if data["hr_id"] != "" else 0
        self._gliese_id   = data["gliese_id"]
        self._bay_flam_id = data["bay_flam_id"]
        self._ra          = float(data["ra"]) if data["ra"] != "" else 0
        self._dec         = float(data["dec"]) if data["dec"] != "" else 0
        self._proper_name = data["proper_name"]
        self._distance    = float(data["distance"]) if data["distance"] != "" else 0
        self._mag         = float(data["mag"]) if data["mag"] != "" else 0
        self._abs_mag     = float(data["abs_mag"]) if data["abs_mag"] != "" else 0
        self._spectrum    = data["spectrum"]
        self._color_id    = float(data["color_index"]) if data["color_index"] != "" else 0
        self._x           = float(data["x"]) if data["x"] != "" else 0
        self._y           = float(data["y"]) if data["y"] != "" else 0
        self._z           = float(data["z"]) if data["z"] != "" else 0
        self._vx          = float(data["vx"]) if data["vx"] != "" else 0
        self._vy          = float(data["vy"]) if data["vy"] != "" else 0
        self._vz          = float(data["vz"]) if data["vz"] != "" else 0
                                               
    def distanceToLy(self):
        return parsecToLightYear(self._distance)

    def __str__(self):
        return "{}\nRA:  {}\nDEC: {}\n{} pc ({} ly)".format(
            self._bay_flam_id,
            round(self._ra, 3),
            round(self._dec, 3),
            round(self._distance, 2),
            round(self.distanceToLy(), 2)

        )


#-------------------------------------------------------------------------------
class Constellation:
    """
    Collection of SkyObject instances
    """
    def __init__(self, name, stars=[]):
        self._name = name
        self._stars = stars

    def __str__(self):
        print("{}".format(self._name))
        print("---------------------")
        for star in self._stars:
            print("\n")
            print(star)
        return ""
