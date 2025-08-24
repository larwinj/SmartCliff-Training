from collections import Counter

def find(original_list):
    freq = Counter(original_list)
    count = 0

    for tup in freq:
        rev = (tup[1], tup[0])
        if rev in freq:
            count += freq[tup] * freq[rev]

    # Each pair is counted twice, so divide by 2
    return count // 2

inp = eval(input("Enter the original list: "))
print(find(inp))