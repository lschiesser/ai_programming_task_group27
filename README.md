# AI programming task Group 27
#### Representation of the search space
We decided to represent the search space as a nested list as follows:
1. Build up the intersection between the inventory (all PSUs and their content) and the order.
In the PSUs now there are only elements that are also in the order.
2. Now the PSUs are graded based on how many items remain after the first processing step.
3. This list is now passed on to the next video.
