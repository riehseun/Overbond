# Overbond

Solution to Maximum Clique problem with Python

1. The algorithm first pick a node from the input file that has most edges.
2. The node with most edges is excluded from the set of input.
3. Find intersection between Step2, AND with set of nodes connected to Step1.
4. Steps 1 to 3 is called recursively with set from Step3 as input.
5. In the 2nd recursive call we are picking the minimum node from the resulting set.
6. Stop recursion when no elements are left in the set.
