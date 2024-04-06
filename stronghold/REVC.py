# Complementing a Strand of DNA

def transcription(dna_string):
    """
    This function returns the reverse complement of a DNA sequence.

    Input: a DNA string
    Returns: the reverse complement string
    """
    rev_string = dna_string[::-1]  # reverses the dna string
    comp_string = rev_string.translate(str.maketrans("ACGT", "TGCA"))  # replace bases with their complements
    return comp_string
