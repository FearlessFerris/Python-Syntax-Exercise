


# 2.) Turn it into a function 

def print_upper_words(words):

    # This function prints all words to uppercase

    for word in words:
        print(word.upper())



# 3.) Change the function so that it only prints words that start with the letter 'e' either upper or lowercase

def print_upper_e_words(words):

# Only prints words that begin with 'e'
    
    
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())



# 4.) Make your function accept a set of letters and have it only print words that start with those letters

def print_upper_words2(words, start_with):

    # Only prints words that begin with the sets of letters passed in

    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())
                break


                

        