def is_power_of_two(n):
	x = 2
	while (n >= x):
		if (x == n):
			return "True"
		x = x * 2
	return "False"

print('Введите число для степенности...')
n = int(input())
print(is_power_of_two(n))
