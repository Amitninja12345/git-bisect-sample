def fibo(n):
    """Compute the nth Fibonacci number.
    Raises if n is negative
    :param n: the index of the Fibonacci number we want to compute
    :type n: int
    :returns: int
    :raises: ValueError
    """
    if n < 0:
        raise ValueError("n must be positive.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
