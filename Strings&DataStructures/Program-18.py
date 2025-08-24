from collections import Counter

def find(dictionary, charset):
    # Storing the frequency of the char
    charset_count = Counter(charset)
    result = []

    for word in dictionary:
        # storing the frequency of the characters in current word

        word_count = Counter(word)
        valid = True
        for ch in word_count:
            if word_count[ch] > charset_count.get(ch, 0):
                valid = False
                break
        if valid:
            result.append(word)
    return result

dictionary = eval(input("input ="))

charset = eval(input("charset ="))

output = find(dictionary, charset)


print("Possible words:", ", ".join(output))