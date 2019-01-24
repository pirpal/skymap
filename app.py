#!usr/bin/python3

import tkinter as tk
from constants import *
from db_reader import HygCsvReader
from api import *
from star import *

class App(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.reader = HygCsvReader(DB_PATH, constellations_only=True)
        self.observer = None
        self.stars = self.reader.toStarsDict()
        # DEBUG
        #print(self.stars[119434])
        # TODO: give access to observer modifications in space and time
        # DEBUG
        cygnus = self.initConstellationFromName("Cyg")
        #print(cygnus)
        for star in cygnus._stars:
            print(star)
            self.draw(star)

    def initUI(self):
        self.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, POS_X, 0))
        self.title("Python Sky Map")
        self.can = tk.Canvas(
            self, width=WIDTH, height=HEIGHT, bg=COLORS["dark blue"]
        )
        self.can.grid(row=0, column=0)

    def initConstellationFromName(self, name):
        """
        Builds a constellation with a prefix, for instance:
        cygnus = initConstellationFromName("Cyg")
        """
        stars = []
        for k, star in self.stars.items():
            if star._bay_flam_id.endswith(name):
                stars.append(self.stars[k])
        return Constellation(name, stars)
                
    
    def draw(self, star):
        cartesian_coords = equatorialToCartesianCoords(star, self.observer)
        # DEBUG
        print("x: {} \ny: {}".format(
            cartesian_coords[0],
            cartesian_coords[1])
        )
        self.can.create_oval(
            cartesian_coords[0] - 1,
            cartesian_coords[0] - 1,
            cartesian_coords[1] + 1,
            cartesian_coords[1] + 1,
            outline="white",
            fill="white",
            tag=star._star_id
        )
