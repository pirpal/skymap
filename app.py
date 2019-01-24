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
        #for star in cygnus._stars:
            #print(star)
            #self.draw(star)
        proxima_centauri = SkyObject({
            "star_id": 70667,
            "hip_id": 70890,
            "hd_id": "",
            "hr_id": "",
            "gliese_id": "Gl 551",
            "bay_flam_id": "Proxima Centauri",
            "proper_name": "Proxima Centauri",
            "ra": 14.49655965,
            "dec": -62.68135207,
            "distance": 1.29478331801173,
            "mag": -3775.64,
            "abs_mag": 768.16,
            "spectrum": -16,
            "color_index": 11.01,
            "x": "",
            "y": "",
            "z": "",
            "vx": "",
            "vy": "",
            "vz": "" 
        })
        print(proxima_centauri)
        self.draw(proxima_centauri)

    def initUI(self):
        self.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, POS_X, 0))
        self.title("Python Sky Map")
        self.can = tk.Canvas(
            self, width=WIDTH, height=HEIGHT, bg=COLORS["dark blue"]
        )
        self.can.grid(row=0, column=0)
        self.drawPolarGrid()


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
        print("x: {} \ny: {}\nz: {}".format(
            cartesian_coords[0],
            cartesian_coords[1],
            cartesian_coords[2]
            )
        )
        x = cartesian_coords[0] * WIDTH / 180
        y = cartesian_coords[1] * HEIGHT / 180
        print("new_x: {}\nnew_y: {}".format(x, y))
        self.can.create_oval(
            cartesian_coords[0] - 1,
            cartesian_coords[0] - 1,
            cartesian_coords[1] + 1,
            cartesian_coords[1] + 1,
            outline="white",
            fill="white",
            tag=star._star_id
        )

    def drawPolarGrid(self):
        # center (zenith)
        self.can.create_line(
            CENTER_X, CENTER_Y - 3,
            CENTER_X, CENTER_Y + 3,
            fill=COLORS["white"]
        )
        self.can.create_line(
            CENTER_X - 3, CENTER_Y,
            CENTER_X + 3, CENTER_Y,
            fill=COLORS["white"]
        )
        self.can.create_line(
            CENTER_X, 0, CENTER_X, HEIGHT,
            fill=COLORS["light blue"]
        )
        self.can.create_line(
            0, CENTER_Y, WIDTH, CENTER_Y,
            fill=COLORS["light blue"]
        )
        # create circle from 0 to 90 declination,
        # step 30 by 30
        for i in range(0, 90, 15):
            self.can.create_oval(
                CENTER_X - (HEIGHT / 180 * i),
                CENTER_Y - (HEIGHT / 180 * i),
                CENTER_X + (HEIGHT / 180 * i),
                CENTER_Y + (HEIGHT / 180 * i),
                outline=COLORS["light blue"],
                width=0.5
            )
        # add NSWE
        self.can.create_text(
            CENTER_X - CARDINAL_POINT_OFFSET,
            CARDINAL_POINT_OFFSET * 2,
            text="N", fill=COLORS["white"]
        )
        self.can.create_text(
            CENTER_X - CARDINAL_POINT_OFFSET,
            HEIGHT - CARDINAL_POINT_OFFSET * 2,
            text="S", fill=COLORS["white"]
        )
        self.can.create_text(
            CARDINAL_POINT_OFFSET,
            HEIGHT / 2 - CARDINAL_POINT_OFFSET,
            text="E", fill=COLORS["white"]
        )
        self.can.create_text(
            WIDTH - CARDINAL_POINT_OFFSET,
            HEIGHT / 2 - CARDINAL_POINT_OFFSET,
            text="W", fill=COLORS["white"]
        )
