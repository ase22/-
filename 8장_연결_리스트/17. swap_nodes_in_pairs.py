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

Llist1.head.next = Node2
Node2.next = Node3
Node3.next = Node4

# 풀이 1. 노드 값 스왑
def swapNodesInPairs(head):
  node = head #head객체의 참조값이 node에 입력됨

  while node:
    node.val, node.next.val, next = node.next.val, node.val, node.next.next
    node = next #node변수는 node.next.next의 참조값을 가리키게 된다. head는 바뀌지 않는다.

  return head

# swapNodesInPairs(Llist1.head)

# print(Llist1.head,Llist1.head.val, Llist1.head.next.val, Llist1.head.next.next.val, Llist1.head.next.next.next.val)

# 풀이 2. 반복 구조로 스왑
# node 대신 root.next를 리턴하는 이유: 
# print(Llist1.head.val, Llist1.head.next.val, Llist1.head.next.next.val)
def swapPairs(head):
  root = prev = Node('')
  prev.next = head

  while head and head.next:
    b = head.next
    head.next = b.next 
    b.next = head

    prev.next = b

    head = head.next # 해드를 가리키는 노드가 직접 바뀌는 풀이라서 head를 리턴하지 못한다.
    prev = prev.next.next

  return root.next # head 이전 값을 root로 별도 설정한 후 root.next를 리턴한다.

# swapPairs(Llist1.head)

# 풀이 3. 재귀 구조로 스왑
# 1. base condition에서 올바른 결과가 나오게 하기
# 2. 재귀 식 찾기
# 3. 이전 단계의 함수는 올바르게 작동한다고 가정하기
def swapPairs2(head):
  if head and head.next:
    p = head.next

    # 스왑된 값 리턴 받음
    head.next = swapPairs2(p.next)
    p.next = head
    return p
  
  return head

print(swapPairs2(Llist1.head).next.val)
def practice(head):
  if head and head.next:
    p = head.next

    head.next = practice(p.next)
    p.next = head
    return p
  
  return head

