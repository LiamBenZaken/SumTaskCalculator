from operation_class import MathUtility


def checkBinaryOP(x: float, op: str, y: float) -> float:
    """
    Method which perform a binary operation on two numbers.

    Parameters:
    - x (float): The first number.
    - op (str): The binary operator.
    - y (float): The second number.

    Returns:
    - float: The result of the binary operation.
    """
    match op:
        case '+':
            return MathUtility.add(x, y)
        case '-':
            return MathUtility.sub(x, y)
        case '*':
            return MathUtility.mult(x, y)
        case '/':
            return MathUtility.div(x, y)
        case '^':
            return MathUtility.pow(x, y)
        case '@':
            return MathUtility.avg(x, y)
        case '$':
            return MathUtility.max(x, y)
        case '&':
            return MathUtility.min(x, y)
        case '%':
            return MathUtility.mod(x, y)


def checkUnaryOP(op: str, x: str) -> float:
    """
    Method which perform a unary operation on a number.

    Parameters:
    - op (str): The unary operator to be applied.
    - x (float): The operand.

    Returns:
    - float: The result of the unary operation.
    """
    match op:
        case '~':
            return MathUtility.neg(x)
        case '!':
            return MathUtility.fuc(x)
        case 'm':
            return MathUtility.neg(x)
        case '#':
            return MathUtility.concat(x)
