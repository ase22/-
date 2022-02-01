import collections

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

# 첫 번째 시도 실패
class Solution:
  def invertBinaryTree(self, root):
    arr = []

    queue = collections.deque([root])

    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        arr.append(node)

        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)

    a = [elem.value for elem in arr]

# 두 번째 시도 성공
class Solution2:
  def invertBinaryTree(self, root):
    queue = collections.deque([root])
    arr = []

    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        if not node:
          continue

        node.left, node.right = node.right, node.left
        arr.append(node.value)

        queue.append(node.left)
        queue.append(node.right)

    return arr

root = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

s= Solution2()

print(s.invertBinaryTree(root))

# 예시 풀이 1. 파이썬다운 방식
class ex1:
  def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
      root.left, root.right = \
        self.invertTree(root.right), self.inverTree(root.left)
      return root
    return None

# 지금까지 재귀 문제를 꽤 많이 풀어봤다. 이제는 어느 정도 직관이 쌓여야 한다. 이 정도면 재귀로 접근하면 풀릴 것 같다는 직관이 생겨야 한다. 우리가 수학 문제를 풀이하는 것도 비슷하다.

# 음수라는 존재가 과연 직관적인가? 자연에 음수라는 개념이 존재하는가? " 나에게 사과가 -5개 있다." 를 일상에서 표현할 수 있는가? 10개든 100개든 양수는 얼마든지 표현할 수 있지만 -5개는 표현할 수 없다. 음수는 일상에서 표현할 수 있는 직관적인 수가 아니다. 그러나 -5가 어떤 의미인지는 초등학생도 잘 알고, 자연스럽게 사용한다. 수많은 선각자들이 만들어 낸 규칙을 후대에 교육을 통해 꾸준히 학습한 결과다.

# 마찬가지로, 재귀도 당장은 직관적이지 않겠지만 꾸준히 학습하면 자연스럽게 직관이 생겨난다. 그것이 바로 우리가 꾸준히 공부하는 이유며, 알고리즘을 공부하는 이유다. 궁극적으로 더 좋은 코드를 작성할 수 있는 능력이다.

# 예시 풀이 2. 반복 구조로 BFS
class ex2:
  def invertTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])

    while queue:
      node = queue.popleft()

      # 부모 노드부터 하향식 스왑
      if node:
        node.left, node.right = node.right, node.left

        queue.append(node.left)
        queue.append(node.right)

    return root

# 예시 풀이 3. 반복   구조로 DFS
class ex3:
  def invertTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
      node = stack.pop()

      # 부모 노드부터 하향식 스왑
      if node:
        node.left, node.right = node.right, node.left

        stack.append(node.left)
        stack.append(node.right)

    return root

# 예시 풀이 4. 반복 구조로 DFS 후위 순회
class ex3:
  def invertTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
      node = stack.pop()

      # 부모 노드부터 하향식 스왑
      if node:
        stack.append(node.left)
        stack.append(node.right)

        node.left, node.right = node.right, node.left

    return root