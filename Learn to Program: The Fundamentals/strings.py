def count_vowels(s):
    ''' (str) -> int

    Return the nomber of vowels in s. Do not treat the
    letter y as a vowel.

    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''
    num_vowels = 0
    
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1

    return num_vowels


def collect_vowels(s):
    ''' (str) -> str

    Returns the vowels from s. Do not treat the letter
    y as a vowel.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    '''
    vowels = ''

    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels


def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but not including
    the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''
    
    # before_vowel contains all the characters found in s[0:i].
    before_vowel = ''
    i = 0

    # Acumulate the non-vowels at the beginning of the string.
    while i < len(s) and not(s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel


def last_vowel(s):
    ''' (str) -> str

    Return the last vowel in s if one exists; otherwise, return None.

    >>> last_vowel('banana')
    'a'
    >>> last_vowel('pfft')
    None
    '''
    #i is the last indice of the string.
    i = len(s) - 1

    #Checks each character, from the end to the beginning, until it finds a vowel.
    while i >= 0:
        if s[i] in 'aeiouAEIOU':
            return s[i]
        i = i -1
    return None

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of ocurrences of a character and an adjacent
    character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    >>> count_adjacent_repeats('joyful')
    0
    '''
    #repeats acumulates the number of repetitions.
    repeats = 0

    #Compares each character to the next one.
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            repeats = repeats + 1

    return repeats

def count_matches(s1, s2):
    ''' (str, str) -> int

    Return the number of positions in s1 that contain the same character
    as the corresponding position of s2.

    Precondition: len(s1) == len(s2)

    >>> count_matches('ate', 'ape')
    2
    >>> count_matches('head', 'hard')
    2
    '''
    #Accumulates the number of matches
    matches = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            matches = matches + 1

    return matches
