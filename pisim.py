# pisim.py
__version__ = '0.1.0'

import math
import random

radius = 1

origin_x = 0
origin_y = 0

in_count = 0
out_count = 0



for i in range(1000000):
    x = (random.randint(0, 199)/100.0000)-1
    y = (random.randint(0, 199)/100.0000)-1

    dist = math.sqrt(x**2 + y**2)

    if dist <= 1:
        in_count += 1
    else:
        out_count += 1

print("The estimated value of pi is...")

print(4*(in_count/(out_count + in_count)))


