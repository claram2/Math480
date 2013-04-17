def euclidean_algorithm(a, b):
    rold2 = a
    rold1 = b
    rnew = b
    while rnew != 0:
        rnew = rold2 - rold1*(rold2/rold1)
        rold2 = rold1
        rold1 = rnew
    return rold2

def factor_int(n):
    if not isinstance(n, (int, long)):
        raise TypeError("n must be an integer")
    i = 2
    factors = []
    if n == 1:
        factors.append(1)
    while n != 1:
        if n % i == 0:
            factors.append(i)
            n /= i
        else:
            i += 1
    return factors

def find_divisors_of_int(n):
    if not isinstance(n, (int, long)):
        raise TypeError("n must be an integer")
    divisors = []
    i = 1
    while i <= n:
        if len(divisors) > 0 and (divisors[len(divisors)-1] * i == n or divisors[len(divisors)-2] * i == n):
            break
        elif n % i == 0:
            divisors.append(i)
        i += 1
    len_div = len(divisors)
    for i in range(len_div):
        j = n / divisors[len_div - i -1]
        if not divisors[len_div - 1] == j:
            divisors.append(j)
    return divisors

def intersect_lists(l1, l2):
    l3 = []
    for item in l1:
#        if l2.contains(item):
        for item2 in l2:
            if item == item2:
                l3.append(item)
                break
    return l3

def common_divisors(n, m):
    if not isinstance(n, (int, long)) or not isinstance(m, (int, long)):
        raise TypeError("n and m must be integers")
    ln = find_divisors_of_int(n)
    lm = find_divisors_of_int(m)
    return intersect_lists(ln, lm)

def greatest_common_divisor(n, m):
    if not isinstance(n, (int, long)) or not isinstance(m, (int, long)):
        raise TypeError("n and m must be integers")
    return max(common_divisors(n,m))

def least_common_multiple(n, m):
    if not isinstance(n, (int, long)) or not isinstance(m, (int, long)):
        raise TypeError("n and m must be integers")
    r = n
    while r % m != 0:
        r += n
    return r

"""
r = int(raw_input("How many integers to factor? "))
for i in range(r):
    m = int(raw_input("Integer to factor: "))
    print 'Factors:'
    for item in factor_int(m):
        print item,
    print ''
    print 'Divisors:'
    for item in find_divisors_of_int(m):
        print item,
    print ''
"""

n = int(raw_input("first integer: "))
m = int(raw_input("second integer: "))
print "greatest common divisor:"
print greatest_common_divisor(n,m)
print "euclidean algorithm:"
print euclidean_algorithm(n,m)
print "least common multiple:"
print least_common_multiple(n,m)
