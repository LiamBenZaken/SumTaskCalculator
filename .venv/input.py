OPERATORS = ['+', '-', '*', '/', '(', ')', '^', '%', '@', '&', '$', '~', '!']


def stringToList(string: str) -> list:
    lst = []
    current = ""
    negflag = 1
    i=0

    for char in string:
        if char.isdigit() or (char == '.' and current and current[-1].isdigit()):
            current += char
        elif char == '-' and (not current or current[-1] in OPERATORS):
            negflag *= -1
        elif char in OPERATORS:
            if current:
                if char == '~' and ((i + 1 < len(string) and string[i + 1] in OPERATORS) or len(string) == i+1):
                    raise ValueError("Not valid input")
                lst.append(negflag * float(current))
                current = ""
                negflag = 1
            lst.append(char)
        elif char != ' ':
            current += char
        i+=1

    if current:
        lst.append(negflag * float(current))

    return lst



