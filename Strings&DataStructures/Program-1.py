def find(text):
    words = text.split()
    res = []
    for i in words:

        # keeping alphanumeric words
        if i.isalnum():
            has_digit = any(ch.isdigit() for ch in i)
            has_letter = any(ch.isalpha() for ch in i)
            if has_digit and has_letter:
                res.append(i)
    return res

text = input()
result = find(text)

for word in result:
    print(word)

