#!usr/bin/python3

import csv
from star import *


#-------------------------------------------------------------------------------
class HygCsvReader:
    """
    Reads the HYG csv catalog
    constellations_only parameter set to true meaans that only the stars
    belonging to a constellation are considered
    (BayerFlamsteed field ! "")
    """
    def __init__(self, f, constellations_only):
        self._file = f
        self.constellations_only = constellations_only

    def toStarsDict(self):
        """
        TODO : progress bar while loading
        """
        stars = {}
        with open(self._file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["BayerFlamsteed"] != "":
                    stars[int(row["StarID"])] = SkyObject({
                        "star_id":     row["StarID"],
                        "hd_id":       row["HD"],
                        "hr_id":       row["HR"],
                        "gliese_id":   row["Gliese"],
                        "bay_flam_id": row["BayerFlamsteed"],
                        "proper_name": row["ProperName"],
                        "ra":          row["RA"],
                        "dec":         row["Dec"],
                        "distance":    row["Distance"],
                        "mag":         row["Mag"],
                        "abs_mag":     row["AbsMag"],
                        "spectrum":    row["Spectrum"],
                        "color_index": row["ColorIndex"],
                        "x":           row["X"],
                        "y":           row["Y"],
                        "z":           row["Z"],
                        "vx":          row["VX"],
                        "vy":          row["VY"],
                        "vz":          row["VZ"]
                    })
        return stars
                
                
