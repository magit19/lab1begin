def is_prime(n):
	s = 2
	if n == 1: return False
	for a in range(2, n):
		if n % s == 0: return False
	else: return True
n = int(input())
print(is_prime(n))
