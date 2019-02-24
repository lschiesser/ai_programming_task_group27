# imports
import search_algorithms as sa
"""

"""

orderPSUs = {}


# first method: receives all information from gui and begins with Preprocessing
def preprocess_info(warehouseFile,orderFile, algorithm, value_alg):
    global orderPSUs
    #control: orderFile = "C:/Users/lukas/Documents/order12.txt"
    #control: warehouseFile = "C:/Users/lukas/Documents/problem1.txt"
    #print(orderFile)
    # method that takes order file and converts it into variable
    order = orderIn(orderFile)
    # method that takes warehouse file and converts it into variable
    inventPSU = inventory(warehouseFile)
    # builds up intersection between order and list of PSUs
    fulfilledPSU = intersection(order, inventPSU)
    #control: print(fulfilledPSU)
    #grades PSU based on how many items from order are contained
    gradedPSUs = gradePSU(fulfilledPSU)
    #control: print(gradedPSUs)
    # after preprocessing pass neighborhood on to search algorithm
    orderPSUs = {}
    # first execution of search algorithm which returns index of chosen PSU
    current = executeAlgo(gradedPSUs, value_alg, algorithm)
    # method checks if search is completed (every item in order is in PSU)
    # if items are left in order, then search algorithm is executed again
    checkCompletion(current, fulfilledPSU, gradedPSUs, order, value_alg, algorithm)
    return orderPSUs

def checkCompletion(current, neighborhood, gradedN, order, value_alg, algorithm):
    """
    Input:
        current: determines current value that is returned by search algorithm
        neighborhood: list of all PSUs with their content in string form that are contained in order
        gradedN: graded PSUs
        order: order file
        value_alg: additional value for search algorithm
        algorithm: determines which algorithm is used
    Method:
        takes current value returned by search algorithm and compares content of
        found PSU and order and deletes every item from order that is contained by PSU
        found PSU is added to a dictionary: key is the PSU number (identifier) and
        the entry is the list of items that are contained in the PSU

    """
    global orderPSUs
    # Simulated Annealing, Hill CLimbing and First Choice and Random Restart Hill Climbing all return
    # only one index of one chosen PSU during one search run
    # Therefore, we only have to compare the chosen PSU with the order and not a list
    if type(current) == int:
        # newOrder has only the items that are not contained in found PSU
        # new Order is then used to rerun the search algorithm
        newOrder = [x for x in order if x not in neighborhood[current]]
        n = neighborhood.pop(current)
        # if len of found PSU (n) is not 0 then add it to the dictionary
        # key of dictionary is number (identifier) of PSU and entry is the list n
        if len(n) != 0:
            orderPSUs[current] = n
        gradedN.pop(current)
    # Local Beam Search returns a list of chosen PSUs we have to go through the list
    # to find out if there are items that are in the order, but not in the chosen PSUs
    else:
        newOrder = []
        # go through every single item in the returned list and figure out if there are
        # still items that are not in PSU and therefore still in the original order
        for item in current:
            newOrder_b = [x for x in order if x not in neighborhood[item]]
            n = neighborhood.pop(item)
            gradedN.pop(item)
            if len(n) != 0:
                orderPSUs[item] = n
        newOrder = [x for x in newOrder_b if x not in order]
    # as long as the length of newOrder is not 0 regrade PSUs, perform search algorithm again
    # and check again if search is complete
    if len(newOrder) != 0:
        newfullfilled = intersection(newOrder, neighborhood)
        newGraded = gradePSU(newfullfilled)
        newcurrent = executeAlgo(newGraded, value_alg, algorithm)
        checkCompletion(newcurrent, newfullfilled, newGraded, newOrder, value_alg, algorithm)


def executeAlgo(gradedPSUs, value_algorithm, algorithm):
    """
    Input:
        gradedPSUs: nested list of graded or regraded PSUs
        value_algorithm: additional value for certain algorithms
        algorithm: determines which algorithm is chosen
    Method:
        executes search algorithm and returns value that is returned by algorithm chosen
    """
    if algorithm == 1:
        return sa.hillclimbing(gradedPSUs)
    elif algorithm == 2:
        return sa.firstchoicehc(gradedPSUs)
    elif algorithm == 3:
        return sa.randrestart(gradedPSUs, value_algorithm)
    elif algorithm == 4:
        return sa.simaneal(gradedPSUs, value_algorithm)
    elif algorithm == 5:
        return sa.localbeam(gradedPSUs, value_algorithm)

def orderIn(orderFile):
    """
    Input:
        orderFile: path to order file
    Method:
        Reads in the order file and splits the items by whitespace to create a list
        to compare PSUs to
    """
    print(orderFile)
    with open(orderFile, 'r') as o:
        order = o.read().split(" ")
        return order



def inventory(warehouseFile):
    """
    Input:
        warehouseFile: path to warehouse file
    Method:
        Reads in warehouse files and PSU, removing the first two lines (complete
        warehouse manifest and empty line) to create a list of PSUs, represented as
        lists containing their items
    """
    available = []
    with open(warehouseFile, 'r') as v:
        for line in v:
            s = line.strip("\n").split(" ")
            available.append(s)
        available.pop(0)
        available.pop(0)
        for nestedlist in available:
            nestedlist.remove('')
        return available

def intersection(lst1, lst2):
    """
    Input:
        lst1: order (files with order items) as list
        lst2: nested list, every list in the list represents one PSU
    Method:
        compares every PSU in the nested list with every single item in the order file
        and deletes every element in the PSUs that is not in the order file
        We build up the intersection of the two different lists and return it as a list
    """
    #compares the two lists and create a new list which contains only PSU lists
    #which contain the order items
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    return lst3

def gradePSU(listPSU):
    """
    Input:
        listPSU: each nested list in this variable representes one PSU which
        contains at least one item of the order
    Method:
        grades every nested PSU list based on the number of order items
        it contains
    """
    graded = []
    for list in listPSU:
        graded.append(len(list))
    return graded
