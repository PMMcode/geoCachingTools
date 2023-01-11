import logging
import sys

'''The script calculates the sum of all letter values in a given word.
'''

def letter_word_value(word):
    word = word.upper()
    letter_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                     'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
                     'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, 'Ä': 27, 'Ö': 28,
                     'Ü': 29, 'ß': 30 }
    word_value = 0
    for letter in word:
        word_value += letter_values[letter]
    return word_value



if len(sys.argv) != 2:
    raise ValueError('Please provide a DestinationId as first argument.')

word = sys.argv[1]

print(f"Der Wortwert von {word} beträgt {letter_word_value(word)}")
