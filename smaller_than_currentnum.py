# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

def smallerNumbersThanCurrent1(nums):
    final = list()
    for num1 in nums:
        lesser = 0
        for num2 in nums:
            if num2 < num1:
                lesser += 1
        final.append(lesser)
    return final


def smallerNumbersThanCurrent(nums):
    final = list()
    as_sort = nums.copy()
    as_sort.sort()
    for num in nums:
        final.append(as_sort.index(num))
    return final


print(smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
print(smallerNumbersThanCurrent([6, 5, 4, 8]))
print(smallerNumbersThanCurrent([7, 7, 7, 7]))
