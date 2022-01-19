# 이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라. 즉 다음과 같은 트리는 [1, 2, 3, null, null, 4, 5] 형태로 직렬화할 수 있을 것이다.

#    1
#   / \
#  2   3
#     / \
#    4   5

import collections
import queue

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

class Solution:
  def getDepth(self, root):
    queue = collections.deque([root])
    depth = 0

    while queue:
      depth += 1
      for _ in range(len(queue)):
        node = queue.popleft()

        if node.left:
          queue.append(node.left)

        if node.right:
          queue.append(node.right)

    return depth

  def serialize(self, root):
    serialized_tree = []

    queue = collections.deque([root])
    depth = 0

    while queue:
      depth += 1

      for _ in range(len(queue)):
        node = queue.popleft()

        if node.left:
          serialized_tree.append(node.left.value)
          queue.append(node.left)
        elif node.left == None and depth != self.getDepth(root):
          serialized_tree.append('null')

        if node.right:
          serialized_tree.append(node.right.value)
          queue.append(node.right)
        elif node.right == None and depth != self.getDepth(root):
          serialized_tree.append('null')

    return serialized_tree

  # 풀이 실패
  def deserialize(self, serialized_tree):
    k = 1

    for i, value in enumerate(serialized_tree):
      node = TreeNode(value)
      node.left = TreeNode(serialized_tree[i + k])
      node.right = TreeNode(serialized_tree[i + k + 1])

  # deserialize 예시풀이
  def ex1(self, data: str) -> TreeNode:
    # 예외 처리
    if data == '# #':
      return None

    nodes = data.split()

    root = TreeNode(int(nodes[1]))
    queue = collections.deque([root])
    index = 2

    while queue:
      node = queue.popleft()

      if node:
        if nodes[index] != '#':
          node.left = TreeNode(nodes[index])
          queue.append(node.left)
          index += 1

        if nodes[index] != '#':
          node.right = TreeNode(nodes[index])
          queue.append(node.right)
          index += 1

    return root

root1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)

root1.left = n2
root1.right = n3
n3.left = n4
n3.right = n5

s = Solution()
print(s.serialize(root1))
