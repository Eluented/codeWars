def remove_url_anchor(url):
    
    for letter in range(len(url)):
        
        if (url[letter] == "#"):
            
            return url[:letter] #return the sliced ting from the 0th to the letter before hash
        
    else:
        
        return url
