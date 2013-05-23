%cython
cpdef long euclidean_algorithm_cython(long a, long b):
    cdef long rold1,rold2,rnew
    rold2 = a
    rold1 = b
    rnew = b
    while rnew != 0:
        rnew = rold2 - rold1*((rold2 - rold2 % rold1)/rold1)
        rold2 = rold1
        rold1 = rnew
    return rold2

cpdef long sum_of_squares_cython(long n):
    cdef long sum = 0
    cdef long i
    for i in range(1,n+1):
        sum += i**2
    return sum

cpdef primes_up_to_n_cython(int n):
    cdef int i,prime
    cdef int is_prime
    primes = []
    for i in range(2,n+1):
        is_prime = 1
        for prime in primes:
            if i % prime == 0:
                is_prime = 0
                break
        if is_prime == 1:
            primes.append(i)
    return primes

cpdef double det_of_nxn_cython(n):
    cdef double ret
    cdef int k,i,j
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
        ret += n[0][k]*((-1)**k)*det_of_nxn_cython(temp)
        temp = []
    return ret

cpdef multiply_4x4_4x4_cython(n,m):
    cdef int i,j,k
    cdef double ij_sum
    result = [[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]]
    for i in range(4):
        for j in range(4):
            ij_sum = 0
            for k in range(4):
                ij_sum += n[i][k] * m[k][j]
            result[i][j] = ij_sum
    return result

cpdef multiply_axb_bxc_cython(n,m):
    cdef int i,j,k
    cdef double ij_sum
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

cpdef print_matrix_cython(n):
    cdef int i,j
    for i in range(len(n)):
        for j in range(len(n[0])):
            print n[i][j],
        print ""
