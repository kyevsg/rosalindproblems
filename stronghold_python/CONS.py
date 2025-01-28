# Consensus and Profile

def consensus_profile(data):
    """
    This function returns .

    Input: DNA strings of equal length in FASTA format
    Returns: a consensus string and profile matrix for the strings
    """
    dna_strings = []
    with open(data, 'r') as fasta_data:
        for line in fasta_data:
            if not line.startswith('>'):
                dna_strings.append(line.strip())
    zeroes = [0] * len(dna_strings[0])
    profile_matrix = {
        'A': zeroes[:],
        'C': zeroes[:],
        'G': zeroes[:],
        'T': zeroes[:]
    }
    for string in dna_strings:
        for i,c in enumerate(string):
            profile_matrix[c][i] += 1
    consensus_string = ""
    for 
    new_line = "\n"
    return f"{consensus_string}{new_line}{profile_matrix}"


print(consensus_profile("sample.txt"))
