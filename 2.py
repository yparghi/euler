limit = 4000000

sum = 0
fib_1 = 1
fib_2 = 1
this_fib = 2

# loop invariant: this_fib = fib_1 + fib_2
while (this_fib <= limit):
  print "this_fib: %d" % this_fib
  if (this_fib % 2 == 0):
    sum += this_fib
  fib_1 = fib_2
  fib_2 = this_fib
  this_fib = fib_1 + fib_2

print "Answer: %d" % sum
