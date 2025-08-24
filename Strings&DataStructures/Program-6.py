def func(words):
    result = []
    visited = [False] * len(words)

    for i in range(len(words)):
        if not visited[i]:
            group = [words[i]]
            visited[i] = True
            for j in range(i + 1, len(words)):
                if not visited[j] and sorted(words[i]) == sorted(words[j]):
                    group.append(words[j])
                    visited[j] = True
            result.append(group)

    return result


n = int(input().strip())
words = []
for _ in range(n):
    words.append(input().strip())

result = func(words)
print(result)
