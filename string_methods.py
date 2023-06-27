#strings are lists of characters
"""for character in string:
    print(string[character])"""




def palindrome(string):
    reversed_str = ""
    high = len(string) - 1
    low = 0
    while string:
        if string[high] == string[low]:


def remove_non_alpha_numeric(sentence):
    cleaned = ""
    for character in sentence:
        if character.isalnum():
            cleaned = cleaned + character
    return cleaned

string = "Go hang a salami, I'm a lasagna hog."
print(remove_non_alpha_numeric(string))
palindrome(string)
