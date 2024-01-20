from errors_checks import findUnaryPostErrors, findUnaryPreErrors, findBracketsErrors
from const import UNARY, OPERATORS, LEFT, RIGHT


def delUnaryMinusDuplication(lst: list) -> list:
    """
    Method which remove duplicate unary minus signs and
    check private case that connected to the brackes with the unary minus.

    Parameters:
    - lst (list): The list representing the mathematical expression.

    Returns:
    - list: The modified list after removing duplicate unary minus signs.

    Raises:
    - ValueError: If there is an issue with the placement of unary minus signs.
    """
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
    return lst


def replaceToUnaryMinus(lst: list) -> list:
    """
    Method which replace strings starting with '-' with 'm' that represent the unary minus and
    check private case that connected to the brackes with the unary minus.

    Parameters:
    - lst (list): The list representing the mathematical expression.

    Returns:
    - list: The modified list after replacing strings with '-' to 'm' only if the conditions really happened.
    """
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
    return lst


def stringToList(string: str) -> list:
    """
    Method which convert a mathematical expression string to a list of tokens and
    simultaneous catches an errors with the user input.

    Parameters:
    - string (str): The input mathematical expression as a string.

    Returns:
    - list: The list of tokens representing the mathematical expression.

    Raises:
    - ValueError: If there is an issue with the input string that doesnt connected to the specific errors
      that i try to find in the findErrors methods.
    """
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

    lst = delUnaryMinusDuplication(lst)
    lst = replaceToUnaryMinus(lst)

    for i in range(len(lst)):
        try:
            if lst[i] == "0" or float(lst[i]):
                lst[i] = float(lst[i])
        except ValueError as err:
            pass
    return lst
