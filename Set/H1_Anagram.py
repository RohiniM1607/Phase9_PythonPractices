def anagram_groups(words):
    groups = {}
    for w in words:
        key = "".join(sorted(w.replace(" ", "")))
        groups.setdefault(key, set()).add(w)
    return list(groups.values())
n = int(input())
words = [input() for _ in range(n)]
print(anagram_groups(words))