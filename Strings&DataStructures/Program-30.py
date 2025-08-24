def findSubstring(s, words):

    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = {}

    #Count Frequency in  dict
    for w in words:
        word_count[w] = word_count.get(w, 0) + 1

    result = []

    # sliding window technique
    for i in range(len(s) - total_len + 1):
        seen = {}
        j = 0
        while j < len(words):
            word = s[i + j*word_len : i + (j+1)*word_len]
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count[word]:
                    break
            else:
                break
            j += 1
        if j == len(words):
            result.append(i)

    return result

s = input()
n = int(input())
words = []

for _ in range(n):
    words.append(input())

print(findSubstring(s, words))