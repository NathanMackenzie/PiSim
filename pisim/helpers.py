import math
import random


def get_random():
    """
    get_random provides random float between -1 and 1

    :return: a random float between -1 and 1
    """
    return (random.randrange(0, 200)/100.0000)-1


def pythag(x, y):
    """
    pythag performs the pythagorean equation to calculate distance from the origin for a point on a 
    2D cartesian coordinate plane

    :param x: x coordinate of point
    :param y: y coordinate of point
    :return:  distance of point from the origin
    """
    return math.sqrt(x**2 + y**2)

def monte_carlo_sim(radius, inside, n):
    """
    monte_carol_sim calculates pi using the monte carlo pi simulation equation

    :param radius: radius of circle
    :param inside: number of point to land inside the circle
    :param n: total number of points during simulation
    :return: estimated value of pi
    """
    area = 4 * radius # area of square surrounding circle
    result = area * (inside/n) 
    return result 