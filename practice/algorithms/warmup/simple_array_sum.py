#!/bin/python3

"""
Given an array of integers, find the sum of its elements.

For example, if the array
, , so return

.

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

    ar: an array of integers

Input Format

The first line contains an integer,
, denoting the size of the array.
The second line contains

space-separated integers representing the array's elements.

Constraints

Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11

Sample Output

31

Explanation

We print the sum of the array's elements:
.
"""

import os
import sys

# approach: pythonic iterate and calculate
def simpleArraySum(ar):
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
