# https://leetcode.com/problems/running-sum-of-1d-array/

def running_sum(nums):
    new_list = list()
    run_sum = 0
    for i in nums:
        run_sum = run_sum + i
        new_list.append(run_sum)
    return new_list


print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))

million_list = list()
j = 1
while j <= 1000:
    million_list.append(1000000)
    j = j + 1
print(running_sum(million_list))
