def is_beautiful(n):
	s = 0
	a = n
	while n > 0:
		s = s + n%10
		n = n//10 
	g = a%s == 0
	return g
n = int(input("Введите число: "))
print(is_beautiful(n))
