# maths/multiply.py
def multiply_nums(*args):
    """
    Multiplica todos los números proporcionados.

    :param args: Cualquier número de argumentos numéricos.
    :returns: Producto de todos los números
    :rtype: int o float

    Ejemplo:
        >>> multiply_nums(2, 3, 4)
        24
        >>> multiply_nums(1, 5, 2)
        10
    """
    result = 1
    for num in args:
        result *= num
    return result
