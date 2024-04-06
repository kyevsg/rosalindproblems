# Rabbits and Recurrence Relations

def rabbit_pairs(n, k):
    """
    This function is an application of Fibonacci's rabbit reproduction problem.
    Starting with one pair, the number of rabbit pairs present after n months with litters of k pairs is determined.

    Input: positive integers n and k
    Returns: total rabbit pairs present after n months if each pair produces a litter of k rabbit pairs
    """
    f = [0, 1]  # first two Fibonacci numbers
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2] * k)  # dynamic programming solution for Fibonacci sequence
    return f[n]
