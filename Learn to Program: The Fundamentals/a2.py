def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    length = 0
    
    for char in dna:
        length = length + 1

    return length


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if dna2 in dna1:
        return True
    else:
        return False


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if DNA sequence dna is composed solely of
    nucleotides.

    >>> is_valid_sequence('ATCTGT')
    True
    >>> is_valid_sequence('ATCcat')
    False
    >>> is_valid_sequence('TCGFAF')
    False
    """
    validity = True

    for char in dna:
        if char not in 'ATCG':
            validity = False

    return validity


def insert_sequence(dna1, dna2, position):
    """ (str, str, int) -> str

    Return a DNA string that inserts dna2 at index position of dna1.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('ATCG', 'TCG', 5)
    'ATCGTCG'
    >>> insert_sequence('GGGCCC', 'ATA', 0)
    'ATAGGGCCC'
    """
    return dna1[:position] + dna2 + dna1[position:]


def get_complement(nucleotide):
    """ (str) -> str

    Return the complimentary nucleotide of parameter nucleotide.

    >>> get_complement('G')
    'C'
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    """
    if nucleotide == 'A':
        return 'T'

    if nucleotide == 'T':
        return 'A'

    if nucleotide == 'C':
        return 'G'

    if nucleotide == 'G':
        return 'C'


def get_complementary_sequence(dna):
    """ (str) -> str

    Return the complimentary sequence to dna.

    >>> get_complementary_sequence('ATCG')
    'TAGC'
    >>> get_complementary_sequence('CCGG')
    'GGCC'
    """
    sequence = ''
    for char in dna:
        sequence = sequence + get_complement(char)

    return sequence
