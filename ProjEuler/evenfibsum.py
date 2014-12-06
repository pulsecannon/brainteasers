import time

def evenFibSum():
  evenfib = 0
  a, b = 0, 1
  while b < 4000000:
    a, b = b, a + b
    if b % 2 == 0:
      evenfib += b
  print evenfib


s = time.time()
evenFibSum()
e = time.time()
print e - s

