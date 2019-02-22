# imports
import random
import math

def simaneal(neighborhood, t):
    """
    Input:
        neighborhood: graded PSUs
        t: temperature from user input (getValue)
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

    #algorithm for hill climbing search, takes gradedPSUs
    neighbor = 0
     #defines current selected neighbor
    current = random.randint(0, len(gradedPSUs) - 1)
    if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
        neighbor = current + 1
    else:
        neighbor = current - 1
        """
            compares selected neighbor and next indexed neighbors to either side;
            whichever next indexed neighbor's value is greater than the other neighbor
            (optimizes the solution) is selected as new neighbor
        """
    while gradedPSUs[current] < gradedPSUs[neighbor]:
        current = neighbor
        if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
            neighbor = current + 1
        else:
            neighbor = current - 1
            #continues until neighbor values are no longer greater than current
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
            #chooses new current based on which neighbor first improves the maximazation function
            #until function can no longer be improved (neighbors are no longer larger)
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



def randrestart(gradedPSUs,n):
#algorithm for random restart search, takes graded PSUs and user input from getValue

    results = [] #collects maximization neighbor for each run of hill climbing

    #defines the last (largest) neighbor index from PSUs after performing n hill climbs

    for _ in range(n):
    #runs a hill climbing search n times, according to user input

      current = random.randint(0, len(gradedPSUs) - 1)
      if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
          neighbor = current + 1
      else:
          neighbor = current - 1
      #defines indices of current and neighbor values in PSUs list

      while gradedPSUs[current] < gradedPSUs[neighbor]:
          current = neighbor
          if gradedPSUs[current + 1] > gradedPSUs[current - 1]:
              neighbor = current + 1
          else:
              neighbor = current - 1
      results.append(current)
      #compares neighbors until a better (larger) neighbor can't be found, and
      #returns the largest neighbor to the results list
      n_best = sorted(results) #sorts results list numerically
      best = n_best[len(n_best)-1]
      return best
