n = int(input())

numbers = input().split(" ", n)
numbers = numbers[::-1]

x = ','.join(numbers)
print(x)