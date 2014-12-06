def solution(A):
  lenOfA = len(A)
  if lenOfA > 10000000:
    raise Exception('Array Too long.')

  if sum(A) > 0:
    raise Exception('Array dosen\'t sum to zero')

  num = lenOfA / 2
  while num >= 0 and num < lenOfA:
    if sum(A[:num]) == sum(A[num:]):
      return num
    elif sum(A[:num]) > sum(A[num:]):
      num += 1
    elif sum(A[:num]) < sum(A[num:]):
      num -= 1


if __name__ == '__main__':
  print solution([1,2,-3])
