"""
PROBLEM:
Given a 6x6 2D Array, arr: 

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
An hourglass in A  is a subset of values with indices falling in this pattern in arr's graphical representation: 

a b c
  d
e f g
There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in arr , then print the maximum hourglass sum. The array will always be 6x6. 

Example
arr=



-9 -9 -9  1 1 1 
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The 16 hourglass sums are: 

-63, -34, -9, 12, 
-10,   0, 28, 23, 
-27, -11, -2, 10, 
  9,  17, 25, 18
The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2: 

0 4 3
  1
8 6 6
"""
#SOLUTION:

#!/bin/python3

import math
import os
import random
import re
import sys


def hourglassSum(arr):
    # Write your code here
    max_sum = -float('inf')
    for i in range(4):
        for j in range (4):
            
            hourGlass = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2]
                +arr[i+1][j+1]+
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            
            max_sum = max(max_sum, hourGlass)
    return max_sum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
