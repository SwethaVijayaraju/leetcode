# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

def kids_with_candies(candies, extraCandies):
    original_greatest = max(candies)
    output = list()
    for original in candies:
        updated_candies = original + extraCandies
        output.append(updated_candies >= original_greatest)
    return output


print(kids_with_candies([2, 3, 5, 1, 3], 3))
print(kids_with_candies([4, 2, 1, 1, 2], 1))
print(kids_with_candies([12, 1, 12], 10))
