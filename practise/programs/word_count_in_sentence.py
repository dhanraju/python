"""This module counts number of words present in a sentence."""
def word_count(sentence):
    '''Count number of words in the sentence.'''
    words = sentence.split()
    return len(words)

if __name__ == '__main__':
    SENTENCE = raw_input(
        "Enter a sentence to find number of words present in it.")
    print(word_count(SENTENCE))
