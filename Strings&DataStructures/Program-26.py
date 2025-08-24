def restrict_tuples(K, tuple_list):
    freq = {}
    result = []

    for tup in tuple_list:
        first = tup[0]
        if freq.get(first, 0) < K:
            result.append(tup)
            freq[first] = freq.get(first, 0) + 1

    return result

k = int(input())
list = eval(input("test_list = "))

result = restrict_tuples(k, list)
print(result)

