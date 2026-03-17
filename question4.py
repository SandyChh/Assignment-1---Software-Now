#Suman Dulal; s396420 Part
#The given requirement of Question no 4:
# The question has asked the user to enter a sentence and performs several analyses:
# 1. Counts the total number of words
# 2. Finds the longest word
# 3. Displays the sentence in different formats (uppercase, lowercase, title case, reversed)


sentence = input("Enter a sentence: ")   # Ask the user to input a sentence

words = sentence.split()                 # Split the sentence into words

total_words = len(words)                 # Count total number of words

longest_word = max(words, key=len)       # Find the longest word

uppercase_sentence = sentence.upper()    # All letters in uppercase
lowercase_sentence = sentence.lower()    # All letters in lowercase
titlecase_sentence = sentence.title()    # First letter of each word capitalized


reversed_sentence = sentence[::-1]       # Reverse the sentence


# Displaying the results with clear formatting

print("\n Sentence Analysis Results")
print("Original Sentence:", sentence)

print("\nTotal number of words:", total_words)
print("Longest word:", longest_word)

print("\nCase Transformations")
print("Uppercase:", uppercase_sentence)
print("Lowercase:", lowercase_sentence)
print("Title Case:", titlecase_sentence)

print("\nReversed Sentence")
print(reversed_sentence)