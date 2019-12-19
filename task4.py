def is_power_of_two(n):
	s = 0
	a = 1
	while a != n:
		a = a*2
		if a > n:
			break

	if a == n:
		s = True
	else:
		s = False
	return s
	
	

	

n = int(input())
print(is_power_of_two(n))
