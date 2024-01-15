from opClass import MathUtility


def checkBinaryOP(x: float, op: str, y: float):
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


def checkUnaryOP(op: str, x: str):
    match op:
        case '~':
            return MathUtility.neg(x)
        case '!':
            return MathUtility.fuc(x)
        case 'm':
            return MathUtility.neg(x)
        case '#':
            return MathUtility.concat(x)
