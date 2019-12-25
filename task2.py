def digit_sum(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10
    return x

print('Введите число')
n = int(input())
print(digit_sum(n))
