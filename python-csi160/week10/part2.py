def synonym_lookup(word_pairs, word_to_lookup):
    """Returns synonym for the word to word_to_lookup

    Complete this function by using a dictionary. For each synonym pair, 
    you should add both words as keys to your dictionary with the value being the other word.

    params:
     word_pairs (tuple of tuples): Example: (('Hello', 'Hi'), ('Goodbye','Bye'))
     word_to_lookup (string): The word to find a synonym for 
     return (string): The synonym for the word_to_lookup
    """
    synonym_dict = {}

    # Create a dictionary with both words in each pair
    for word1, word2 in word_pairs:
        synonym_dict[word1] = word2
        synonym_dict[word2] = word1

    # Return the synonym
    return synonym_dict.get(word_to_lookup, None)


example_word_pairs = (('Hello', 'Hi'), ('Goodbye','Bye'), ('Snake', 'Serpent'))

print(f'A synonym for "Serpent" is {synonym_lookup(example_word_pairs, "Serpent")}.  (Snake expected)')
