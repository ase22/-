import collections
import math
nodes = [3, 9, 20, None, None, 15, 7]

# 내 풀이
# 이진트리에 최대로 들어갈 수 있는 노드수를 깊이가 점점 커지면서 해당 깊이에 해당하는 최대 노드수보다 nodes의 길이가 크면 depth를 증가시키는 알고리즘
def maximumDepth(nodes):
  size = len(nodes)
  depth = 1
  e = 1

  while True:
    if size > e:
      e = e + math.pow(2, depth)
      depth += 1
    else:
      return depth

# print(maximumDepth(nodes))

# 예시 풀이 1. 반복 구조로 BFS 풀이
# DFS는 스택으로, BFS는 큐를 사용해서 구현한다.
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

root = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
# n4 = TreeNode(None)
# n5 = TreeNode(None)
n6 = TreeNode(15)
n7 = TreeNode(7)

root.left = n2
root.right = n3
n3.left = n6
n3.right = n7

class Solution:
  def maxDepth(self, root):
    if root is None:
      return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
      depth += 1
      # 큐 연산 추출 노드의 자식 노드 삽입
      for _ in range(len(queue)):
        cur_root = queue.popleft()

        if cur_root.left:
          queue.append(cur_root.left)

        if cur_root.right:
          queue.append(cur_root.right)

    # BFS 반복 횟수 == 깊이
    return depth
    
s = Solution()

print(s.maxDepth(root))

class Practice:
  def maxDepth(self, root: TreeNode) -> int:
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
a = Practice()
a.maxDepth(root)

