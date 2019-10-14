def is_power_of_two(n):
    if n == 1:
        return True
    if n & 1:
        return False
    return is_power_of_two(n >> 1)
n = int(input())
print(is_power_of_two(n))