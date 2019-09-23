# Собственность MaxCorp
def is_power_of_two(n):
	x = 2
	if (n <= 0): return "ERROR"
	while (n >= x):
		if (x == n): 
			return "true"
		x = x * 2
	return "false"

print('Введите число для степенности...')
n = int(input())
print(is_power_of_two(n))
