import numpy as np
import math
def primesfrom3to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns a array of primes, p < n """

    # an assert is entered as a method of debugging. n must be greater than or equal to 2 or else prime calculation will fail. I would think this could bge skipped by getting the numbers absolute value
    assert n>=2

    # new var named 'sifter' (hated the word sieve) and assigning an array of 1's. The parameters for this array will divide the array shape by 2, it also sets the array elements data type as a boolean. ??? Will there ever be a non-boolean data type when using np ones/zeros?
    sifter = np.ones(n/2, dtype=np.bool)

    # iterate over a range of numbers. Since it's using xrange the numbers won't be generated until needed, in situations with enormous lists, this helps. xrange's parameters are (start, stop, [step]), This xrange starts at the number 3 (so 2) and ends at the square root of n (the provided func arg) OR n to the 0.5 power plus one, then steps over 2 elements
    for i in xrange(3,int(n**0.5)+1,2):
        # if sifter is divisible by two expression, I assume if no remainder is left than it's evaluated as "True"; if expression is true,then switch element to be false
        if sifter[i/2]:
            # the the above expression is true, ie: it divides cleanly, then proceed to this statment and set one (or more!?) array elements to false
            sifter[i*i/2::i] = False
    # returns only true values from the sifter array
    return np.r_[2, 2*np.nonzero(sifter)[0][1::]+1]

print primesfrom3to(100)


#things to look up
# numpy - ones, r_, nonzero
# sifter/sifter/numpy
# python - assert, xrange
# wtf!? - return np.r_[2, 2*np.nonzero(sifter)[0][1::]+1]
    # double colon (::) is part of extended slices. Specifically for numpy to skip 3, or step 3.
