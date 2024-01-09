from checks import findUnaryPostErrors, findUnaryPreErrors
from const import UNARY, OPERATORS, LEFT, RIGHT


def stringToList(string: str) -> list:
    string = string.replace(" ", "").replace("\t", "").replace("\n", "")
    lst = []
    current = ""
    i = 0

    for char in string:
        if char.isdigit() or (char == '.' and current and '.' not in current):
            current += char
            i += 1
        elif char == '-' and (not current or current[-1] in OPERATORS):
            current += char
            i += 1
        elif char != 'm':
            if current:
                lst.append(current)
                current = ""
                negflag = 1
            if char in UNARY and UNARY[char] == LEFT:
                findUnaryPreErrors(char, string, i)
            elif char in UNARY and UNARY[char] == RIGHT:
                findUnaryPostErrors(char, string, i)
            lst.append(char)
            i += 1
        else:
            raise ValueError("ValueError: Not valid input")
    if current:
        lst.append(current)
    for i in range(len(lst)):
        minus = lst[i].count('-')
        if minus > 1:
            if minus % 2 == 0:
                lst[i] = lst[i].replace('-', '')
            else:
                lst[i] = lst[i].replace('-', '')
                lst[i] = '-' + lst[i]

    for i in range(len(lst)):
        if lst[i].startswith('-') and len(lst[i]) > 1:
            if i - 1 != -1 and (lst[i - 1] in UNARY and UNARY[lst[i - 1]] == RIGHT or lst[i] in "1234567890)"):
                lst.insert(i, '-')
            else:
                lst.insert(i, 'm')
            lst[i + 1] = lst[i + 1].replace('-', '')

    for i in range(len(lst)):
        try:
            if float(lst[i]):
                lst[i] = float(lst[i])
        except ValueError as err:
            pass
    return lst
