class Node:
  def __init__(self, value):
    self.val = value
    self.next = None
  

class LinkedList:
  def __init__(self):
    self.head = None

nums1 = [1, 2, 4]
nums2 = [1, 3, 4]

list1 = LinkedList()
list1.head = Node(nums1[0])
l1Node2 = Node(nums1[1])
l1Node3 = Node(nums1[2])
list1.head.next = l1Node2
l1Node2.next = l1Node3

list2 = LinkedList()
list2.head = Node(nums2[0])
l2Node2 = Node(nums2[1])
l2Node3 = Node(nums2[2])
list2.head.next = l2Node2
l2Node2.next = l2Node3

# 예시풀이 1. 재귀 구조로 연결
def mergeTwoLists(list1Node1, list2Node1):
  if (not list1Node1) or (list2Node1 and list1Node1.val > list2Node1.val):
    list1Node1, list2Node1 = list2Node1, list1Node1
  
  if list1Node1:
    list1Node1.next = mergeTwoLists(list1Node1.next, list2Node1)
  
  return list1Node1

mergeTwoLists(list1.head, list2.head)
print(list1.head.val, list1.head.next.val, list1.head.next.next.val, list1.head.next.next.next.val, list1.head.next.next.next.next.val, list1.head.next.next.next.next.next.val)
