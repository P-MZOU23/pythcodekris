"""for character in string:
    print(string[character])"""




def palindrome(cleaned):
    high = len(cleaned) - 1
    low = 0
    while high>low:
        if cleaned[high] == cleaned[low]:
            high = high - 1
            low = low + 1
        else:
            return False
    return True

def remove_non_alpha_numeric(sentence):
    cleaned = ""
    for character in sentence:
        if character.isalnum():
            cleaned = cleaned + character
    return cleaned.lower()



def main():
    sentence = "Go hang a salami, I'm a lasagna hog."
    sentence = "dac"
    
    cleaned = remove_non_alpha_numeric(sentence)
    answer = palindrome(cleaned)
    print(answer)

main()