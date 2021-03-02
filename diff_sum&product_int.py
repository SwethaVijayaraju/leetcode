# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
def subtractProductAndSum(n):
    string = str(n)
    nums = list()
    for num in string:
        nums.append(int(num))
    product = 1
    for i in nums:
        product = product * i
    return product - sum(nums)


print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))