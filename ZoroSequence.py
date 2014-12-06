import sys

zeroSq = []
def getSeq(initseq, nextNum, seqLen):
  if int(nextNum) < seqLen:
    getSeq(initseq + '+' + nextNum, str(int(nextNum) + 1), seqLen)
    getSeq(initseq + '-' + nextNum, str(int(nextNum) + 1), seqLen)
  else :
    if eval(initseq + '+' + str(seqLen)) == 0:
      zeroSq.append(initseq + '+' + str(seqLen))
    if eval(initseq + '-' + str(seqLen)) == 0:
      zeroSq.append(initseq + '-' + str(seqLen))


if __name__ == '__main__':
  import time
  s = time.time()
  getSeq('1', '2', int(sys.argv[1]))
  e = time.time()
  print zeroSq, e-s

