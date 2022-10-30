import math
a = 0
n = int(input())
for i in range(int(n * math.log(n, 2))):
    a += 1
print(a)
