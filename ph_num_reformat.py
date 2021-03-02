# https://leetcode.com/problems/reformat-phone-number/
def split(clean_num):
    if len(clean_num) == 2:
        return clean_num
    if len(clean_num) == 3:
        return clean_num
    if len(clean_num) == 4:
        clean_num = clean_num[:2] + '-' + clean_num[2:]
        return clean_num
def reformatNumber(number):
    clean_num = str()
    for num in number:
        try:
            int_num = int(num)
            clean_num = clean_num + str(int_num)
        except:
            continue
    new_num = str()
    i = 0
    if len(clean_num)%3 == 0:
        for num in clean_num:
            if i

print(reformatNumber("1-23-45 6"))
print(reformatNumber("123 4-567"))
print(reformatNumber("123 4-5678"))
print(reformatNumber("12"))
print(reformatNumber("--17-5 229 35-39475 "))
