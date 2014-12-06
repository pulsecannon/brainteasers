class MinO1(object):
  stack = []
  minstack = []

  def push(self, num):
    self.stack.append(num)
    if self.minstack:
      if num <= self.minstack[-1]:
        self.minstack.append(num)
    else:
      self.minstack.append(num)

  def top(self):
    return self.stack[-1]

  def pop(self):
    num = self.stack.pop()
    if num == self.minstack[-1]:
      self.minstack.pop()
    return num

  def getMin(self):
    if self.minstack:
      return self.minstack[-1]
    return 'notfound'
