def is_power_of_two(n):
	a = n & (n-1) == 0
	return a
n = int(input("Введите число: "))
print(is_power_of_two(n))
