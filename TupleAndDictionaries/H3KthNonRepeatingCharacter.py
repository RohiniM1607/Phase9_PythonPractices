s = "goods for goods"
k = 3
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
count = 0
for ch in s:
    if freq[ch] == 1:
        count += 1
        if count == k:
            print(ch)
            break
else:
    print("Less than k non-repeating characters in input.")