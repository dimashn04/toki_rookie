n = int(input())

list_nums = []
for i in range(n):
    num = int(input())
    num = str(num)
    list_nums.append(num)

for num in list_nums:
    print(int(num[::-1]))