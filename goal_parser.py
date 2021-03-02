# https://leetcode.com/problems/goal-parser-interpretation/
# Hi there
def interpret(command):
    parsed = str()
    i = 0
    for letter in command:
        if letter == 'G':
            parsed = parsed + "G"
            i = i + 1
        elif letter == '(':
            if command[i + 1] == ')':
                parsed = parsed + "o"
                i = i + 1
            elif command[i + 1] == 'a':
                parsed = parsed + "al"
                i = i + 1
        else:
            i = i + 1
    return parsed


print(interpret("G()(al)"))
print(interpret("G()()()()(al)"))
print(interpret("(al)G(al)()()G"))


def interpret2(command):
    if '()' in command:
        command = command.replace('()', 'o')
    if '(al)' in command:
        command = command.replace('(al)', 'al')
    return command


print(interpret2("G()(al)"))
print(interpret2("G()()()()(al)"))
print(interpret2("(al)G(al)()()G"))
