# https://leetcode.com/problems/shuffle-the-array/
def shuffle(nums, n):
    shuffled = list()
    for i in range(0, n):
        shuffled.append(nums[i])
        shuffled.append(nums[i + n])
    return shuffled


print(shuffle([2, 5, 1, 3, 4, 7], 3))
print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(shuffle([1, 1, 2, 2], 2))
