class MathUtility:
    @staticmethod
    def add(x: float, y: float) -> float:
        """
       Returns the sum of two numbers.

       Parameters:
       - x (float): The first number.
       - y (float): The second number.

       Returns:
       - float: The result of the addition.
        """
        return x + y

    @staticmethod
    def sub(x: float, y: float) -> float:
        """
        Returns the difference between two numbers.

        Parameters:
        - x (float): The minuend.
        - y (float): The subtrahend.

        Returns:
        - float: The result of the subtraction.
        """
        return x - y

    @staticmethod
    def mult(x: float, y: float) -> float:
        """
        Returns the product of two numbers.

        Parameters:
        - x (float): The first number.
        - y (float): The second number.

        Returns:
        - float: The result of the multiplication.
        """
        return x * y

    @staticmethod
    def div(x: float, y: float) -> float:
        """
       Returns the result of dividing two numbers.

       Parameters:
       - x (float): The dividend.
       - y (float): The divisor.

       Returns:
       - float: The result of the division.

       Raises:
       - ArithmeticError: If attempting to divide by zero.
       """
        if y == 0:
            raise ArithmeticError("ArithmeticError: Cannot divide by zero")
        return round(x / y, 10)

    @staticmethod
    def pow(x: float, y: float) -> float:
        """
        Returns x raised to the power of y.

        Parameters:
        - x (float): The base.
        - y (float): The exponent.

        Returns:
        - float: The result of x raised to the power of y.

        Raises:
        - ArithmeticError: If attempting to calculate the square of a negative number.
        - ArithmeticError: If attempting to calculate the power of 0 to a non-positive exponent.
        - OverflowError: If the result is too large to be represented as a float.
        """
        if x < 0 and (-1 < y < 0 or 0 < y < 1):
            raise ArithmeticError("ArithmeticError: cannot sqrt negative number")
        if x == 0 and y <= 0:
            raise ArithmeticError(f"ArithmeticError: cannot pow {x} with {y} ")
        try:
            return x ** y
        except OverflowError:
            return float("inf")

    @staticmethod
    def avg(x: float, y: float) -> float:
        """
        Returns the average of two numbers.

        Parameters:
        - x (float): The first number.
        - y (float): The second number.

        Returns:
        - float: The average of x and y.
        """
        return (x + y) / 2

    @staticmethod
    def max(x: float, y: float) -> float:
        """
        Returns the maximum of two numbers.

        Parameters:
        - x (float): The first number.
        - y (float): The second number.

        Returns:
        - float: The maximum of x and y.
        """
        return x if x >= y else y

    @staticmethod
    def min(x: float, y: float) -> float:
        """
       Returns the minimum of two numbers.

       Parameters:
       - x (float): The first number.
       - y (float): The second number.

       Returns:
       - float: The minimum of x and y.
       """
        return x if x <= y else y

    @staticmethod
    def mod(x: float, y: float) -> float:
        """
        Returns the remainder of the division of two numbers.

        Parameters:
        - x (float): The dividend.
        - y (float): The divisor.

        Returns:
        - float: The remainder of x divided by y.
        """
        return round(x % y, 10)

    @staticmethod
    def neg(x: float) -> float:
        """
        Returns the negation of a number.

        Parameters:
        - x (float): The number to be negated.

        Returns:
        - float: The negation of x.
        """
        return -x

    @staticmethod
    def fuc(x: float) -> float:
        """
        Returns the factorial of a non negative integer.

        Parameters:
        - x (float): The non-negative integer for calculate the factorial.

        Returns:
        - float: The factorial of x.

        Raises:
        - ArithmeticError: If x is negative or not an integer.
        """
        if x < 0 or x % 1 != 0:
            raise ArithmeticError("ArithmeticError: Cannot calculate fucturial for this number")
        func = 1
        for i in range(1, int(x + 1)):
            func *= i
        return func

    @staticmethod
    def concat(x: float) -> float:
        """
        Returns the sum of the digits of a non negative number.

        Parameters:
        - x (float): The non-negative number for which to calculate the digit sum.

        Returns:
        - float: The sum of the digits of x.

        Raises:
        - ArithmeticError: If x is negative.
        """
        if x < 0:
            raise ArithmeticError("ArithmeticError: Cannot concat negative number")
        x = str(x)
        sum = 0
        for i in range(len(x)):
            if x[i].isdigit():
                sum += int(x[i])
        return sum
