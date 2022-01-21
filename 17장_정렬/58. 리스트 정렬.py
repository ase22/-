# 연결 리스트를 O(n log n)에 정렬하라.
class LinkedList:
  def __init__(self):
    self.head = None

class Node:
  def __init__(self, val):
    self.next = None
    self.value = val

llist = LinkedList()

llist.head = Node(4)
n2 = Node(2)
n3 = Node(1)
n4 = Node(3)

llist.head.next = n2
n2.next = n3
n3.next = n4

class Solution:
  # 내 풀이
  # 리스트의 값을 배열에 저장한 후 오름차순으로 정렬하고 링크드 리스트에 순서대로 할당하는 방법
  def sortLinkedList(self, head):
    node_value_list = []
    node = head
    node2 = head

    while head:
      node_value_list.append(head.value)
      head = head.next
    
    node_value_list.sort()

    for i in range(len(node_value_list)):
      if node:
        node.value = node_value_list[i]
        node = node.next
    
    print(node2.value, node2.next.value, node2.next.next.value, node2.next.next.next.value)

# s = Solution()
# s.sortLinkedList(llist.head)

# 예시 풀이 2. 병합 정렬
class ex1:
  def mergeTwoLists(self, l1: Node, l2: Node) -> Node:
    if l1 and l2:
      if l1.value > l2.value:
        l1, l2 = l2, l1
      l1.next = self.mergeTwoLists(l1.next, l2)

    return l1 or l2
  
  def sortList(self, head: Node) -> Node:
    if not (head and head.next):
      return head
    
    # 런너 기법 활용
    half, slow, fast = None, head, head

    while fast and fast.next:
      half, slow, fast = slow, slow.next, fast.next.next

    half.next = None

    # 분할 재귀 호출
    l1 = self.sortList(head)
    l2 = self.sortList(slow)

    return self.mergeTwoLists(l1, l2)

# 예시 풀이 2. 내장 함수를 이용하는 실용적인 방법
class ex2:
  def sortList(self, head: Node) -> Node:
    # 연결 리스트 -> 파이썬 리스트
    p = head
    lst: list = []
    
    while p:
      lst.append(p.value)
      p = p.next

    # 정렬
    lst.sort()

    # 파이썬 리스트 -> 연결 리스트
    p = head
    
    for i in range(len(lst)):
      p.val = lst[i]
      p = p.next
    
    return head
    



