
def string_conv(string):
    """given a string of words 'abc def ghi' where the separator is a " ", 
    will format into a list with the following format: ['abc', 'def', 'ghi'],
    so that the result can be added to the LANGUAGES list in languages,py"""
    word = "" #initialize empty string
    
    result = [] #initialize list that will contain the formatted strings
    for i in range(0, len(string)):
        
        if string[i].isspace() != True:
            #if the character specified is not a space, add it to the word
            word = word + string[i]
            
        elif string[i].isspace()==True:
            #if the character is a space, this is the end of the word, add to list
            result.append(word)
            word = "" #clear word
    return result   

#example below    
#convert = '''the of to and a in is it you that he was for on are with as I his 
#             they be at one have this from or had by hot word but what some we 
#             can out other were all there when up use your how said an each she
#             '''
#outputme = string_conv(convert)

#can append to LANGUAGES after, add support for more languages if you want!
    
        