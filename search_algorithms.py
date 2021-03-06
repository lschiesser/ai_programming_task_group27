# imports
import random
import math
"""
Group 27
Members: Ieshia Hickey-Williams, Sarah Jähnichen, Berit Reise, Lukas Schießer
"""

def simaneal(gradedPSUs, t):
    """
    Input:
        gradedPSUs: graded PSUs
        t: temperature from user input (getValue)
    Method:
        performs simulated annealing
    """
    #choose a random current
    current = random.randint(1, len(gradedPSUs) - 2)
    # while temperatur t bigger or equal 0 perform search
    while t >= 0:
        # if t equals 0 then return index of PSU currently chosen
        if t == 0:
            return current
        # choose a random neighbor of current
        next = random.randint(1, len(gradedPSUs) - 2)
        # calculate difference between the current PSU and the chosen neighbor
        delta = gradedPSUs[next] - gradedPSUs[current]
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
    """
    Input:
        graded PSUs as state space
    Method:
        performs hillclimbing
    """
    # choose random PSU as start spate = current
    neighbor = 0
    current = random.randint(1, len(gradedPSUs) - 2)
    # compare PSU's on either side of current to evaluate which one has more order items/ is the better choice to optimize the solution
    # define better choice as neighbor of current
    if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
        neighbor = current + 1
    else:
        neighbor = current - 1
    # as long as the neighbor is a better solution than the current, the neighbor becomes the new current
    while gradedPSUs[current] < gradedPSUs[neighbor]:
        current = neighbor
        # evaluate new neighbor
        if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
            neighbor = current + 1
        else:
            neighbor = current - 1
    # return current that is locally optimal (no higher neighbor found) to functionality as part of the end solution
    return current


def firstchoicehc(gradedPSUs):
    """
    Input:
        graded PSUs as state space
    Method:
        performs first choice hillclimbing
    """
    # same as hillclimbing
    neighbor = 0
    current = random.randint(1, len(gradedPSUs) - 2)
    if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
        neighbor = current + 1
    else:
        neighbor = current - 1
    # as long as the neighbor is a better choice/has more order items than the current
    while gradedPSUs[current] < gradedPSUs[neighbor]:
        # chooses new current based on which neighbor first improves the maximazation function (has more order items)
        if gradedPSUs[current + 1] > gradedPSUs[current]:
            current = current + 1
        elif gradedPSUs[current - 1] > gradedPSUs[current]:
            current = current - 1
    return current


def localbeam(graded, k):
    """
    Input:
        graded = graded PSU's
        k = number of states that are selected (User Input)
    Method:
        performs local beam search
    """
    # create list of graded PSU's stored together with their original index
    graded_OI = []
    x = 0
    for sublist in graded:
        graded_OI.append([[sublist], x])
        x = x + 1
    # create a ordered list of the graded PSU's with their original index such that they are in reversed order (lowest biggest to lowest)
    ordered = sorted(graded_OI, reverse=True)
    # copy the first k PSUs (with their graded number and original index) from ordered into k_best
    # since those PSU's have the highest number of ordered items stored in them
    k_best = ordered[:k]
    returnlist = []
    # for every PSU list in k_best only append the corresponding index to the returnlist
    for subl in k_best:
        _, seq = subl
        returnlist.append(seq)
    # return the list with the indices of the k best PSU's to functionality as the solution
    return returnlist



def randrestart(gradedPSUs,n):
    """
    Input:
        graded PSU's
        n = (User Input from getValue)
    Method:
        performs random restart hillclimbing
    """
    # collects maximization neighbor for each run of hill climbing
    results = []
    # create list of graded PSU's stored together with their original index
    graded_OI = []
    x = 0
    for sublist in gradedPSUs:
        graded_OI.append([[sublist], x])
        x = x + 1
    # runs a hill climbing search n times, according to user input
    for _ in range(n):
      # same as hillclimbing
      current = random.randint(1, len(gradedPSUs) - 2)
      if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
          neighbor = current + 1
      else:
          neighbor = current - 1

      # compares neighbors until a better (larger) neighbor can't be found
      while gradedPSUs[current] < gradedPSUs[neighbor]:
          current = neighbor
          if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
              neighbor = current + 1
          else:
              neighbor = current - 1
      # if the currently largest PSU is found, we put it's graded number and index (= current) to the results list
      results.append(graded_OI[current])

    # sorts results list with n best PSU's numerically
    n_best = sorted(results)
    # return only the index of the last PSU in the sorted result list to functionality as a partial solution
    _, best = n_best[len(n_best)-1]
    return best
