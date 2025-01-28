# Counting DNA Nucleotides

def count_nucleotides(dna_string):
    """
    This function counts the number of each type of nucleotide within a DNA sequence.

    Input: a DNA string
    Returns: the counts of A, C, G, and T within the DNA string as four integers separated by spaces
    """
    nuc_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}  # initializing a dictionary to store the nucleotide counts
    for nuc in dna_string:
        nuc_count[nuc] += 1  # increment count of nucleotide identified
    return f"{nuc_count['A']} {nuc_count['C']} {nuc_count['G']} {nuc_count['T']}"  # return counts
