"""
Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
def wordPattern(pattern, s):

    words = s.split(" ")

    #Edge Case if the amount of words does not equal the amount chars in pattern
    if len(pattern) != len(words):
        return False

    """
    Logic:
    Create two hashmaps that check both of keys and values.
    
    "abba"
    "dog cat cat dog"
    a -> dog
    b -> cat
    b -> cat
    a -> dog
    
    dog -> a
    cat -> b
    cat -> b
    dog -> a
    """
    characterToWord = {}
    wordToCharacter = {}

    for char, word in zip(pattern,words):
        if char in characterToWord and characterToWord[char] != word:
            return print(False)
        if word in wordToCharacter and wordToCharacter[word] != char:
            return print(False)

        characterToWord[char] = word
        wordToCharacter[word] = char

    return print(True)

wordPattern("abba", "dog cat cat dog")

