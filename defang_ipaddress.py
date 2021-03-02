# https://leetcode.com/problems/defanging-an-ip-address/
def defangIPaddr(address):
    defanged = str()
    for i in address:
        try:
            ip_int = int(i)
            defanged = defanged + str(ip_int)
        except:
            defanged = defanged + '[' + i + ']'
    return defanged


print(defangIPaddr("1.1.1.1"))
print(defangIPaddr("255.100.50.0"))
