from collections import Counter

def duplicate_count(text):
    
    # lower it since case insensitive
    
    lower_text = text.lower()
    
    # count everything using Counter and convert it to a dictionairy
    
    count_dict = dict(Counter(lower_text))
    
    # initialise a counter
    
    count_duplicate = 0
    
    # loop through the count_dict and IF it is greater than one +1 to the duplicate counter
    
    for value in count_dict.values():
        if (value > 1):
            count_duplicate += 1
    
    return count_duplicate
