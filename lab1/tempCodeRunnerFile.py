def is_prime(number, divisor=2):
    if number <= 1:
        return False
    if divisor == number:
        return True
    if number % divisor == 0:
        return False
    return is_prime(number, divisor + 1)

num = int(input())
if is_prime(num):
    print("YES")
else:
    print("NO")