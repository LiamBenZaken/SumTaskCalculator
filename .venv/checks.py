from const import OPERATORS, UNARY


def findUnaryPostErrors(char: str, string: str, i: int):
    if (i + 1 < len(string) and string[i + 1].isdigit()):
        raise ValueError(f"ValueError: Not valid input , incorrect syntax for the char:'{char}' ")


def findUnaryPreErrors(char: str, string: str, i: int):
    if ((i + 1 < len(string) and string[i + 1] != '-' and string[i].isdigit()) or len(
            string) <= i + 1 or i - 1 != -1 and string[i-1] in UNARY):
        raise ValueError(f"ValueError: Not valid input , incorrect syntax for the char:'{char}' ")
