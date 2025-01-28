# Computing GC Content

def comp_gc(data):
    """
    This function returns the highest GC content sequence out of a number of sequences along with the GC percentage.

    Input: DNA strings in FASTA format
    Returns: the ID of the string with highest GC content and its GC content
    """
    with open(data, 'r') as fasta_data:
        ids = []
        gc_values = []
        seq = ''
        for line in fasta_data:  # iterating through file
            if line.startswith('>'):
                ids.append(line[1:])
                # before new sequence starts add gc value of last sequence
                if seq:
                    gc_values.append(100 * (seq.count('G') + seq.count('C')) / len(seq))
                    seq = ''
            else:
                seq += line.strip()
        gc_values.append(100 * (seq.count('G') + seq.count('C')) / len(seq))  # gc value of final sequence
        max_gc = max(gc_values)  # identify max sequence
    return f"{ids[gc_values.index(max_gc)]}{max_gc}"
