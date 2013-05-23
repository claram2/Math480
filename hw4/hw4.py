for b in range(20):
    for c in range(-20,20):
        if not (b % 2 == 1 and c % 2 == 0 or c == 0):
            print "x^2 + " + str(b) + "x + " + str(c)
            primes = 0
            for x in range(200):
                if is_prime(x**2 + b*x + c):
                    primes += 1
            print "primes = " + str(primes)

def hist_of_primes_mod_n(n):
    p = prime_range(10^7)
    p_mod = range(len(p))
    for i in range(len(p)):
        p_mod[i] = p[i] % n
    h = stats.TimeSeries(p_mod)
    if is_prime(n):
        hist = h.histogram(n-1)
    else:
        hist = h.histogram(n-2)
    return hist[0]

for n in range(10, 21):
    print n
    print hist_of_primes_mod_n(n)

x = 0.13869616280169693
c = continued_fraction(x, nterms=20)
c.convergents()

try1 = 1105489/7970581
try2 = 1234567/8901234
print try1 % (37 + 10^15)
print try2 % (37 + 10^15)
print 372806624339965
