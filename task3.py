def is_beautiful(n):
	s = 0
	
	while n > 0:
		s = s + n%10
		n = n // 10



		

	
		if n%s == 0:
			s = True
		else:
			s = False
		return s
print('Введите число')		
n = int(input())
print(is_beautiful(n))

