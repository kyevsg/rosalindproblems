# Finding a Motif in DNA

def substring(s, t):
    """
    This function returns all starting locations within a DNA string s for the substring t.

    Input: two DNA strings s and t
    Returns: all locations of t as a subset of s
    """
    locations = []  # initialize list of locations
    # save location of the start of substring whenever substring is found
    for i in range(0, len(s)):
        if s[i:i+len(t)] == t:
            locations.append(str(i+1))  # need to add one to convert python index into position
    return ' '.join(locations)
