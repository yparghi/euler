input = 100
assert input > 1

sum_of_squares = 0
for i in range(1, input+1):
  sum_of_squares += i**2

square_of_sum = (input * (input + 1) / 2) ** 2

print "Difference: %d" % (square_of_sum - sum_of_squares)
