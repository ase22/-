# 다음의 기능을 제공하는 해시맵을 디자인하라.
# put(key, value): 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트한다.
# get(key): 키에 해당하는 값을 조회한다. 만약 키가 존재하지 않는다면 -1을 리턴한다.
# remove(key): 키에 해당하는 키, 값을 해시맵에서 삭제한다.

# 개별 체이닝 방식

import collections

class Node:
  def __init__(self, key=None, value=None):
    self.val = value
    self.key = key
    self.next = None

class MyHashMap:
  def __init__(self):
    self.size = 1000
    self.table = collections.defaultdict(Node)

  def put(self, key, value):
    index = key % self.size

    if self.table[index].value is None:
      self.table[index] = Node(key, value)
      return
    
    p = self.table[index]
    while p:
      if p.key == key:
        p.value = value
        return
      
      if p.next == None:
        break

      p = p.next
      p.next = Node(key, value)
  
  def get(self, key):
    index = key % self.size
    p = self.table[index]

    while p:
      if p.key == key:
        return p.val
      p = p.next

    return -1
  
  def remove(self, key):
    index = key % self.size

    if self.table[index].val == None:
      return

    p = self.table[index]
    
    # 인덱스의 첫 번째 노드일 때 삭제 처리
    if p.key == key:
      self.table[index] = Node() if p.next is None else p.next
      return

    # 연결 리스트 노드 삭제
    prev = p
    while p:
      if p.key == key:
        prev.next = p.next
        return
      prev, p = p, p.next


