# https://leetcode.com/problems/richest-customer-wealth/
def rich_customer(accounts):
    max_wealth = 0
    for customer in accounts:
        new_wealth = sum(customer)
        if new_wealth > max_wealth:
            max_wealth = new_wealth
    return max_wealth


print(rich_customer([[1, 2, 3], [3, 2, 1]]))
print(rich_customer([[1, 5], [7, 3], [3, 5]]))
print(rich_customer([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
