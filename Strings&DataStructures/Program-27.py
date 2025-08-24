def find(s, k):
    freq = {}
    order = []

    for i, ch in enumerate(s):
        if ch not in freq:
            freq[ch] = [1, i]
            order.append(ch)
        else:
            freq[ch][0] += 1

    # collect non-repeating characters in order
    non_repeats = [ch for ch in order if freq[ch][0] == 1]

    if k <= len(non_repeats):
        return non_repeats[k - 1]
    else:
        return "Less than k non-repeating characters in input."


s = input("Enter the string: ")
k = int(input("Enter k: "))
print(find(s, k-1))