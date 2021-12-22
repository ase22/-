# 연결리스트(linked list) 구현 방법 및 팰린드롬 구현
# 예시풀이 1 연결리스트를 이용한 풀이
import collections
from typing import Collection, Deque


class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

LList = LinkedList()
LList.head = Node(1)
Node2 = Node(2)
Node3 = Node(2)
Node4 = Node(1)
LList.head.next = Node2
Node2.next = Node3
Node3.next = Node4

def isPalindrome(head) -> bool:
  q: list = [];

  if not head:
    return True
  
  node = head
  #리스트 변환
  while node is not None:
    q.append(node.val)
    node = node.next

  #펠린드롬 판별
  while len(q) > 1:
    if q.pop(0) != q.pop():
      return False
    
  return True

print(isPalindrome(LList.head))

# 예시풀이 2. 데크를 이용한 최적화
# 동적 배열로 구성된 리스트: 맨 앞 아이템을 가져오기에 적합한 자료형이 아니다.
# 왜? pop을 하면 리스트 특성상 shifting이 일어나는데 이때 시간복잡도는 O(n)이 발생하기 때문이다.
# 따라서 pop할 때 시간복잡도를 줄일 수 있는 자료형이 필요, => Deque
# Deque는 이중(양방향) 연결 리스트라서 양쪽 방향 모두 추출시 O(n)이다.
def isPalindrome2(head):
  q = collections.deque

  if not head:
    return True
  
  node = head

  while node != None:
    q.append(node.val)
    node = node.next
  
  while len(q) > 1:
    if q.popleft() != q.pop():
      return False
    
  return True

# print(isPalindrome2(LList.head))

# 예시풀이 3. 런너를 이용한 풀이
# 런너가 제대로된 팰린드롭 풀이법이다.
def isPalindrome3(head):
  rev = None
  slow = fast = head
  # 런너를 이용해 역순 연결 리스트 구성
  while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
  if fast:
    slow = slow.next

  # 팰린드롬 여부 확인
  while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next
  return not rev
# fast러너가 완주를 했을 때 slow러너는 코스 반만큼까지 달린 상태
# 이 상태가 첫 번째 while문을 진행한 후 상태이다.
# 두 번째 while문에서는 slow러너가 나머지 코스를 완주할 때 rev와 같은 값인지를 따지는 코드이다.
# 팰린드롬이라면 중앙에서 양쪽을 비교했을 때 대칭이어야 하고, slow는 중앙에 위치한 상태이고 rev는 slow러너의 역순을 가지고 있으므로 slow러너의 나머지 코스와 rev의 정방향 코스는 같은 값을 가진다.

print(isPalindrome3(LList.head))

# 파이썬의 다중 할당
# 파이썬은 다중 할당시 값과 나눠서 할당할 시의 값이 다르다.
# rev, rev.next, slow = slow, rev, slow.next
# 와
# rev, rev.next = slow, rev
# slow = slow.next
# 는 rev = slow 부분에서 동일참조가 일어나서 서로 같은 값을 참조하게 된다. 파이썬 특징.