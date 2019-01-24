#!usr/bin/python3

# see https://en.wikipedia.org/wiki/Right_ascension

class HourAngle:
    def __init__(self, hours, minutes, seconds):
        self.hours   = hours
        self.minutes = minutes
        self.second  = second

    def __str__(self):
        return "{}h{}m{}s".format(self.hours, self.minutes, self.seconds)


