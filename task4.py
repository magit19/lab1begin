def is_power_of_two(n):
	s = 1
	while s < n:
		s = s * 2
	if s == n: s = ("True")
	else: s = ("False")
	return s
n = int(input())
print(is_power_of_two(n))
