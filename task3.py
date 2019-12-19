def is_beautiful(n):
	s = 0
	c = n
	while n>0:
		s = s + n%10
		n = n // 10
	if c%s == 0: s = ("True")
	else: s = ("False")
	return s

n = int(input())
print(is_beautiful(n))
