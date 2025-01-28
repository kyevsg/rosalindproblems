# Counting Point Mutations

def hamming(seq1, seq2):
    """
    This function counts the number of point mutations in a DNA string, outputting the Hamming distance.

    Input: two DNA strings of equal length
    Returns: the Hamming distance as an integer
    """
    ham_dist = sum(1 for i, j in zip(seq1, seq2) if i != j)  # add 1 to count for each difference
    return ham_dist
