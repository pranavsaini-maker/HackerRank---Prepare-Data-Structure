"""
PROBLEM:
• Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
• Declare an integer, last Answer, and initialize it to 0.
• There are 2 types of queries, given as an array of strings for you to parse:
1. Query: 1 x y
1. Let idx = ( (x # last Answer) % n).
2. Append the integer y to arr idx).
2. Query: 2 x y
1. Let idx = ( (x @ last Answer) % n).
2. Assign the value arr idx) ly % size(arr idx])] to last Answer.
3. Store the new value of last Answer to an answers array.
Note: ® is the bitwise XOR operation, which corresponds to the ^ operator in most
languages. Learn more about it on Wikipedia. % is the modulo operator.
Finally, size(arrlidx]) is the number of elements in arrlidx]
Function Description
Complete the dynamicArray function below.
dynamicArray has the following parameters:
- int n: the number of empty arrays to initialize in arr
- string queriesql: query strings that contain 3 space-separated integers
Returns
• intl: the results of each type 2 query in the order they are presented
Input Format
The first line contains two space-separated integers, n, the size of arr to create, and q,
the number of queries, respectively.
Each of the q subsequent lines contains a query string, queries (¿].
Constraints
• 1≤ n, q ≤ 105
• 0≤2,510%
• It is guaranteed that query type 2 will never query an empty array or index.
Sample Input
"""

#SOLUTION:
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    result = []
    
    for query in queries:
        type_of_query, x, y = query
        
        if type_of_query == 1:
            idx = (x ^ lastAnswer) % n
            arr[idx].append(y)
            
        elif(type_of_query == 2):
            idx = (x ^ lastAnswer) % n
            lastAnswer = arr[idx][y % len(arr[idx])]
            result.append(lastAnswer)
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
