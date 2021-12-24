class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

Llist = LinkedList()
Llist.head = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Llist.head.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5



# 풀이 1. 재귀 풀이 순서
# 재귀로 풀때 어떻게 풀건지 생각
#   1. 중첩함수 필요성 생각
#   2. 첫 번째 노드는 헤드라서 이전 노드(prev)가 없기 때문에 prev = None으로 초기값 줘야 한다.
#   3. 빠져나오는 조건(다음 노드가 None이면 끝)
#   4. 인자에 뭘 넣고 돌릴건지(다음 노드와 현재 노드)
def reversellist(head):
  def reverse(node, prev = None): # 초기값 지정이 중요함
    if not node: #재귀로 돌다가 node가 None까지 갔을 경우를 재귀에서 빠져나오는 순간으로 설정함
      return prev
    next, node.next = node.next, prev # 현재 노드의 next 노드를 설정하고, 다음 노드를 알려준다.
    return reverse(next, node) # 다음 노드와 현재 노드를 넣는다.
  
  return reverse(head) # 헤드 노드를 넣는다.

# 풀이 2. 반복 구조로 뒤집기
def reverseList(head):
  node, prev = head, None

  while node:
    next, node.next = node.next, prev
    prev, node = node, next
  
  return prev #꼭 prev 리턴 안해도 된다. 

reverseList(Llist.head)

print(Node5.next.next.next.val)
