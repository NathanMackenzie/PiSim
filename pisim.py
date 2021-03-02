# pisim.py
__version__ = '0.1.0'

import math
import random

radius = 1
in_count = 0
n = 0

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

# Perform monte carlo simulation
for i in range(1000000):
    n = i # number of iterations

    # get random point coordinates
    x = get_random()
    y = get_random()

    # calculate points distances from origin
    dist = pythag(x, y)

    # check if point is witin the circle
    if dist <= 1:
        in_count += 1


# Print results
print("The estimated value of pi is...")
print(monte_carlo_sim(1, in_count, n))


