if __name__ == '__main__':
  size = raw_input()
  initElements = raw_input()
  operation = raw_input()
  element = raw_input()

  queue = initElements.split()

  if len(queue) > size:
    print 'Size and num of initial elements dont match'

  if operation == '1':
    queue.append(element)
    print ' '.join(queue)
  elif operation == '0':
    try:
      queue.remove(element)
      print ' '.join(queue)
    except ValueError:
      print 'element not in queue'
  else:
    print 'Invalid operation'
