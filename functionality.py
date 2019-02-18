# imports

"""
1. Definition of universe --> variable list consisting of items in the order list


"""

# first method: receives all information from gui and begins with Preprocessing
def preprocess_info(warehouseFile,orderFile, algorithm, value_alg):

    orderFile = "C:/Users/lukas/Documents/order12.txt"
    warehouseFile = "C:/Users/lukas/Documents/problem1.txt"
    #print(orderFile)
    # method that takes order file and converts it into variable
    order = orderIn(orderFile)
    # method that takes warehouse file and converts it into variable
    inventPSU = inventory(warehouseFile)
    fulfilledPSU = intersection(order, inventPSU)
    print(fulfilledPSU)
    gradedPSUs = gradePSU(fulfilledPSU)
    print(gradedPSUs)
    # preprocess information
    # after preprocessing pass neighborhood on to search algorithm
    if algorithm == 1:
        print(a)
    elif algorithm == 2:
        print(b)
    elif algorithm == 3:
        print(c)
    elif algorithm == 4:
        print(d)
    elif algorithm == 5:
        print(e)

    return

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
        #print(order)
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

preprocess_info("","",0,1)
