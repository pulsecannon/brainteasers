import sys


START_CHAR = 'M'
END_CHAR = '*'
TREE_CHAR = 'X'
EMPTY_CHAR = '.'


def getInitialData(forest):
  start = end = None
  emptyLocations = []
  for x, row in enumerate(forest):
    try:
      start = (x, row.index(START_CHAR))
    except ValueError:
      pass
    try:
      end = (x, row.index(END_CHAR))
    except ValueError:
      pass
    emptyLocations.append(
      (x, i) for i, el in enumerate(row) if el == EMPTY_CHAR)
  return start, end, emptyLocations

def getNext

def findPath(start, end, emptyLocs):
  path = []
  start


def main(filename):
  inputFile = open(filename, 'r')
  forest = [line.split() for line in inputFile.read().split('\n')]
  start, end, emptyLocs = getInitialData(forest)
  if start and end and emptyLocs:
    findPath(start, end, emptyLocs)
  else:
    print "Invalid Input, start = %s, end = %s" %(start, end)


if __name__ == '__main__':
  main(sys.argv[1])
