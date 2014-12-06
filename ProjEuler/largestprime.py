import time

def isPrime(num):
  if num == 2:
    return True
  i = 2
  while i < num/2:
    if num % i == 0:
      return False
    i += 1
  return True


def primeFactorOfNumber(num):



s = time.time()
isPrime()
e = time.time()
print e - s



