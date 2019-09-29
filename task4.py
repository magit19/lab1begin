def is_power_of_two(n):
	s = 0
	if n & (n-1) == 0: #Нашел это решение в интернете, не очень понял что из себя предстовляет оператор "&"
		s = "True"
	else:
		s = "False"
	return s
n = int(input("Введите число: "))
print(is_power_of_two(n))
