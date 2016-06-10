import sys
from profanity import profanity

def filtered_words(wordlist):
    '''
    Return a word if it is not considered offensive. 
    Arguments: 
        word : string 
    Returns: Word, if it is not included in the offensive_filter 
    '''

    # Load custom offensive dictionary    
    with open('offensive_filter.txt', 'r') as readfile:
        bad_words = readfile.readlines()
        bad_words = [word.strip() for word in bad_words]
        profanity.load_words(bad_words)
        
        with open(wordlist, 'r') as readfile:
            for word in readfile:
                if not profanity.contains_profanity(word):
                    print word

    
wordlist = sys.argv[1]
filtered_words(wordlist)

