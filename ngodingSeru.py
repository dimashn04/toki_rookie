a, b, c, k = input().split()
a, b, c, k = int(a), int(b), int(c), int(k)

if k == 0:
    list_nums = [a,b,c]
    list_nums.sort(reverse=True)
elif k == 1:
    list_nums = [a,b,c]
    list_nums.sort()

for nums in list_nums:
    print(nums, end =" ")