def countMatches(items, ruleKey, ruleValue):
    num = 0
    if ruleKey == 'type':
        for item in items:
            if ruleValue == item[0]:
                num += 1
    elif ruleKey == 'color':
        for item in items:
            if ruleValue == item[1]:
                num += 1
    elif ruleKey == 'name':
        for item in items:
            if ruleValue == item[2]:
                num += 1
    return num


print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
                    ["phone", "gold", "iphone"]], "color", "silver"))
print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]],
                   "type", "phone"))
print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "lenovo"],
                    ["phone", "gold", "iphone"]], "name", "pixel"))
