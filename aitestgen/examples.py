from aitestgen.autotest import autotest

@autotest()
def sum(num1: float, num2: float) -> float:
    """This function is responsible for calculating the sum of two numbers"""
    return num1 + num2

@autotest()
def mul(num1: float, num2: float) -> float:
    """This function is responsible for calculating the multiplication of two numbers"""
    return num1 * num2
