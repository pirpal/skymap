#!usr/bin/python3

# GUI --------------------------------------------------------------------------
WIDTH        = 800
HEIGHT       = 700
POS_X        = 200
CENTER_X     = WIDTH / 2
CENTER_Y     = HEIGHT / 2
ASPECT_RATIO = WIDTH / HEIGHT
COLORS = {
    "light blue": "#0f153d",
    "dark blue":  "#03040c",
    "white":      "#ffffff"
}

# DISPLAY SETTINGs -------------------------------------------------------------
MIN_MAGNITUDE = 2.0
CARDINAL_POINT_OFFSET = 8

# DB ---------------------------------------------------------------------------
DB_PATH = "db/hygxyz.csv"

# PHYSICS ----------------------------------------------------------------------
LIGHT_YEAR = 9.4607e15        # meters
PARSEC     = 3.0857e16        # meters
AU         = 1.49597870700e12 # meters 
