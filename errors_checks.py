from const import OPERATORS, UNARY, LEFT


def findUnaryPostErrors(char: str, string: str, i: int):
    """
    Check for errors related to unary operators appearing after operands.

    Parameters:
    - char (str): The unary operator character.
    - string (str): The input mathematical expression as a string.
    - i (int): The current index in the string.

    Raises:
    - ValueError: If there is an error related to the placement of unary operators.
    """
    if (i + 1 < len(string) and string[i + 1].isdigit()):
        raise ValueError(f"ValueError: Not valid input , incorrect syntax for the char:'{char}' ")


def findUnaryPreErrors(char: str, string: str, i: int):
    """
    Check for errors related to unary operators appearing before operands.

    Parameters:
    - char (str): The unary operator character.
    - string (str): The input mathematical expression as a string.
    - i (int): The current index in the string.

    Raises:
    - ValueError: If there is an error related to the placement of unary operators.
    """
    if ((i + 1 < len(string) and string[i + 1] != '-' and string[i].isdigit()) or len(
            string) <= i + 1 or i - 1 != -1 and string[i - 1] in UNARY):
        raise ValueError(f"ValueError: Not valid input , incorrect syntax for the char:'{char}' ")


def findBracketsErrors(char: str, string: str, i: int):
    """
    Check for errors related to brackets in the mathematical expression.

    Parameters:
    - char (str): The parenthesis character.
    - string (str): The input mathematical expression as a string.
    - i (int): The current index in the string.

    Raises:
    - ValueError: If there is an error related to brackets.
    """
    if char == '(' and ')' not in string or char == ')' and '(' not in string:
        raise ValueError("ValueError: missing brackets")
    if string.count('(') != string.count(')'):
        raise ValueError("ValueError: worng number of Brackets")
    elif char == '(' and i + 1 < len(string) and ')' == string[i + 1] or char == ')' and i + 1 < len(string) and '(' == \
            string[i + 1] or char == ')' and i == 0 or char == '(' and i == len(string):
        raise ValueError(f"ValueError: invalid use with Brackets")
    elif (char == '(' and
          (i == 0 or string[i - 1] not in OPERATORS) and
          (i + 1 < len(string) and string[i + 1] not in UNARY and string[i + 1] != '-' and string[
              i + 1] in OPERATORS and string[i + 1] != '(')):
        raise ValueError("ValueError: unmatching value in the Brackets")
    elif (char == ')' and ((i + 1 < len(string) and string[i + 1] not in OPERATORS) or
                           (i - 1 >= 0 and (string[i - 1] not in UNARY and string[i - 1] in OPERATORS and string[
                               i - 1] != ')')))):
        raise ValueError("ValueError: unmatching value in the Brackets")
