n, d = input().split()
n, d = int(n), int(d)

c = []
for i in range(n):
    numbers =  int(input())
    c.append(numbers)

if d in c:
    print(c.index(d))
else:
    print(-1)
