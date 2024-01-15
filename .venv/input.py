from checks import findUnaryPostErrors, findUnaryPreErrors, findBracketsErrors
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
        elif char == '-' and (not current or current[-1] in OPERATORS) and (
                (i - 1 >= 0 and string[i - 1] != ')') or (i == 0)):
            current += char
            i += 1
        elif char != 'm' and char in OPERATORS:
            if current:
                lst.append(current)
                current = ""
            if char in UNARY and UNARY[char] == LEFT:
                findUnaryPreErrors(char, string, i)
            elif char in UNARY and UNARY[char] == RIGHT:
                findUnaryPostErrors(char, string, i)
            elif char == '(' or char == ')':
                findBracketsErrors(char, string, i)
            lst.append(char)
            i += 1

        else:
            raise ValueError(f"ValueError: Not valid input: '{char}'")
    if current:
        lst.append(current)
    i = 0
    while i < len(lst):
        minus = lst[i].count('-')
        if minus > 1:
            if minus % 2 == 0 and lst[i][-1].isdigit():
                lst[i] = lst[i].replace('-', '')
            elif minus % 2 == 0 and i + 1 < len(lst) and lst[i + 1] in UNARY and UNARY[lst[i + 1]] == LEFT:
                raise ValueError("ValueError: The minus unary is not in the right place ")
            elif minus % 2 == 0:
                lst.pop(i)
            else:
                lst[i] = lst[i].replace('-', '')
                lst[i] = '-' + lst[i]
        i += 1
    i = 0
    while i < len(lst):  # private cases
        if lst[i] == '-' and i == 0 and i + 2 < len(lst) and lst[i + 1] == '-' and lst[i + 2] == '(':
            lst.pop(i)
            lst.pop(i)
        if lst[i] == '-' and i + 2 < len(lst) and lst[i + 1] == '-' and lst[i + 2] == '(':
            lst[i + 1] = lst[i + 1].replace('-', 'm')
        i += 1

    for i in range(len(lst)):
        if lst[i].startswith('-') and len(lst[i]) > 1:
            if i - 1 != -1 and (lst[i - 1] in UNARY and UNARY[lst[i - 1]] == RIGHT or lst[i] in "1234567890)"):
                lst.insert(i, '-')
            else:
                lst.insert(i, 'm')
            lst[i + 1] = lst[i + 1].replace('-', '')
        if (lst[i] == '-' and len(lst) > i + 1 and lst[i + 1] == '(' and (
                ((i - 1 >= 0 and lst[i - 1] not in UNARY and lst[i - 1] in OPERATORS) or i == 0))):
            lst[i] = lst[i].replace('-', 'm')

    for i in range(len(lst)):
        try:
            if lst[i] == "0" or float(lst[i]):
                lst[i] = float(lst[i])
        except ValueError as err:
            pass
    print(lst)
    return lst
