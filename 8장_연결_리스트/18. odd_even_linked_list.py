class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

class Llist:
  def __init__(self):
    self.head = None

Llist1 = Llist()
Llist1.head = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Llist1.head.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

# 내 풀이
# 포인터는 한 노드씩 건너가고 노드의 next노드를 두칸 뒤 노드로 한다.
# 포인터가 마지막 노드까지 가서 while문을 빠져오면 해당 노드의 next노드를 첫 번째 짝수번 째 노드로 지정한다.
# 첫 번째 짝수 노드는 처음 while문을 돌 때 참조값을 secondNode 변수에 넣어주었다.
def oddEvenLinkedList(head):
  prev = Node('')
  prev.next = head
  secondNode = Node('')

  count = 0

  while head and head.next:
    next, head.next = head.next, head.next.next
    head = next
    
    if count == 0:
      secondNode = next
    
    count += 1

  head.next = secondNode
  return prev.next

# n1 = oddEvenLinkedList(Llist1.head)
# print(n1.val, n1.next.val, n1.next.next.val, n1.next.next.next.val, n1.next.next.next.next.val)

# 예시 풀이1. 반복 구조로 홀짝 노드 처리
def oddEvenList(head):
  # 예외 처리
  if head is None:
    return None
  
  odd = head
  even = head.next
  even_head = head.next

  #반복하면서 홀짝 노드 처리
  while even and even.next:
    odd.next, even.next = odd.next.next, even.next.next
    odd, even = odd.next, even.next
  
  #홀수 노드의 마지막을 짝수 헤드로 연결
  odd.next = even_head
  return head

# h1 = oddEvenList(Llist1.head)
# print(h1.val, h1.next.val, h1.next.next.val, h1.next.next.next.val, h1.next.next.next.next.val)
