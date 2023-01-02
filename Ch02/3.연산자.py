"""
    날짜: 2023/01/02
    이름: 조광호
    내용: 파이썬 연산자 실습하기
"""

# 대입연산자
a = 1
b = c = d = 0
e, f, g = 7, True, 'Apple'

print('a :', a)
print('c :', c)
print('f :', f)
print('g :', g)

# 산술연산자
num1 = 1
num2 = 2
num3,num4 = 3,4

r1 = num1 + num2
r2 = num1 - num2
r3 = num2 * num3
r4 = num2 ** num3
r5 = num4 / num3
r6 = num4 // num3
r7 = num4 % num3

print('r1 : ', r1)
print('r2 : ', r2)
print('r3 : ', r3)
print('r4 : ', r4)
print('r5 : ', r5)
print('r6 : ', r6)
print('r7 : ', r7)

# 복합대입연산자
num5, num6, num7, num8 = 5, 6, 7, 8

num5 += 1
num6 -= 2
num7 *= 3
num8 /= 4

print('num5 : ', num5)
print('num6 : ', num6)
print('num7 : ', num7)
print('num8 : ', num8)

# 비교연산자

# 논리연산자