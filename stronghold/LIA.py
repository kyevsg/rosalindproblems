# Independent Alleles

import math


def probability(k, n):
    """
    This function calculates the probability that at least N Aa Bb organisms will belong to the k-th generation of a
    family tree that starts with the organism Aa Bb and where all organisms in the tree mate with an Aa Bb organism.

    Input: two positive numbers k and N
    Returns: a probability in the form of a decimal
    """
    p = []
    for i in range(n, 2**k + 1):
        # formula for independent probabilities and append result to probability list
        p.append((math.factorial(2**k) / (math.factorial(i) * math.factorial(2**k - i))) * 0.25**i * 0.75**(2**k - i))
    return sum(p)
