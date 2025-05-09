# Inferring mRNA from Protein

def protein_to_mrna(protein_string):
    """
    This function computes the number of possible RNA strings from which a given protein could be translated.

    Input: a protein string of length at most 1000 aa
    Returns: the total number of different RNA strings, modulo 1,000,000
    """
    rna_dict = {'F':2,'L':6,'S':6,'Y':2,'C':2,'W':1,'P':4,'H':2,'Q':2,'R':6,'I':3,'M':1,'T':4,'N':2,'K':2,'V':4,'A':4,'D':2,'E':2,'G':4}
    total_strings = 3  # 3 possibilities for stop codons
    for aa in protein_string:
        total_strings = (total_strings * rna_dict[aa]) % 1E6  # for each amino acid, adding on additional possibilities
    return total_strings