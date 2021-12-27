class Node:
  def __init__(self, value):
    self.val = value
    self.next = None


class Llist:
  def __init(self):
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
# 리버스 함수 만들고 안에서 count 수만큼 리버스 한 후에 처음 head값 next 까지 연결한 이후 prev 리턴
def reverseLinkedList(head, m, n):
  if not head or m == n:
    return head

  def reverse(head):
    prev = None
    node = head
    count = 0

    while count <= n - m:
      next, node.next = node.next, prev
      node, prev = next, node
      count += 1

    head.next = next
    return prev

  count = 1
  # 리버스가 수행되기 바로 전 노드를 저장할 node 변수
  node = Node('')

  # 링크드리스트의 첫번째 노드를 저장할 initialNode 변수
  initialNode = Node('')
  initialNode.next = head

  while head:
    if count == m:
      node.next = reverse(head)

    else:
      node = head
      head = head.next

    if count > m:
      return initialNode.next

    count += 1

# n1 = reverseLinkedList(Llist1.head, 2, 4)
# print(n1.val, n1.next.val, n1.next.next.val, n1.next.next.next.val, n1.next.next.next.next.val)

# 예시풀이
def reverseBetween(head, m, n):
  # 예외 처리
  if not head or m == n:
    return head
  
  root = start = Node('')
  root.next = head
  
  #start, end 지정
  for _ in range(m - 1):
    start = start.next
  end = start.next

  # 반복하면서 노드 차례대로 뒤집기
  for _ in range(n - m):
    tmp, start.next, end.next = start.next, end.next, end.next.next
    start.next.next = tmp

  return root.next

n1 = reverseBetween(Llist1.head, 2, 4)
print(n1.val, n1.next.val, n1.next.next.val)

