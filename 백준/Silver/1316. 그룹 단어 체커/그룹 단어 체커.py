n = int(input())
count = 0

for _ in range(n):
    word = input()
    used = set()
    prev = ''
    is_group = True

    for ch in word:
        if ch != prev:
            if ch in used:
                is_group = False
                break
            used.add(ch)
        prev = ch

    if is_group:
        count += 1

print(count)
