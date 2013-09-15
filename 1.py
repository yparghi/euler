import sys


sum = 0
limit = int(sys.argv[1])


for i in range(1, limit):
  if (i % 3 == 0) or (i % 5 == 0):
    sum += i


print "Sum below %d: %d" % (limit, sum)
