class MathUtility:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    @staticmethod
    def mult(x, y):
        return x * y

    @staticmethod
    def div(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y

    @staticmethod
    def pow(x, y):
        if x < 0 and -1 < y < 1:
            raise ValueError("Not valid input")
        return x ** y

    @staticmethod
    def avg(x, y):
        return (x + y) / 2

    @staticmethod
    def max(x, y):
        return x if x >= y else y

    @staticmethod
    def min(x, y):
        return x if x <= y else y

    @staticmethod
    def mod(x, y):
        return x % y

    @staticmethod
    def neg(x):
        return -x

    @staticmethod
    def fuc(x):
        if x < 0 or x % 1 != 0 or x > 150:
            raise ValueError("Cannot calculate fucturial for this number")
        if x == 0 or x == 1:
            return 1
        else:
            return MathUtility.fuc(x - 1) * x
