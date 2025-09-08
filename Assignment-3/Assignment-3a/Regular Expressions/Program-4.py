import re

def same_letter_words(text):
    pattern = r'\b([a-zA-Z])\w*\1\b'
    return re.findall(pattern, text, flags=re.IGNORECASE)

text = input("Enter the text: ")

print(same_letter_words(text))