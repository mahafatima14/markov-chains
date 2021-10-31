"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
   # return 'Contents of your file as one long string'
    return contents

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    words.append(None)

    for i in range(len(words) - 2):
        word_pair_key = words[i], words[i + 1]
        tuple(word_pair_key)
        word_pair_value = words[i + 2]      
        
        if word_pair_key not in chains: 
            chains[word_pair_key] = [word_pair_value]
        else:
            chains[word_pair_key].append(word_pair_value)

        for keys, values in chains.items():
            print(f'{keys}, {values}')
    
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    # randomly create "link" that selects one of the keys from our dictionary 
    # and a random word from list of values that follows it. Put into words list

    #creates a new key by randomly selecting from the list of keys in the chains dict
    initial_key = choice(list(chains.keys()))
    #indexing the values from initial_key to store in the words list
    words = [initial_key[0], initial_key[1]]
    #adding a randomly selected value from the initial_key in the chains dict and appending it to words list
    
    
    next_word = chains[initial_key]
    #words.append(choice(initial_key))
    
    #loop through text to append until reaches end of text
    new_key = words[-2:]
    new_key = tuple(new_key)
    print("New Key: ", new_key)


    
    
    print("value of words list", words)
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
