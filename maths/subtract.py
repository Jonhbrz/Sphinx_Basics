# maths/subtract.py
def subtract_nums(*args):
    """
    Resta todos los números de izquierda a derecha.

    :param args: Cualquier número de argumentos numéricos.
    :returns: Resultado de restar todos los números en orden
    :rtype: int o float

    Ejemplo:
        >>> subtract_nums(100, 20, 30, 40)
        10
        >>> subtract_nums(50, 10, 5)
        35
    """
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
