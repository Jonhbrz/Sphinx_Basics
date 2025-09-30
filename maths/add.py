# maths/add.py
def add_nums(*args):
    """
    Suma cualquier cantidad de números.

    :param int args: Números a sumar
    :returns: La suma de todos los números
    :rtype: int

    Ejemplos:
    >>> add_nums(2, 4, 6)
    12
    >>> add_nums(1, 2, 3, 4)
    10
    """
    return sum(args)