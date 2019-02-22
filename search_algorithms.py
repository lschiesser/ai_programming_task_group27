# imports
import random
import math

def simaneal(neighborhood, t):
    current = random.randint(0, len(neighborhood) - 1)
    while t >= 0:
        if t == 0:
            return current
            print(neighborhood[current])
        next = random.randint(0, len(neighborhood) - 1)
        delta = neighborhood[next] - neighborhood[current]
        if delta > 0:
            current = next
        elif math.exp(delta)/t >= random.randrange(0, 1):
            current = next
        t = t - 1
