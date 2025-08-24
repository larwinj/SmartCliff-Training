def mirror_string(K, s):

    mirror = {}
    for i in range(26):
        mirror[chr(97 + i)] = chr(122 - i)

    result = []
    for i in range(len(s)):
        if i < K - 1:
            result.append(s[i])
        else:
            result.append(mirror[s[i]])

    return "".join(result)


s = input("Enter the string: ")
k = int(input("Enter k: "))

print(mirror_string(k, s))