def find(s1, s2):
    #Split into words
    words1 = s1.split()
    words2 = s2.split()

    #Count occurrences in both sentences
    count = {} # map
    for w in words1 + words2:
        count[w] = count.get(w, 0) + 1

    #Collect words that appear exactly once
    result = []
    for w in count:
        if count[w] == 1:
            result.append(w)

    return result

s1 = input()
s2 = input()

print(find(s1, s2))
