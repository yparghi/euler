def is_prime(candidate, known_primes):
  for prime in known_primes:
    if (candidate % prime) == 0:
      return False
  return True

def prime_gen():
  primes = [2]
  yield 2

  prime_candidate = 2
  while True: 
    prime_candidate += 1
    if is_prime(prime_candidate, primes):
      primes.append(prime_candidate)
      yield prime_candidate
