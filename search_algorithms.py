# imports
import random


def simaneal(neighborhood, t):
    print("sa")
    current = random.randint(0, len(neighborhood) - 1)
    print(current)
    while t >= 0:
        if t == 0:
            return current
            print(neighborhood[current])
        next = random.randint(0, len(neighborhood) - 1)
        print(next)
        delta = neighborhood[next] - neighborhood[current]
        print(delta)
        if delta > 0:
            current = next
        elif delta/t >= 0.6:
            current = next
        t = t - 1
