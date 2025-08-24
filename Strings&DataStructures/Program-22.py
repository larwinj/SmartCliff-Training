def mixed_string(s1, s2):
    s3 = ""
    i, j = 0, len(s2) - 1

    while i < len(s1) and j >= 0:
        s3 += s1[i] + s2[j]
        i += 1
        j -= 1

    # Append leftover characters from s1
    if i < len(s1):
        s3 += s1[i:]

    # Append leftover characters from s2
    if j >= 0:
        s3 += s2[:j+1]

    return s3


s1 = input()
s2 = input()

print(mixed_string(s1, s2))