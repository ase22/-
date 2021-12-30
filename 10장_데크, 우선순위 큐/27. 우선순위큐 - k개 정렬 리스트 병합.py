import heapq
class Node:
  def __init__(self, value):
    self.val = value
    self.next = None

class LinkedList:
  def __init(self):
    self.head = None

def mergeKLists(self, lists):
  root = result = Node(None)
  heap = []

  # 각 연결 리스트의 루트를 힙에 저장
  for i in range(len(lists)):
    if lists[i]:
      heapq.heappush(heap, (lists[i].val, i, lists[i]))
  
  # 힙 추출 이후 다음 노드는 다시 저장
  while heap:
    node = heapq.heappop(heap)
    idx = node[1]
    result.next = node[2]
  
    result = result.next

    if result.next:
      heapq.heappush(heap, (result.next.val, idx, result.next))
    
  return root.next