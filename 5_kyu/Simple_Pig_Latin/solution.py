from re import match

def pig_it(text):
    
    # split the text into words
    split_text = text.split()
    
    # prep the empty array
    pigLatin = []
    
    # for each word...
    for word in split_text:
    
    # if it's a WORD split it after 1st index and add the first letter at the end THEN add ay 
        if match('[a-zA-Z]', word):
            pigLatin.append(word[1:] + word[0]+ "ay")
            
    # if it is a punctuation mark - just add it onto the array 
        else:
            pigLatin.append(word)
    
    return " ".join(pigLatin)
