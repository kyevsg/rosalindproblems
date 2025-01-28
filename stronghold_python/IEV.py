# Calculating Expected Offspring

def offspring(a, b, c, d, e, f):
    """
    This function takes in counts of couples with the genotypes AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, and aa-aa
    and returns the expected number of offspring displaying the dominant phenotype in the next generation.

    Input: 6 nonnegative integers
    Returns: expected number of offspring displaying the dominant phenotype
    """
    return 2*a + 2*b + 2*c + 1.5*d + 1*e + 0*f  # return expected offspring


print(offspring(19356, 16128, 17959, 16768, 16441, 16236))
