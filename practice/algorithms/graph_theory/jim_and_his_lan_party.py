#!/bin/python3
 
"""
During the Steam Summer Sale, Jim's friends have purchased games, which are numbered from to

. The games are multiplayer. Jim has invited his friends to his basement where they will play by making a LAN-Party.

Each friend has already decided the game he would like to play for the rest of the day. So there will be a group of friends who will play the same game together.

But then, they face a problem: Currently, none of the friends' PCs are connected. So they have to be connected using the available
wires. Jim decides to connect friends and with the

th wire one by one. So he starts with wire 1, then with wire 2 and so on.

A group can start playing their game, only if all the members are connected (if not directly, then there must exist a path connecting them). They want to start playing as soon as possible.

For each game, find out the wire after adding which the group can start playing. It is also possible that a group will never get connected. In such a case, this group starts crying and you should display -1.

Input Format

On the first line there will be
, and each separated by a single space. On the second line we will give you integers separated by a single space: The -th integer denotes the game friend wants to play (all between and ). The next lines will denote wires: ith line denotes ith wire and is denoted by and

pairs each separated by a single space.

Constraints

For each game , the number of players playing will be positive.

Note Each game is chosen by at least one player. If a group consists of only one member, then print 0, since this lucky (?) lone player can start right away!

Output Format

Print on the
th line the answer for the

th game.

Sample Input

5 2 4
1 2 2 2 1
1 2 
2 3
1 5
4 5 

Sample Output

3
4

Explanation

The group with the game 1 can play after the 3rd wire is added. The group with game 2 can play only after the 4th wire has been added because after adding the 4th wire, a path between (2,3) (3,4) and (2,4) gets created.
"""

import os
import sys

# approach: iterative clusterfuck
# memory: O(n^n)
# runtime: O(n^n)
def lanParty(games, wires, m):
    connected = [True]
    who = []
    minimums = []
    print('minimums', minimums)

    for i in range(0, m+1):
        who.append([])
        minimums.append(len(wires)+1)
    for j in range(0, len(games)):
        connected.append(False)
        who[games[j]].append(j+1)
    print('connected', connected)
    print('who', who)
    for k in range(0, len(wires)):
        print('wires[k][x]', wires[k][0], wires[k][1])
        connected[wires[k][0]] = True
        connected[wires[k][1]] = True
        print('connected', connected)
        for l in range(0, len(who)):
            allConnected = True
            for player in who[l]:
                if connected[player] == False:
                    allConnected = False
            if allConnected:
                if k + 1 < minimums[l]:
                    minimums[l] = k + 1
    print('minimums', minimums)
    formatted = minimums[1:]
    newFormatted = []
    print('formatted', formatted)
    for z in range(0, len(formatted)):
        print(formatted[z], len(wires) + 1)
        if formatted[z] == len(wires) + 1:
            print('made it here')
            formatted[z] = -1
            print(formatted)
            newFormatted.append(-1)
        else:
            newFormatted.append(formatted[z])
    return newFormatted


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nmq = input().split()

    n = int(nmq[0])

    m = int(nmq[1])

    q = int(nmq[2])

    games = list(map(int, input().rstrip().split()))

    wires = []

    for _ in range(q):
        wires.append(list(map(int, input().rstrip().split())))

    print(games, wires, m)
    result = lanParty(games, wires, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
