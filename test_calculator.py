import pytest

from main import calculation


@pytest.mark.parametrize("input_test, result", [
    ("3+*1", "ValueError: Not valid mathematical expression"),
    ("3..2", "ValueError: Not valid input: '.'"),
    ("!3", "ValueError: Not valid input , incorrect syntax for the char:'!' "),
    ("(-5)^-0.5", "ArithmeticError: cannot use pow on negative number with float exponent"),
    ("3----2!#", "ArithmeticError: Cannot calculate fucturial for this number"),
    ("liam the king", "ValueError: Not valid input: 'l'"),
    ('', "ValueError: Not valid mathematical expression"),
    (' ', "ValueError: Not valid mathematical expression"),
    ("2.^:3", "ValueError: Not valid input: ':'"),
    ("5 + 3 * 2", 11),
    ("2+44", 46),
    ("2.33#", 8),
    ("3!-5", 1),
    ("40%5", 0),
    ("40$100", 100),
    ("400&1", 1),
    ("(4+4)", 8),
    ("10/5", 2),
    ("10@30", 20),
    ("5^2", 25),
    ("-5--2", -3),
    ("~-4.2^2$6.7+3.1@1.5/2-8^2", 14926.066686990747),
    ("5.6*3.2@2.1+1-7^2/4%3+6*5.4", -0.7599999999999909),
    ("7&2.8@3.5+1-4^2*6/2*3.4+9", -150.04999999999998),
    ("~-6&2.3*3.6+7^2*4/3.1-9^2", -9.494193548400006),
    ("10$4/2^2-3!+1*2+4^2.3", 22.751465064166364),
    ("8*2.5@4%3.2+1-6/2*7-2.1", -21.700000000000003),
    ("5&2$3.4%2-6^2+1@7*4.6-8", -24.200000000000003),
    ("~-4*2.6#+5.5+6*3@8-2*9.4", 51.7),
    ("7+3.2$4@2^2-1+8/2*6+3.9", 42.9),
    ("7&2.8@3.5+1-4^2*6/2*3.4+9 - 1.7", -151.74999999999997),
    ("~-6&2.3*3.6+7^2*4/3.1-9^2 + 4.2", -5.294193548400005),
    ("4.1^2@6-3*2.8+7^2*4-5*3 * 1.4", 449.1760999999999),
    ("7+3.2$4@2^2-1+8/2*6+3.9 - 4.5", 38.4),
    ("~-4.2^2$6.7+3.1@1.5/2-8^2 + 6.3 - 4.2", 14928.166686990746),
    ("5.6*3.2@2.1+1-7^2/4%3+6*5.4 - 2.8 + 9.1", 5.540000000000009),
    ("10$4/2^2-3!+1*2+4^2.3 * 5 + 8.6", 128.35732532083182),
    ("6&2^3.1$4+5*-9/3+7^2.6 * 3.7 - 8.2", 575.5155775535179),
    ("~-4*2.6#-5.5+6*3@8-2*9.4 * 2.1 - 7.8", 12.219999999999995),
    ("9-2$4.3%2+5*3@4-7.2^2 * 3.6 + 2.5 - 1.9", -159.82400000000004),
    ("4.1^2@6.7/3+8%1-7+2*5-4 * 2.5 - 3.2 + 7.4", 151.54356312540003),
    ("7+3.2$4@2^2-1+8/2*6+3.9 - 4.5 + 1.6 * 7.3", 50.08)
])
def test_my_code(input_test, result):
    """
    Test the hole calculator with various input expressions and expected results.

    Parameters:
    - input_test (str): The input expression to be evaluated.
    - result: The expected result of the calculation or an error message.
    """
    assert calculation(input_test) == result
