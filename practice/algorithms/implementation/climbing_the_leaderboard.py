#!/bin/python3

"""
Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking. The game uses Dense Ranking, so its leaderboard works like this:

    The player with the highest score is ranked number 

    on the leaderboard.
    Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.

For example, the four players on the leaderboard have high scores of
, , , and . Those players will have ranks , , , and , respectively. If Alice's scores are , and , her rankings after each game are , and

.

Function Description

Complete the climbingLeaderboard function in the editor below. It should return an integer array where each element
represents Alice's rank after the

game.

climbingLeaderboard has the following parameter(s):

    scores: an array of integers that represent leaderboard scores
    alice: an array of integers that represent Alice's scores

Input Format

The first line contains an integer
, the number of players on the leaderboard.
The next line contains space-separated integers , the leaderboard scores in decreasing order.
The next line contains an integer, , denoting the number games Alice plays.
The last line contains space-separated integers

, the game scores.

Constraints

for for The existing leaderboard,
, is in descending order.
Alice's scores,

    , are in ascending order.

Subtask

For

of the maximum score:

Output Format

Print
integers. The integer should indicate Alice's rank after playing the

game.

Sample Input 1
CopyDownload




Array: scores




100


100


50


40


40


20


10



 






Array: alice




5


25


50


120



 

7
100 100 50 40 40 20 10
4
5 25 50 120

Sample Output 1

6
4
2
1

Explanation 1

Alice starts playing with

players already on the leaderboard, which looks like this:

image

After Alice finishes game
, her score is and her ranking is

:

image

After Alice finishes game
, her score is and her ranking is

:

image

After Alice finishes game
, her score is and her ranking is tied with Caroline at

:

image

After Alice finishes game
, her score is and her ranking is

:

image

Sample Input 2
CopyDownload




Array: scores




100


90


90


80


75


60



 






Array: alice




50


65


77


90


102



 

6
100 90 90 80 75 60
5
50 65 77 90 102

Sample Output 2

6
5
4
2
1
"""

import math
import os
import random
import re
import sys

# approach: dynamic programming using a lookup table
# memory: O(n)
# runtime: O(2n)
def climbingLeaderboard(scores, alice):
    alicesRanks = []

    # special case: empty leaderboard or alice is an ace
    if len(scores) == 0 or alice[0] >= scores[0]:
        for score in alice:
            alicesRanks.append(1)
        return alicesRanks
    
    # initialize lookup table
    lookupTable = {}
    rank = 1
    lookupTable[rank] = scores[0]
    for index, score in enumerate(scores[1:]):
        lastScore = scores[index]
        if lastScore > score:
            rank += 1
            lookupTable[rank] = score
    
    # iterate through looup table from the bottom up
    lastRank = len(lookupTable)
    for index, score in enumerate(alice):
        # quick check for a bad score
        if score < scores[-1]:
            alicesRanks.append(lastRank + 1)
        else:
            while lastRank != 0 and score > lookupTable[lastRank]:
                lastRank -= 1
            if lastRank == 0 or lookupTable[lastRank] > score:
                alicesRanks.append(lastRank + 1)
            else:
                alicesRanks.append(lastRank)
    
    return alicesRanks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
