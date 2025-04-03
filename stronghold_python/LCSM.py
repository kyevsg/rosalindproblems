# Finding a Shared Motif

def shared_motif(data):
    """
    This function finds the longest shared motif (longest common substring) in a list of DNA strings using dynamic programming.

    Input: DNA strings in FASTA format
    Returns: the longest shared motif in the strings
    """
    dna_strings = []
    with open(data, 'r') as file:
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    dna_strings.append(seq)
                seq = ""
            else:
                seq += line
        if seq:
            dna_strings.append(seq)
    ref_string = dna_strings[0]  # first string is the reference string
    longest_motif = ""
    for i in range(len(ref_string)):
        for j in range(i+1, len(ref_string)+1):
            motif = ref_string[i:j]
            if all(motif in string for string in dna_strings[1:]):
                if len(motif) > len(longest_motif):
                    longest_motif = motif
    print(longest_motif)
    return longest_motif  # return the longest motif
