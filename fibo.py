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
    result = 0
    if n <= 2 :
        result = n
    else:
        result = fibo(n-1) + fibo(n-2)
    return result
