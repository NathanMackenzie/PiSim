# pisim.py
__version__ = '0.1.0'

import math
import random
import helpers as hp

radius = 1
in_count = 0
n = 0

# Perform monte carlo simulation
for i in range(1000000):
    n = i # number of iterations

    # get random point coordinates
    x = hp.get_random()
    y = hp.get_random()

    # calculate points distances from origin
    dist = hp.pythag(x, y)

    # check if point is witin the circle
    if dist <= 1:
        in_count += 1


# Print results
print("The estimated value of pi is...")
print(hp.monte_carlo_sim(1, in_count, n))


