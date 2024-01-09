ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
MAX = 10
LEFT = "left"
RIGHT = "right"
OPERATORS = ['+', '-', '*', '/', '(', ')', '^', '%', '@', '&', '$', '~', '!', 'm']
PRIORITY = {'+': ONE, '-': ONE, '*': TWO, '/': TWO, '^': THREE, '%': FOUR, '@': FIVE, '&': FIVE, '$': FIVE, '~': SIX,
            '!': SIX, 'm': MAX}
UNARY = {'!': RIGHT, '~': LEFT, 'm': LEFT}

"""
if char == '(' and ')' == string[i + 1]:
    raise ValueError(f"ValueError: cannot put blank ()")
if char == ')' and ('(' not in lst or i + 1 < len(string) and string[i + 1] not in OPERATORS or i - 1 >= 0 and string[
    i - 1] not in OPERATORS):
    raise ValueError(f"ValueError: Not valid input , incorrect syntaxx")
if char == '(' and (
        ')' not in string or i + 1 < len(string) and string[i + 1] not in OPERATORS or i - 1 >= 0 and string[
    i - 1] not in OPERATORS):
    raise ValueError(f"ValueError: Not valid input , incorrect syntax")
"""
