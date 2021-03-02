import math
import random

# get_random() provides random float between -1 and 1
#
# @return float between -1 and 1
def get_random():
    return (random.randrange(0, 200)/100.0000)-1

# pythag(x, y) performs the pythagorean equation to calculate distance from 
# origin on a cartesian coordinate plane
#
# @param x contains the x coordinate
# @param y contains the y coordinate
# @return distance of point from origin 
def pythag(x, y):
    return math.sqrt(x**2 + y**2)

# monte_carlo_sim(radius, instide, n) performs the monte carlo pi simulation equation
#
# @param radius contains the radius of the circle
# @param inside is the number of points found to land inside the circle
# @param n is the total number of simulation iterations
# @return results containing the estimated calculation of pi
def monte_carlo_sim(radius, inside, n):
    area = 4 * radius # area of square surrounding circle
    result = area * (inside/n) 
    return result 