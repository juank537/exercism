"""
PIG LATIN
Instructions
Implement a program that translates from English to Pig Latin.

Pig Latin is a made-up children's language that's intended to be confusing. It obeys a few simple rules (below), but when it's spoken quickly it's really difficult for non-children (and non-native speakers) to understand.

Rule 1: If a word begins with a vowel sound, add an "ay" sound to the end of the word. Please note that "xr" and "yt" at the beginning of a word make vowel sounds (e.g. "xray" -> "xrayay", "yttria" -> "yttriaay").
Rule 2: If a word begins with a consonant sound, move it to the end of the word and then add an "ay" sound to the end of the word. Consonant sounds can be made up of multiple consonants, such as the "ch" in "chair" or "st" in "stand" (e.g. "chair" -> "airchay").
Rule 3: If a word starts with a consonant sound followed by "qu", move it to the end of the word, and then add an "ay" sound to the end of the word (e.g. "square" -> "aresquay").
Rule 4: If a word contains a "y" after a consonant cluster or as the second letter in a two letter word it makes a vowel sound (e.g. "rhythm" -> "ythmrhay", "my" -> "ymay").
"""


def is_vowel(l):
    return l in ['a', 'e', 'i', 'o', 'u', 'y', 'x']

def translate(text):
    if is_vowel(text[0]) or text[:2] in ['xr', 'yt']:
        return text + 'ay'
    if not is_vowel(text[0]) and text[1:3] == 'qu':
        return text[3:] + text[0] + 'quay'
    if text[:2] == 'qu':
        return text[2:] + 'quay'
    for i in range(len(text)):
        if is_vowel(text[i]) or (text[i] == 'y' and i > 0):
            return text[i:] + text[:i] + 'ay'


print(translate('square'))
print(translate('rhythm'))
print(translate('chair'))
print(translate('my'))
print(translate('yttria'))
print(translate('xray'))

