# imports

"""
1. Definition of universe --> variable order tuple consisting of every single order items


"""

# first method: receives all information from gui and begins with Preprocessing
def preprocess_info(warehouseFile,orderFile, algorithm, value_alg):
    # method that takes warehouse file and converts it into variable
    orderFile = "C:/Users/lukas/Documents/order11.txt"
    warehouseFile = "C:/Users/lukas/Documents/problem1.txt"
    print(orderFile)
    orderIn(orderFile)
    inventory(warehouseFile)
    # method that takes order file and converts it into variable

    # preprocess information
    # after preprocessing pass neighborhood on to search algorithm
    #if (algorithm == 1):
        #hill Climbing
    #elif algorithm == 2:
        #first choice hill Climbing
    #elif algorithm == 3:
        #parallel hill Climbing
    #elif algorithm == 4:
        #simulated Annealing
    #elif algorithm == 5:
        #local beam search

    return

def orderIn(orderFile):
    print(orderFile)
    with open(orderFile, 'r') as o:
        order = o.read().split(" ")
        print(order)
        return order



def inventory(warehouseFile):
    available = []
    with open(warehouseFile, 'r') as v:
        for line in v:
            s = line.strip("\n").split(" ")
            available.append(s)
        print(available)
        return available


preprocess_info("","",0,1)
