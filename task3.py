def is_beautiful(n):
    sum = 0
    while (n != 0):
        sum = sum + (n % 10)
        n = n // 10
    if (n % x == 0):
        return "True"
    else:
        return "False"

print('Введите число для красоты...')
n = int(input())
print(is_beautiful(n))
