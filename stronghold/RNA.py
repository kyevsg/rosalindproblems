def transcription(dna_string):
    """
    This function transcribes a DNA sequence to an RNA one.

    Input: a DNA string
    Returns: the corresponding RNA string
    """
    rna_string = dna_string.replace("T", "U")  # replace T nucleotides with U
    return rna_string
