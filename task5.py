# Собственность MaxCorp
def is_prime(n):
	counter = 0
	numba = 1
	x = 1
	if (n <= 0): return "ERROR"
	while (x <= n):
		if (n % x == 0):
			counter = counter + 1
		x = x + 1
		if (counter > 2):
			return "false"
	return "true"

print('Введите простое число...')
n = int(input())
print(is_prime(n))
