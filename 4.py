import sys

product_min = 100
product_max = 999


def is_palindrome(n):
  s = str(n)
  return s == s[::-1]

largest_palindrome = 0

for i in range(product_max, product_min - 1, -1):
  for j in range(product_max, product_min - 1, -1):
    product = i * j
    if product < largest_palindrome:
      break
    elif is_palindrome(product):
      largest_palindrome = product


print "The largest palindrome is %d" % largest_palindrome
