def add_nums(*args):
    """
    Suma todos los números proporcionados.

    :param args: Cualquier número de argumentos numéricos.
    :returns: La suma de todos los números
    :rtype: int o float

    Ejemplo:
        >>> add_nums(2, 3, 5)
        10
        >>> add_nums(1, 2, 3, 4)
        10
    """
    return sum(args)
