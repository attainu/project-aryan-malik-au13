The Maze Solver
It is a python program to solve a matrix with 0s and 1s as elements.A Maze is given as row*column binary matrix of blocks where starting point is the upper left most block i.e., maze[0][0] and ending point is lower rightmost block i.e., maze[row-1][column-1].A person starts from starting point and has to reach the ending point. The person can move in all directions.In the maze matrix, 0 means the block is a dead end and 1 means the block can be used in the path from source to destination.

I have used Backtracking to solve this problem in which i created another matrix named sol which have the same dimension as the input matrix. In my code i have used two pointers as row_pointer and column_pointer.These two pointer are used to move the person to all four directions.If there is decrease in row_pointer it moves the person in upward direction significantly increasing the row_pointer moves the person in downward direction and increase in column_pointer moves the person in right direction significantly decreasing the column_pointer moves the person in left direction. I have created a function named isSafe which check whether it is safe for the person to move on the specified location or not and then have created another function named delwrongpath which replace the old path of 1s with 0s back to it's original self.In the end there is another file print.py which contains function that prints the solved matrix.

Colouring the Matrix:-
I have introduced different colors for obstacles and path to make it easy for users to identify the possible path.The color for 0s is green and for 1s it is yellow.different color makes matrix more visualy appealing.
I have also wrote two different types of comment -one for describing the function and the other one for describing the specific functionality of the line under. 
It takes input from inputfile by the help fileinput module that i have used in MazeSolver.py .

Some Sample Code
Input file contains data like this:

1 0 1 1 1 1 0 1
1 0 1 0 0 1 0 1
1 1 1 0 0 1 0 1
0 0 0 1 1 1 0 1
1 1 1 1 0 0 0 1 
0 0 0 1 1 1 1 1 

Output should contains data like this:
1 0 1 1 1 1 0 0 
1 0 1 0 0 1 0 0
1 1 1 0 0 1 0 0
0 0 0 1 1 1 0 0
0 0 0 1 0 0 0 0
0 0 0 1 1 1 1 1
