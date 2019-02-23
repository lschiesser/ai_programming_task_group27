# AI programming task Group 27
#### General Approach
The GUI builds up the application for the users where they can use their warehouse and order files and select which search algorithms they want to run. For certain search algorithms the users can also insert non negative values.
The GUI then gives the information about chosen algorithm etc. forth to functionality.
Functionality reads the given files and preprocesses them such that we have a easy representation for our search algorithms.
Furthermore it calls (?) the chosen search algorithm in search_algorithms and receives partial solutions as a return. It then applies a completion check to see if the order has been completely found and only ends the search if all items of the order are selected in a solution list.
This solution list is then given to GUI which produces a window with the finished list of PSU's that are needed for the order.
#### Representation of the search space
We decided to represent the search space as a nested list as follows:
1. Build up the intersection between the inventory (all PSUs and their content) and the order.
In the PSUs now there are only elements that are also in the order.
2. Now the PSUs are graded based on how many items remain after the first processing step.
3. This list is now passed on to the next video.
