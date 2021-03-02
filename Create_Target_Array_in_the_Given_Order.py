def createTargetArray(nums, index):
    output = list()
    j = 0
    for i in nums:
        output.insert(index[j], i)
        j += 1
    return output


print(createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1])) #output = [0,4,1,3,2]
print(createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))  #output = [0,1,2,3,4]
print(createTargetArray([1], [0]))  #output = [1]
