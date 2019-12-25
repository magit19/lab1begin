def is_prime(n):
	counter = 0
	x = 1
	while (x <= n):
		if (n % x == 0):
			counter = counter + 1
		x = x + 1
		if (counter > 2):
			return "False"
	return "True"

print('Введите простое число...')
n = int(input())
print(is_prime(n))
