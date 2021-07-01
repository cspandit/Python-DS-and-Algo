from doctest import testmod

def factorial(n):
    """Lets see how doctest works
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    if n <= 1:
        return 1
    return n*factorial(n-1)


if __name__ == "__main__":
    testmod(name='factorial', verbose=True)
