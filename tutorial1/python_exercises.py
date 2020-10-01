"""
Intro to python exercises shell code
"""

def is_odd(x):
    return x % 2 != 0
    """
    returns True if x is odd and False otherwise
    """


def is_palindrome(word):
    return word == word[::-1]
    """
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    output = []
    for i in numlist:
        output.append(i)
    return output
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    output = dict()
    text.lower()
    words = text.split(" ")
    for word in words:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1
    return output
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
