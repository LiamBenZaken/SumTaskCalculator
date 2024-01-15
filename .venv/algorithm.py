from calls import checkUnaryOP, checkBinaryOP
from input import stringToList
from const import OPERATORS, PRIORITY, UNARY , BEFOREMINUS


def inifxToPostfix(string: str) -> list:
    lst = stringToList(string)
    lstpost = []
    stack = []

    for item in lst:
        if item not in OPERATORS:
            lstpost.append(item)
        elif item == '(':
            stack.append(item)
        elif item == ')':
            while stack and stack[-1] != '(':
                lstpost.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and PRIORITY[item] <= PRIORITY[stack[-1]]:
                if (len(stack) == 1 and stack[-1] == 'm' and item in BEFOREMINUS) or (
                        len(stack) >= 2 and stack[-2] == '(' and stack[-1] == 'm' and item in BEFOREMINUS):
                    break
                lstpost.append(stack.pop())
            stack.append(item)
    while stack:
        lstpost.append(stack.pop())
    print(lstpost)
    return lstpost


def calculator(string: str):
    lst = inifxToPostfix(string)
    stack = []

    for item in lst:
        if item in OPERATORS and item in UNARY:
            if not stack:
                raise ValueError("ValueError: Not valid input")
            op = stack.pop()
            stack.append(checkUnaryOP(item, op))
        elif item in OPERATORS and item not in UNARY:
            if len(stack) < 2:
                raise ValueError("ValueError: Not valid input")
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(checkBinaryOP(op1, item, op2))
        else:
            stack.append(item)

    if len(stack) != 1:
        raise ValueError("ValueError: Not valid input")

    num = stack.pop()
    if num > 10 ** 10 or num < -(10 ** 10):
        return num;
    if num % 1 == 0:
        return int(num)
    return num
