# Name: Sandeep Chhetri
# Student ID: s396070

#returns true if any character of the word is a digit using loop and false if not
def contains_digit(word):
    return any(char.isdigit() for char in word)     #isdigit() checks a character whether it is a digit or not 

#returns true if any character of the word is in upper case using loop
def contains_uppercase(word):
    return any(char.isupper() for char in word)     #isupper() is used to check if a character is upper case or not

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
