# Mortal Fibonacci Rabbits

def mortal_rabbits(n, m):
    """
    This function is an application of Fibonacci's rabbit reproduction problem.
    Starting with one pair, the number of rabbit pairs present after n months with litters of 1 pairs is determined
    when the rabbits live only m months.

    Input: positive integers n and m
    Returns: total rabbit pairs present after n months if each pair produces a litter of k rabbit pairs and live m months
    """
    f = [1, 1]  # beginning of Fibonacci sequence
    for i in range(2, n):
        rabbits = f[i-1] + f[i-2]  # dynamic programming solution for Fibonacci sequence
        if i == m:
            rabbits -= 1
        elif i > m:
            rabbits -= f[i - m - 1]
        f.append(rabbits)
    return f[-1]
