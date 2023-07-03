"""Write a function named uses_only that takes a word and a string of letters, and that
returns True if the word contains only letters in the list. Can you make a sentence
using only the letters acefhlo? Other than “Hoe alfalfa?”"""
def used_only(word, string_letter):
    for letter in word:
        if letter not in string_letter:
            return False
    return True
print(used_only('hello','leo'))


