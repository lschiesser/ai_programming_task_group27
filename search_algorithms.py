# imports
import random
import math

def simaneal(neighborhood, t):
    """
    Input:
        neighborhood: graded PSUs
        t: temperature
    Method:
        performs simulated annealing
    """
    #choose a random current
    current = random.randint(0, len(neighborhood) - 1)
    # while temperatur t bigger or equal 0 perform search
    while t >= 0:
        # if t equals 0 then return index of PSU currently chosen
        if t == 0:
            return current
        # choose a random neighbor of current
        next = random.randint(0, len(neighborhood) - 1)
        # calculate difference between the current PSU and the chosen neighbor
        delta = neighborhood[next] - neighborhood[current]
        # if difference is bigger than 0, then the chosen neighbor is the new current
        # PSU chosen
        if delta > 0:
            current = next
        # if the exponential of delta/t is bigger than a random probabaility,
        # then the new current PSU is the neighbor
        elif math.exp(delta/t) >= random.randrange(0, 1):
            current = next
        # lower temperature linearly
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

def localbeam(graded, k):
    graded_OI = []
    x = 0
    for sublist in graded:
        graded_OI.append([[sublist], x])
        x = x + 1
    ordered = sorted(graded_OI, reverse=True)
    k_best = ordered[:k]
    returnlist = []
    for subl in k_best:
        _, seq = subl
        returnlist.append(seq)
    print("a")
    return returnlist
