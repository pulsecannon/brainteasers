C = {0:' ', 1:'-', 2:'+'}

def base3(N,M):
  R = [0]*M
  while N:
    R[M-1] = N%3
    N/=3
    M-=1
  R = map(lambda x: C[x], R)
  return R

def mix(A, B):
  R = str(A[0])
  for i in xrange(len(B)):
    R += B[i] + str(A[i+1])
  return R

def process(N):
  X = range(1,N+1)
  for i in xrange(3**(N-1)):
    Y = mix(X, base3(i,N-1))
    if eval(Y.replace(' ', '')) == 0:
      print Y

def main():
  while True:
      X = raw_input()
      try:
          N = int(X)
      except:
          break
      process(N)

if __name__ == '__main__':
  main()


