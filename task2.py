# Собственность MaxCorp
def digit_sum(n):
  x = 0
  if (n <= 0): return "ERROR"
  while (n!=0):
    x = x + (n % 10)
    n = n // 10
  return x

print('Введите число')
n = int(input())
print(digit_sum(n))