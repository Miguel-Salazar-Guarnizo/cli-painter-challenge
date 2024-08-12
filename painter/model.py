# TODO: Add code here

import math

import matplotlib.pyplot as plt

class Point:

    def __init__(self, x: float, y:flot):
        self.x: float =x
        self.y: float =y

class Circle:

    def __init__(self, center: Point, radius:float):
        self.radius: float = radius
        self.center: Point=center

    def area_circle(self)->float:
        Area= math.pi*(self.radius)**2
        return Area
    def Draw(self):
        circle= plt.Circle ((self.center.x, self.center.y), self.radius, color="r")
