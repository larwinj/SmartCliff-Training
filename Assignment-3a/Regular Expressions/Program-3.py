import re

def extract_tags(html):
    pattern = r'<[^>]+>'
    return re.findall(pattern, html)

s = input("Enter the html: ")

print(extract_tags(s))