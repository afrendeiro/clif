def add(a: int, b: int) -> int:
    """
    Add two integers.


    Parameters
    ----------
    a : int
        Integer to be added.
    b : int
        Integer to be added.

    Returns
    ----------
    int
        Integer sum.
    """
    return a + b


add.__doc__ = """
Add two integers.

Add integers and return the sum.

:param a: Integer to be added.
:param b: Integer to be added.

:returns: Integer sum.
"""


def unnanotated_function(a, b):
    pass


def sum_mix(a: int, b: float):
    return a + b


def brief_docstring(a: int, b: float):
    """Brief description"""
    return a + b


def brief_docstring_one_param(a: int, b: float):
    """
    Brief description

    :param a: Integer to be added.
    """
    return a + b
