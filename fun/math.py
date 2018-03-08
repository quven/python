#!/usr/bin/env python

import math
def move(x, y, step, angle = 0):
    mx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
