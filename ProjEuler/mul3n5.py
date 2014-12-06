import time

def clacMulof3n5in1000():
  mulOf3n5 = [i for i in range(1000) if i % 3  == 0 or i % 5 == 0]
  print sum(mulOf3n5), mulOf3n5[0]


s = time.time()
clacMulof3n5in1000()
e = time.time()
print e - s

