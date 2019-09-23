def digit_sum(n):
	s = 0
	while n > 0:
		s = s + n % 10
		n = n // 10
	return s

def is_beautiful(n):
	if n % digit_sum(n) == 0:
		return True
	else:
		return False

print('Введите число')
n = int(input())
print(is_beautiful(n))