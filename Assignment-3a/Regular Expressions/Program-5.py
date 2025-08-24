import re

def extract_phone_numbers(text):
    # Regex for Indian phone numbers
    pattern = r'\b(?:\+91-\d{10}|91\d{10}|[6-9]\d{9})\b'
    return re.findall(pattern, text)

text = input("Enter the text: ")

print(extract_phone_numbers(text))


