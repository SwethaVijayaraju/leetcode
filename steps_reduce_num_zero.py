# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
def numberOfSteps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps = steps + 1
    return steps


print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))