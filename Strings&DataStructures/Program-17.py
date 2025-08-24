def remove(test_list, K):
    return [t for t in test_list if len(t) != K]

list = eval(input("test_list = "))
K = int(input())

result = remove(list, K)
print("Output:", result)
