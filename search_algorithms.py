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

def hillclimbing(gradedPSUs):
    neighbor = 0
    current = random.randint(0, len(gradedPSUs) - 1)
    if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
        neighbor = current + 1
    else:
        neighbor = current - 1

    while gradedPSUs[current] < gradedPSUs[neighbor]:
        current = neighbor
        if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
            neighbor = current + 1
        else:
            neighbor = current - 1
    return current


def firstchoicehc(gradedPSUs):
    neighbor = 0
    current = random.randint(0, len(gradedPSUs) - 1)
    if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
        neighbor = current + 1
    else:
        neighbor = current - 1

    while gradedPSUs[current] < gradedPSUs[neighbor]:
        if gradedPSUs[current + 1] > gradedPSUs[current]:
            current = current + 1
        elif gradedPSUs[current - 1] > gradedPSUs[current]:
            current = current - 1
    return current
