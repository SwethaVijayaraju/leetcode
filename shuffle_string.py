# https://leetcode.com/problems/shuffle-string/
def restoreString(s, indices):
    mapping = dict()
    n = 0
    for position in indices:
        mapping[position] = s[n]
        n += 1

    ascending = sorted(indices)
    restored = str()
    for pos in ascending:
        restored = restored + mapping[pos]
    return restored


print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
print(restoreString("abc", [0, 1, 2]))
print(restoreString("aiohn", [3, 1, 4, 2, 0]))
print(restoreString("aaiougrt", [4, 0, 2, 6, 7, 3, 1, 5]))
print(restoreString("art", [1, 0, 2]))
