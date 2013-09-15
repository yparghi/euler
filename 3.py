import prime_gen
import sys

input = 600851475143

original_input = input

# Thoughts:
# - break down the number as quickly as possible
# - start with small primes? or faster to start with the biggest factor (non-prime, maybe)
#   - and stop when a factor is smaller than biggest known prime so far
# - Also, use a prime generator?

my_prime_gen = prime_gen.prime_gen()

if input < 1:
  print "Input must be an integer greater than 1!"
  sys.exit(1)

while input > 1:
  next_prime = next(my_prime_gen)
  while input % next_prime == 0:
    input /= next_prime

print "Largest prime factor of %d: %d" % (original_input, next_prime)
