class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

class Llist:
  def __init__(self):
    self.head = None

#첫 번째 링크드 리스트
Llist1 = Llist()
Llist1.head = Node(2)
Node12 = Node(4)
Node13 = Node(3)

Llist1.head.next = Node12
Node12.next = Node13

#두 번째 링크드 리스트
Llist2 = Llist()
Llist2.head = Node(5)
Node22 = Node(6)
Node23 = Node(4)

Llist2.head.next = Node22
Node22.next = Node23

def reverseList(head):
    node, prev = head, None

    while node:
      next, node.next = node.next, prev
      prev, node = node, next
    
    return prev

def sumTwoLlistToNumber(head1, head2):
  node1 = reverseList(head1)
  node2 = reverseList(head2)
  
  number1 = ''
  number2 = ''

  while node1 and node2:
    number1 += str(node1.val)
    number2 += str(node2.val)

    node1, node2 = node1.next, node2.next
  
  numberString = str(int(number1) + int(number2))
  
  return numberString

def toReversedLinkedList(numberString):
  prev = None

  for element in numberString:
    node = Node(element)
    node.next = prev
    prev = node

  return prev
# toReversedLinkedList(sumTwoLlistToNumber(Llist1.head, Llist2.head))

def addTwoNumber(l1, l2):
  num1 = 0
  num2 = 0
  index = 0

  while l1:
    num1 += l1.val * (10**index)
    l1 = l1.next
    index += 1
  
  index = 0

  while l2:
    num2 += l2.val * (10**index)
    l2 = l2.next
    index += 1
  
  numberString = str(num1 + num2)

  prev = None

  for number in numberString:
    node = Node(number)
    node.next = prev
    prev = node

  print(node.val, node.next.val, node.next.next.val)
  
addTwoNumber(Llist1.head, Llist2.head)

def practice(l1, l2):
  num1 = 0
  num2 = 0
  index = 0

  while l1:
    num1 += l1.val * (10**index)
    l1 = l1.next
    index += 1
  
  index = 0
  
  while l2:
    num2 += l2.val * (10**index)
    l2 = l2.next
    index += 1
  
  numberString = str(num1 + num2)

  prev = None

  for number in numberString:
    node = Node(number)
    node.next = prev
    prev = node
  
  return node







