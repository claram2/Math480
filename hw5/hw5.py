def find_nd(a,m):
    d = 1
    n = 0
    while a*d <= m and d <= sqrt(m/2):
        while n <= sqrt(m/2):
            if n == ((d*a) % m):
                print str(n) + " " + str(d)
                return true
            n += 1
        d += 1
    return false
a = 389
m = 5077
print find_nd(a,m)
a = 17
m = 10000
print find_nd(a,m)
a = 123456789
m = 2345678910
print find_nd(a,m)
a = 8171666302
m = 10000000000
print find_nd(a,m)

n = 4654252230393111226989449826741007006486078009450861095070222439898324342353927553909251532232407850265642079868425916328810273416481567992145162141358151
i = 1
while i < n:
    if Mod(i,n)^(n-1) == 1:
        print "n is not a prime"
        break
    i += 1
        
p = round(sqrt(n))
while true:
    if n % p == 0:
        break
    else:
        p -= 1

q = n/p
print "p = " + str(p) + " q = " + str(q)
print "p*q = " + str(p*q)
print "n   = " + str(n)
