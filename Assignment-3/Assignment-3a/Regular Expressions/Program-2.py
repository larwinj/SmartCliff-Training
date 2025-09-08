import re

def extract_dates(text):
    pattern = r'\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}\.\d{2}\.\d{2})\b'
    return re.findall(pattern, text)

text = input("Enter the text: ")
print(extract_dates(text))
