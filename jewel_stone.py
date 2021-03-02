# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(J, S):
    total = 0
    for stone in S:
        if stone in J:
            total = total + 1
    return total


print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))
print(numJewelsInStones("oPFgls", "aAPfFgiwiwis"))