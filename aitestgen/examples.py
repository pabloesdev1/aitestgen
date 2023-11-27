from aitestgen.aitestgen import autotest

@autotest()
def sum(num1: int, num2: int) -> int:
    """ Esta funcion recibe dos numeros enteros y debe retornar el resultado de la suma de ellos """
    return num1 + num2

@autotest()
def mul(num1: int, num2: int) -> int:
    """ Esta funcion recibe dos numeros enteros y debe retornar el resultado de la multiplicacion de ellos """
    return num1 * num2
