# triangle-problem
triangle problem

Assumptions:
Triangle text file format is correct.
Text file can be expressed as a tree data structure.
Moving to adjacent numbers on the next row means new index equals last index + or - 1.
Output only the max sum.
Numbers are integers

Approach:
Use level order traversal (breadth first search) to traverse the triangle.
Read the txt file lines and use indexes to assume an implicit tree structure.
Keep track of sums and take the max sum at the end of the traversal.

Examples:
   5 
  9 6 
 4 6 8 
0 7 1 5
max = 27

    0 
   0 1 
  0 3 2 
 9 4 1 3
 max = 9