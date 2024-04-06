# Mendel's First Law

def mendelian(k, m, n):
    """
    This function calculates the probability of Mendelian inheritance of dominant alleles
    given random mating between homozygous dominant (k), heterozygous (m), and homozygous recessive (n) individuals.

    Input: the number of k, m, and n individuals in the population as three positive integers
    Returns: the probability that two randomly selected mating organisms will produce an individual
    possessing a dominant allele as a decimal
    """
    total_pop = k + m + n
    # calculating the probability of only recessive alleles
    both_rec = (n/total_pop)*((n-1)/(total_pop-1))  # all of these will be only recessive
    both_het = (m/total_pop)*((m-1)/(total_pop-1))  # a quarter of these will be only recessive
    het_rec = (n/total_pop)*(m/(total_pop-1)) + (m/total_pop)*(n/(total_pop-1))  # half of these will be only recessive
    return 1 - (both_rec + both_het/4 + het_rec/2)  # probability of dominant is one minus recessive probability
