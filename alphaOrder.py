def solution(S1, S2):
    seq = 'abcdefghijklmnopqrstuvwxyz'
    s1Sum = 0
    s2Sum = 0
    for s1 in S1:
      s1Sum += seq.find(s1)

    for s2 in S2:
      s2Sum += seq.find(s2)

    if s1Sum > s2Sum:
      return -1
    elif s1Sum == s2Sum:
      return 0
    elif s1Sum < s2Sum:
      return 1
