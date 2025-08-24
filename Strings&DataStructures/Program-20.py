def find(emails):
    unique = set()

    for email in emails:
        local, domain = email.split("@")
        # Ignore after '+'
        if '+' in local:
            local = local[:local.index('+')]
        # Remove all '.'
        local = local.replace(".", "")
        unique.add(local + "@" + domain)

    return len(unique)


n = int(input())
emails = [input() for _ in range(n)]

print(find(emails))
