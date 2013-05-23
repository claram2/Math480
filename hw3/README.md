Math480
=======
Euclidean algorithm (from homework 2)

timeit('euclidean_algorithim_python(9971*37, 9971*3)')
	625 loops, best of 3: 18.4 µs per loop

timeit('euclidean_algorithim_cython(9971*37, 9971*3)')
	625 loops, best of 3: 599 ns per loop

=======
Finding the sum of the squares of all the numbers up to n

timeit('sum_of_squares_python(10000)')
	625 loops, best of 3: 1.16 ms per loop

timeit('sum_of_squares_cython(10000)')
	625 loops, best of 3: 6.11 µs per loop

=======
Finding all the primes up to n

timeit('primes_up_to_n_python(10000)')
	5 loops, best of 3: 48.6 ms per loop

timeit('primes_up_to_n_cython(10000)')
	125 loops, best of 3: 4.89 ms per loop

=======
Finding the determinant of a 4x4 matrix (though mine works for anything 2x2 or larger)

timeit('det_of_nxn_python(n)')
	625 loops, best of 3: 70.4 µs per loop

timeit('det_of_nxn_cython(n)')
	625 loops, best of 3: 10.6 µs per loop

=======
Multiplying two 4x4 matrices together

timeit('multiply_4x4_4x4_python(n,m)')
	625 loops, best of 3: 18.8 µs per loop

timeit('multiply_4x4_4x4_cython(n,m)')
	625 loops, best of 3: 4.56 µs per loop

=======
The restrictiveness of the code for 4x4 multiplication annoyed me so I wrote a version just to multiply two matrices together as long as they were compatable sizes

timeit('multiply_axb_bxc_python(n,m)')
	625 loops, best of 3: 22.1 µs per loop

timeit('multiply_axb_bxc_cython(n,m)')
	625 loops, best of 3: 4.79 µs per loop
