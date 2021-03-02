# https://leetcode.com/problems/number-of-good-pairs/
def numIdenticalPairs(nums):
    updated_nums = nums.copy()
    good_pairs = 0
    for i in nums:
        updated_nums.remove(i)
        for j in updated_nums:
            if i == j:
                good_pairs += 1
    return good_pairs


print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(numIdenticalPairs([1, 1, 1, 1]))
print(numIdenticalPairs([1, 2, 3]))
