def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True

def prime_number_list(length):
    result = []
    i=1
    while len(result) != length:
        if is_prime(i):
            result.append(i)
        i += 1
    return result

length = int(input('Length? '))
print(prime_number_list(length))