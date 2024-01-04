def stringToList(string: str) -> list:
    valid_list = []
    current_element = ""
    for i, char in enumerate(string):
        if char.isdigit() or (char == '-' and (i == 0 or expression[i - 1] in ('+', '-', '*', '/', '('))):
            current_element += char
        elif char == '.':
            current_element += char
        elif char in ('(', ')', '+', '-', '*', '/'):
            if current_element:
                valid_list.append(float(current_element))
                current_element = ""
            valid_list.append(char)
        elif char != ' ':
            current_element += char

    if current_element:
        valid_list.append(float(current_element))

    return valid_list
