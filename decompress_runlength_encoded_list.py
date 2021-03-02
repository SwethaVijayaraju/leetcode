def decompressRLElist(nums):
    try:
        if not 2 <= len(nums) <= 100:
            raise Exception("Number of items exceeds the limit")
        if len(nums) % 2 != 0:
            raise Exception("One value missing")
        for i in nums:
            if not 1 <= i <= 100:
                raise Exception('Value exceeds the limit')
    except Exception as e:
        return str(e) + ". " + 'Give a new list of nums'
    output = list()
    for j in range(0, len(nums), 2):
        k = nums[j]
        output.extend([nums[j + 1]] * k)
    return output


print(decompressRLElist([1, 2, 3, 4]))
print(decompressRLElist([1, 1, 2, 3]))
print(decompressRLElist([1, 1, 2, 100]))