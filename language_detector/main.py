from .languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    '''Detects language name based on # of matches of common words to words in text'''
    
    #lists that will hold counts for each language
    lang_match_counts = [] 
    
    #iterate sequentially through languages list
    for language in range(len(languages)): 
        
        lang_match_counts.append(0) #initialize the language match word count for the language
        common_word_set = languages[language]['common_words'] 
        #access to language's common words
        
        for word in common_word_set:  
            lang_match_counts[language] += text.count(" " + word)
        
    #send lang_match_counts to function that matches it to the language, depending on its index
    index_of_language = which_language(lang_match_counts)
    return languages[index_of_language]['name']
def which_language(match_counts):
    '''helps determines the language by returning the index of match_counts that has
    the highest value, which corresponds to language name in lang_list'''
    high = 0 #holds highest value of match_counts, initiallizing here
    for item in range (len(match_counts)): 
        #goes through match_counts and saves index of highest value 
        if match_counts[item]>high:
            high = match_counts[item] 
            highindex = item
    return highindex
    