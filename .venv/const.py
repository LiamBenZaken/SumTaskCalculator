ONE = 1
TWO = 2
THREE = 3
FOUR = 4
FIVE = 5
SIX = 6
MAX = 10
LEFT = "left"
RIGHT = "right"
OPERATORS = ['+', '-', '*', '/', '(', ')', '^', '%', '@', '&', '$', '~', '!', 'm', '#']
PRIORITY = {'+': ONE, '-': ONE, '*': TWO, '/': TWO, '^': THREE, '%': FOUR, '@': FIVE, '&': FIVE, '$': FIVE, '~': SIX,
            '!': SIX, '#': SIX, 'm': MAX}
UNARY = {'!': RIGHT, '~': LEFT, 'm': LEFT, '#': RIGHT}
BEFOREMINUS = [operator for operator in PRIORITY if operator != 'm' and PRIORITY[operator]>TWO]