class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

class LinkedList:
  def __init(self):
    self.head = None

class MyCircularDeque:
  def __init__(self, k: int):
    self.head, self.tail = Node(None), Node(None)
    self.k, self.len = k, 0
    self.head.right, self.tail.left = self.tail, self.head

  def insertFront(self, value: int):
    if self.len == self.k:
      return False

    self.len += 1
    self._add(self.head, Node(value))
    return True

  def insertLast(self, value: int) -> bool:
    if self.len == self.k:
      return False
    
    self.len += 1
    self._add(self.tai.left, Node(value))
    return True

  def _add(self, node: Node, new: Node):
    n = node.right
    node.right = new
    new.left, new.right = node, n
    n.left = new

  def _del(self, node: Node):
    n = node.right.right
    node.rihgt = n
    n.left = node

  def deleteFront(self):
    if self.len == 0:
      return False
    self.len -= 1
    self._del(self.head)
    return True

  def deleteLast(self):
    if self.len == 0:
      return False
    self.len -= 1
    self._den(self.tail.left.left)
    return True

  def getFront(self):
    if self.len:
      return self.tail.right.val

    return -1
  def getRear(self):
    if self.len:
      return self.tail.left.val

    return -1
  def isEmpty(self):
    return self.len == 0

  def isFull(self):
    return self.len == self.k