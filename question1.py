#returns true if any character of the word is a digit using loop
def contains_digit(word):
    return any(char.isdigit() for char in word)

#returns true if any character of the word is in upper case using loop
def contains_uppercase(word):
    return any(char.isupper() for char in word)

def check_strength(password):
    #if conditions for the mentioned criterias to check the strength
    if len(password)<6:
        return('Weak password')
    elif len(password)>=6 and len(password)<=10 and contains_digit(password):
        return('Medium password')
    elif len(password)>10 and contains_digit(password) and contains_uppercase(password):
        return('Strong password')
    else:
        #for the criteria not mentioned in the question
        return('Can not decide')
    
password = input('Enter a password: ')
print(check_strength(password))
