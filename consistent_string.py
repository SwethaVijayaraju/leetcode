# https://leetcode.com/problems/count-the-number-of-consistent-strings/
def countConsistentStrings(allowed, words):
    final = len(words)
    for word in words:
        for letter in word:
            if not letter in allowed:
                final -= 1
                break
    return final


print(countConsistentStrings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
print(countConsistentStrings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(countConsistentStrings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
