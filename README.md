# AI programming task Group 27
**To execute the program run gui_qt.py**
#### General Approach
The GUI builds up the application for the users where they can use their warehouse and order files and select which search algorithms they want to run. For certain search algorithms the users can also insert non negative values.
The GUI then gives the information about chosen algorithm etc. forth to functionality.
Functionality reads the given files and preprocesses them such that we have a easy representation for our search algorithms.
Furthermore it calls the chosen search algorithm in search_algorithms and receives partial solutions as a return. It then applies a completion check to see if the order has been completely found and only ends the search if all items of the order are selected in a solution list.
This solution list is then given to GUI which produces a window with the finished list of PSU's that are needed for the order.
#### Representation of the search space
We decided to represent the search space as a nested list as follows:
1. The list represents all PSUs in the warehouse, every nested list represents one PSU and has all of its content as elements.
2. We build up the intersection between the inventory (all PSUs and their content) and the order.
Now, in the PSUs there are only elements that are also in the order.
3. Now the PSUs are graded based on how many items remain after the first processing step.
4. This list is now passed on to the next steps, the preprocessing of the warehouse description ends with this step.
#### Search Process
We decided to check after every execution of a search algorithm if the order is fulfilled by deleting every item that is in the PSU and the order and adding the PSU and its identifier to a dictionary. If the new order file is empty, then we can return the dictionary with the PSUs that fulfill the order. If not, we rerun the search algorithm until the order is fulfilled. 
#### Packages used and their version
* PyQt5-sip version: 4.19.13
* Python 3.6.5 :: Anaconda, Inc.
* math
* random
