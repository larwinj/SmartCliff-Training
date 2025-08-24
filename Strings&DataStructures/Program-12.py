s1 = input("string1=")

words = s1.split()

if len(words) != 3:
    print("Input must contain exactly three words.")
else:
    # Default order
    print("Print String in default order:")
    print("{}".format(" ".join(words)))

    # Positional order
    print("Print String in Positional order:")
    print("{1} {0} {2}".format(words[0], words[1], words[2]))

    # Keyword order
    print("Print String in order of Keywords:")
    print("{c} {b} {a}".format(a=words[0], b=words[1], c=words[2]))
