# find([1,2,2,3], 3) => True

def find(numlist, num):
    return num in numlist


print(find([1, 2, 2, 3], 3))
print(find([1, 2, 2, 9], 3))
print('--------------------------------')


def find(numlist, num):
    for i in numlist:
        if i == num:
            return True
    return False


print(find([1, 2, 2, 3], 3))
print(find([1, 2, 2, 9], 3))
print('--------------------------------')


def slicing(position, numlist, num):
    if numlist[position] == num:
        return True
    elif numlist[position] < num:
        new_numlist = numlist[(position + 1):]
        return num in new_numlist
    else:
        new_numlist = numlist[:(position - 1)]
        return num in new_numlist


def find_sorted(numlist, num):
    total = len(numlist)
    if numlist[-1] == num:
        return True
    elif numlist[-1] < num:
        return False
    else:
        if total % 2 == 0:
            position = int(total / 2)
            return slicing(position, numlist, num)
        else:
            position = int(total / 2) + 1
            return slicing(position, numlist, num)


print(find_sorted([1, 2, 2, 3], 3))
print(find_sorted([1, 2, 2, 9], 12))
print(find_sorted([1, 2, 4, 5, 7, 9], 5))
print(find_sorted([1, 2, 4, 5, 7, 9], 2))
print(find_sorted([1, 2, 4, 5, 9], 5))
print(find_sorted([1, 2, 4, 5, 9], 2))
print('--------------------------------')