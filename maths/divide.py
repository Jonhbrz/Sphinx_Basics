def divide_nums(*args):
    """
    Divide el primer número por los siguientes, en orden.

    :param args: Cualquier número de argumentos numéricos.
    :returns: Resultado de dividir en secuencia
    :rtype: float

    Ejemplo:
        >>> divide_nums(100, 2, 5)
        10.0
        >>> divide_nums(50, 2)
        25.0
    """
    if not args:
        return None
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("No se puede dividir por cero")
        result /= num
    return result
