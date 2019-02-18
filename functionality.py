# imports

"""
1. Definition of universe --> variable order tuple consisting of every single order items


"""

# first method: receives all information from gui and begins with Preprocessing
def preprocess_info(warehousepath, orderpath, algorithm, value_alg):
    # method that takes warehouse file and converts it into variable

    # method that takes order file and converts it into variable
    order = orderIn(orderpath)
    # preprocess information
    # after preprocessing pass neighborhood on to search algorithm
    if algorithm == 1:
        #hill Climbing
    elif algorithm == 2:
        #first choice hill Climbing
    elif algorithm == 3:
        #parallel hill Climbing
    elif algorithm == 4:
        #simulated Annealing
    elif algorithm == 5:
        #local beam search

    return

def orderIn(orderpath):
    with open(orderpath, 'r') as o:
        order = o.split(" ")
        return order


def inventory(warehousepath):
    with open(warehousepath, 'r') as v:
        for i, line in v:
            if i>1:
                available =
