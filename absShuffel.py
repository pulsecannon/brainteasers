import itertools

def absFun(S):
  maxRes = abs(S[0]-S[1]) + abs(S[1]-S[2]) + abs(S[2]-S[3])
  return maxRes

def solution(A, B, C, D):
  seq = itertools.permutations([A, B, C, D])
  maxSeq = max(seq, key=absFun)
  return absFun(maxSeq)


if __name__ == '__main__':
  print solution(5, 3, -1, 5)
