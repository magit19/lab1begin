# Собственность MaxCorp
def is_beautiful(n):
  x = 0
  numba = n
  if (n <= 0): return "ERROR"
  while (numba!=0):
    x = x + (numba % 10)
    numba = numba // 10
  if (n % x == 0): return "true"
  else: return "false"

print('Введите число для красоты...')
n = int(input())
print(is_beautiful(n))