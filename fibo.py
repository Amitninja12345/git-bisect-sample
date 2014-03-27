def fibo(n):
    """Compute the nth Fibonacci number.
    :param n: the index of the Fibonacci number we want to compute
    :type n: int
    :returns: int
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
