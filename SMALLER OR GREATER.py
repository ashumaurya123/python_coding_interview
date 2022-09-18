a = [2987, 576, 498, 323, 543, 32]
smaller = a[0]
for i in range(len(a)):
    if a[i] < smaller:
        smaller = a[i]

print(smaller)