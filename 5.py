import prime_gen

input = 20
assert input > 1, "Input must be greater than 1!"

# Get the prime factors (with repetition) of 1 to input and multiply them together.

my_prime_gen = prime_gen.prime_gen()

prime_factor_count = {}

for prime in my_prime_gen:
  if prime > input:
    break
  prime_factor_count[prime] = 0

for i in range(2, input + 1):
  for (prime, count) in prime_factor_count.iteritems():
    this_count = 0
    while i % prime == 0:
      this_count += 1
      i /= prime
    if this_count > count:
      prime_factor_count[prime] = this_count

answer = 1
for (prime, count) in prime_factor_count.iteritems():
  for i in range(count):
    answer *= prime

print "Final answer: %d" % answer
