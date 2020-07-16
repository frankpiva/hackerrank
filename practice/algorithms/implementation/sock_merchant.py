#!/bin/python3

"""
John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are
socks with colors . There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is

.

Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

    n: the number of socks in the pile
    ar: the colors of each sock

Input Format

The first line contains an integer
, the number of socks represented in .
The second line contains space-separated integers describing the colors

of the socks in the pile.

Constraints

where

Output Format

Return the total number of matching pairs of socks that John can sell.

Sample Input

9
10 20 20 10 10 30 50 10 20

Sample Output

3

Explanation

sock.png

John can match three pairs of socks.
"""

import math
import os
import random
import re
import sys

# approach: populate, iterate, and check
# memory: O(n)
# runtime: O(n)
def sockMerchant(n, ar):
    count, dictionary = 0, {}

    for sock in ar:
        if sock not in dictionary:
            dictionary[sock] = 1
        else:
            dictionary[sock] += 1

    for key in dictionary:
        count += dictionary[key] // 2

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
