def find_short(s):
    words = s.split() # split the sentence so I can loop through it
    smallest_word = words[0] # need a starting point for smallest word
    
    for word in words:
        if (len(word) < len(smallest_word)): # if the length of the word is smaller than the current smallest word 
            smallest_word = word # change the smallest word to THAT smaller word - loops through the entire sentence

    return len(smallest_word) # returns the length of the smallest word
        
    
