#!usr/bin/python3

class Observer:
    """
    An observer is located at the centre of his celestial
    sphere with +z above his head and the NESW.
    
    Any sky object can be identified by its two coordinates
    altitude and azimut.

    Altitude h is the angular distance above the horizon (0 < h < 90°)
    
    Azimut alpha is the angular distance measured along the horizon,
    westwards from the south point S (in astronomy) or eastwards
    from the north point N in nautics (0 < alpha < 360°)
    """
    def __init__(self, data):
        self._name      = data["name"]
        self._latitude  = data["latitude"]
        self._longitude = data["longitude"]
        self._altitude  = data["altitude"]
        self._time      = data["time"]


