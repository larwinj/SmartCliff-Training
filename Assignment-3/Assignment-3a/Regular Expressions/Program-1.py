import re
def extract_hashtags_mentions(text):

    pattern = r'[@#]\w+'
    return re.findall(pattern, text)

text = input("Enter the text: ")

print(extract_hashtags_mentions(text))