t = walltime()
euclidean_algorithm_python(9971*37, 9971*3)
p = walltime(t)
t = walltime()
euclidean_algorithm_cython(9971*37, 9971*3)
c = walltime(t)
print "speedup = " + str(p/c)

t = walltime()
sum_of_squares_python(10000)
p = walltime(t)
t = walltime()
sum_of_squares_cython(10000)
c = walltime(t)
print "speedup = " + str(p/c)

t = walltime()
primes_up_to_n_python(10000)
p = walltime(t)
t = walltime()
primes_up_to_n_cython(10000)
c = walltime(t)
print "speedup = " + str(p/c)

n = [[1,3,5,1],[0,2,3,4],[1,5,3,0],[2,0,1,1]]
t = walltime()
det_of_nxn_python(n)
p = walltime(t)
t = walltime()
det_of_nxn_cython(n)
c = walltime(t)
print "speedup = " + str(p/c)

m = [[6,3,2,9],[3,0,2,5],[2,0,3,7],[7,8,6,1]]
t = walltime()
multiply_4x4_4x4_python(n,m)
p = walltime(p)
t = walltime()
multiply_4x4_4x4_cython(n,m)
c = walltime(t)
print "speedup = " + str(p/c)

t = walltime()
multiply_axb_bxc_python(n,m)
p = walltime(t)
t = walltime()
multiply_axb_bxc_cython(n,m)
c = walltime(t)
print "speedup = " + str(p/c)
