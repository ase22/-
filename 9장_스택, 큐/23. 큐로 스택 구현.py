import collections

class MyStack:
  def __init__(self):
    self.queue = collections.deque()
    
    def push(self, x):
      self.queue.append(x)

      # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
      for _ in range(len(self.queue) - 1):
        self.queue.append(self.queue.popleft())
      
    def pop(self):
      return self.queue.popleft()
    
    def top(self):
      return self.queue[0]
    
    def empty(self):
      return len(self.queue) == 0

  