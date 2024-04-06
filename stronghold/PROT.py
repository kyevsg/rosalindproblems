# Translating RNA into Protein

def translation(rna_string):
    """
    This function translates an RNA sequence into a protein sequence.

    Input: an RNA string
    Returns: the corresponding protein string
    """
    bases = ['U', 'C', 'A', 'G']
    codons = [a+b+c for a in bases for b in bases for c in bases]
    amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    trans_dict = dict(zip(codons, amino_acids))
    protein_string = ''
    while len(rna_string) > 0:
        if trans_dict[rna_string[:3]] == '*':
            break
        protein_string += trans_dict[rna_string[:3]]
        rna_string = rna_string[3:]
    return protein_string
