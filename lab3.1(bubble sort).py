from random import randint
n = 10
a = []
for i in range(n):
    a.append(randint(1, 99))
print(a)
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[i]:
            a[j], a[i] = a[i], a[j]
print(a)
