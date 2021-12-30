class MyCircularQueue:
  def __init__(self, k):
    self.queue = [None] * k
    self.maxlen = k
    self.front = 0
    self.rear = 0

    #enQueue(): 리어 포인터 이동
    def enQueue(self, value):
      if self.queue[self.rear] is None:
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.maxlen
        return True
      else:
        return False
    
    #deQueue(): 프론트 포인터 이동
    def deQueue(self):
      if self.queue[self.front] is None:
        return False
      else:
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.maxlen
        return True
    
    def Front(self):
      if self.queue[self.front] == None:
        return -1
        
      return self.queue[self.front]
    
    def Rear(self):
      if self.queue[self.rear - 1] == None:
        return -1

      return self.queue[self.rear - 1]
    
    def isEmpty(self):
      if len(self.queue) == 0:
        return True

      return False
    
    def isFull(self):
      if self.front == self.rear and self.queue[self.front] != None:
        return True

      return False

    

    
