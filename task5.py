def is_prime(n):
	s = 2
	while n % s != 0: 
		s += 1 
	return s == n
n = int(input("Введите число: "))
print(is_prime(n))
