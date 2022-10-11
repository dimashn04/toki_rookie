def grade_checker(n):
    if 0 <= n <= 100:
        return "YA"
    else:
        return "TIDAK"

n = int(input())
print(grade_checker(n))