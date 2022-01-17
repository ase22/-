# 동일한 값을 지닌 가장 긴 경로를 찾아라.

class TreeNode:
  def __init__(self, val = 0):
    self.value = val
    self.left = None
    self.right = None

# 내 풀이
# 이전 문제의 가장 긴 경로 구하는 문제를 이용해서 부모 노드와 자식 노드의 값을 비교한다.
# 3가지 경우로 나눠서 자식 노드 둘 다 부모와 같은 경우, 왼쪽만 같은 경우, 오른쪽만 같은 경우 이렇게 나누었다.
class Solution:
  longest: int = 0
  # 내 풀이

  def longestUnivaluePath(self, root) -> int:
    def dfs(node: TreeNode) -> int:
      if not node:
        return -1

      left = dfs(node.left)
      right = dfs(node.right)

      if node.left and node.right and node.value == node.left.value and node.value != node.right.value:
        self.longest = max(self.longest, left + 1)

      if node.right and node.left and node.value != node.left.value and node.value == node.right.value:
        self.longest = max(self.longest, right + 1)

      if node.right and node.left and node.value == node.left.value and node.value == node.right.value:
        self.longest = max(self.longest, left + right + 2)

      return max(left, right) + 1

    dfs(root)

    return self.longest

root = TreeNode(1)
n2 = TreeNode(4)
n3 = TreeNode(5)
n4 = TreeNode(4)
n5 = TreeNode(4)
n6 = TreeNode(5)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

# 예시 풀이 1. 상태값 거리 계산 DFS
class Solution:
  result: int = 0

  def longestUnivaluePath(self, root: TreeNode) -> int:
    def dfs(node: TreeNode):
      if node is None:
        return 0

      # 존재하지 않는 노드까지 DFS 재귀 탐색
      left = dfs(node.left)
      right = dfs(node.right)

      # 현재 노드가 자식 노드와 동일한 경우 거리 1 증가
      if node.left and node.left.val == node.val:
        left += 1
      else:
        left = 0

      if node.right and node.right.val == node.val:
        right += 1
      else:
        right = 0

      # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과
      self.result = max(self.result, left + right)
      # 자식 노드 상태값 중 큰 값 리턴
      return max(left, right)

    dfs(root)

    return self.result
