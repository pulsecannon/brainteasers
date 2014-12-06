def solution(M, N):
  if M > N and N > 648:
    return None

  start = M
  end = N
  andProduct = M
  while (start + 1) <= end:
    start += 1
    print start, andProduct
    andProduct = andProduct & start

  return andProduct


if __name__ == '__main__':
  print solution(5, 7)
