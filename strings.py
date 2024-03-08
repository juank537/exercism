"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return "un" + word

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    new_list = [vocab_words[0]]

    for i in vocab_words[1::]:
        new_list.append(vocab_words[0] + i)

    return (" :: ").join(new_list)


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word[-5] == 'i':
        return word[:-5] + "y"
    return word[:-4]


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    sentence_list = sentence.split(" ")
    sentence_list[-1] = sentence_list[-1][:-1]
    return sentence_list[index] + "en"
    


# print(add_prefix_un('believe'))
# print(make_word_groups(['en', 'close', 'joy', 'lighten']))
# print(remove_suffix_ness('heaviness'))
# print(remove_suffix_ness('sadness'))
# print(remove_suffix_ness('hungriness'))
# print(remove_suffix_ness('happiness'))

print(adjective_to_verb("It got dark as the sun set.", 2))
print(adjective_to_verb("Look at the bright sky.", -2))
print(adjective_to_verb('His expression went dark.', -1))
print(adjective_to_verb('The bread got hard after sitting out.', 3))
print(adjective_to_verb('The butter got soft in the sun.', 3))
print(adjective_to_verb('Her eyes were light blue.', -2))
print(adjective_to_verb('The morning fog made everything damp with mist.', 5))
print(adjective_to_verb('Charles made weak crying noises.', 2))
print(adjective_to_verb('The black oil got on the white dog.', 1))




# Mejores Respuestas

def make_word_groups_best(vocab_words):
    return (" :: " + vocab_words[0]).join(vocab_words)


def remove_suffix_ness_best(word):
    return word[:-4] if word[-5] != 'i' else word[:-5]+'y'


def adjective_to_verb_best(sentence, index):
    return sentence.split()[index].strip(".")+'en'