def is_beautiful(n):
	s = 0
	a = n
	while n > 0:
		s = s + n%10
		n = n//10 
	if a%s == 0:
		s = True
	else:
		s = False
	return s
n = int(input("Введите число: "))
print(is_beautiful(n))
