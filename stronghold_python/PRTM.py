# Calculating Protein Mass

def calc_mass(prot_string):
    """
    This function calculates the mass of a protein given its sequence.

    Input: a protein string
    Returns: the mass of the given protein based on the monoisotopic mass of each amino acid
    """
    monoisotopic_mass = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
        'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
        'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111,
        'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
    }
    mass = 0  # initialize mass
    for aa in prot_string:
        mass += monoisotopic_mass[aa]  # loop through and add mass of each amino acid
    return round(mass,3)
