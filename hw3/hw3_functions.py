def euclidean_algorithm_python(a, b):
    rold2 = a
    rold1 = b
    rnew = 1
    while rnew != 0:
        rnew = rold2 - rold1*((rold2 - rold2 % rold1)/rold1)
        rold2 = rold1
        rold1 = rnew
    return rold2

def sum_of_squares_python(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

def primes_up_to_n_python(n):
    primes = []
    for i in range(2,n+1):
        is_prime = true
        for prime in primes:
            if i % prime == 0:
                is_prime = false
                break
        if is_prime:
            primes.append(i)
    return primes

def det_of_nxn_python(n):
    if len(n) == 2:
        return n[0][0]*n[1][1] - n[0][1]*n[1][0]
    temp = []
    ret = 0.0
    for k in range(len(n[0])):
        for i in range(len(n)-1):
            temp.append([])
            for j in range(len(n[0])):
                if j != k:
                    temp[i].append(n[i+1][j])
        ret += n[0][k]*((-1)**k)*det_of_nxn_python(temp)
        temp = []
    return ret

def multiply_4x4_4x4_python(n,m):
    result = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            ij_sum = 0
            for k in range(4):
                ij_sum += n[i][k] * m[k][j]
            result[i][j] = ij_sum
    return result

def multiply_axb_bxc_python(n,m):
    if len(n[0]) != len(m):
        raise TypeError("Dimensions of n and m do not match")
    result = []
    for i in range(len(n)):
        result.append([])
        for j in range(len(m[0])):
            ij_sum = 0
            for k in range(len(m)):
                ij_sum += n[i][k] * m[k][j]
            result[i].append(ij_sum)
    return result

def print_matrix_python(n):
    for i in range(len(n)):
        for j in range(len(n[0])):
            print n[i][j],
        print ""
