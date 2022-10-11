p, q = input().split()
p, q = int(p), int(q)

whole = p**2 + q**2 + 1

if whole % 4:
    print(-1)
else:
    print(whole // 4)