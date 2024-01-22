from algorithm import calculator


def calculation(string: str):
    """
    Method which perform a mathematical calculation based on the provided string expression.

    Parameters:
    - string (str): The mathematical expression to be evaluated.

    Returns:
    - str: The result of the calculation or an error message if an exception is encountered.

    Raises:
    - ValueError: If the input expression is not valid.
    - OverflowError: If the calculation result exceeds the representational limits of the data type.
    - ArithmeticError: If there is an arithmetic error during the calculation.
    - EOFError: If the calculation encounters an End-of-File (EOF) condition.
    """
    try:
        print(calculator(string))
        return calculator(string)
    except (ValueError, OverflowError, ArithmeticError) as err:
        print(err)
        return str(err)


def main():
    """
    Main - gets the mathematical expression from the user
    and use the calculator to get the answer for the provided input.
    """
    try:
        string = input("enter what do u want to calculate:")
    except EOFError:
        print("EOF: bye")
    else:
        calculation(string)


if __name__ == '__main__':
    main()
