from scratch import prime_check
import math as m

prime_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

test_range = range(101)

def test_prime_check():
   assert prime_check(test_range) == prime_100
