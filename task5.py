def is_prime(n):
	for i in range(2, (n-1)):
		if n%i == 0: 
			return False
	else:
	   return True
n = int(input())
print(is_prime(n))
