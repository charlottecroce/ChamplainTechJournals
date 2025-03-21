import string
from alice import alice_text

def word_frequency(text):
    """Generates a word frequency dictionary for the supplied text.  All punctuation is stripped and the case is converted to lowercase.

    Example dictionary: {'the': 2, 'cat': 1, 'bit': 1, 'dog': 1}

    param text: (string) The text to be analyzed
    return: (dict) Word frequency dictionary
    """
    # Strip Punctuation
    for character in string.punctuation:
        text = text.replace(character, "")
    
    # Convert to lower case
    text = text.lower()

    # Generate a list of all of the words
    words = text.split()

    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency


# Code for testing purposes. Do not modify
short_sentence = "The silly cat is the silly face."
print(f'Analyzing word frequency of "{short_sentence}"')
print(word_frequency("The silly cat is the silly face."))

print()
try:
    print('In Alice and Wonderland,')
    alice_freq = word_frequency(alice_text)
    print(f'The word Alice occurs {alice_freq["alice"]} times')
    print(f'The word melancholy occurs {alice_freq["melancholy"]} times')
    print(f'{len(alice_freq)} different words are used in the book.')
except Exception as e:
    print('Exception raised when analyzing Alice in Wonderland:')
    print(e)
