a, b, c = map(int, input().split())

first = (a+b)%c
second = ((a%c) + (b%c))%c
third = (a * b)%c
four = ((a%c) * (b%c))%c

print(first)
print(second)
print(third)
print(four)