import math
n = int(input())
a = 0
for i in range(int(3 * math.log(n, 2))):
    a += 1
print(a)
