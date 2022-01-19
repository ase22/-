# 두 이진 트리를 병합하라. 중복되는 노드는 값을 합산한다.
import collections

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

# 내 풀이
class Solution:
  def mergeTrees(self, root1, root2):
    queue = collections.deque([(root1, root2)])
    root1.value += root2.value

    while queue:
      node1, node2 = queue.popleft()

      if node1.left and node2.left:
        node1.left.value += node2.left.value
        queue.append((node1.left, node2.left))

      if node1.right and node2.right:
        node1.right.value += node2.right.value
        queue.append((node1.right, node2.right))

      if not node1.left and node2.left:
        node1.left = node2.left

      if not node1.right and node2.right:
        node1.right = node2.right

    return root1

root1 = TreeNode(1)
n12 = TreeNode(3)
n13 = TreeNode(2)
n14 = TreeNode(5)

root1.left = n12
root1.right = n13
n12.left = n14

root2 = TreeNode(2)
n22 = TreeNode(1)
n23 = TreeNode(3)
n24 = TreeNode(4)
n25 = TreeNode(7)

root2.left = n22
root2.right = n23
n22.right = n24
n23.right = n25

s = Solution()

print(s.mergeTrees(root1, root2).right.right.value)

# 예시 풀이 1. 재귀 탐색
class ex1:
  def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    if t1 and t2:
      node = TreeNode(t1.val + t2.val)
      node.left = self.mergeTrees(t1.left, t2.left)
      node.right = self.mergeTrees(t1.right, t2.right)

      return node
    else:
      return t1 or t2 # 존재하는 노드를 리턴한다.
