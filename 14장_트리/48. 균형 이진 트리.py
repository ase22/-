# 이진 트리가 높이 균형인지 판단하라.
# 높이 균형은 모든 노드의 서브 트리 간의 높이 차가 1 이하인 것을 말한다.
class Solution:
  def isBanalnced(self, root):
    def check(root):
      if not root:
        return 0

      left = check(root.left)
      right = check(root.right)

      # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
      if left == -1 or \
        right == -1 or \
          abs(left - right) > 1:
        return -1
      return max(left, right) + 1

    return check(root) != -1

class practice:
  def isBalanced(self, root):
    def check(node):
      if not node:
        return 0

      left = check(node.left)
      right = check(node.right)

      # node = None 노드일 때 0을 리턴한 후, abs(left - right)에서 통과돼서 -1을 리턴하면 그 이후로는 위 노드와 상관없이 노드의 높이차이가 1을 초과하는 상황이므로 left == 1 or right == 1 조건을 추가해서 -1을 리턴하도록 한다.
      if abs(left - right) > 1 or left == -1 or right == -1:
        return -1
      # 그 외의 경우 높이를 left,right 중 높은 쪽 + 1을 해서 해당 노드의 맨 밑까지의 높이를 구한걸 리턴한다.
      return max(left, right) + 1
    # check(root)결과가 -1이 아닌 경우가 모든 노드의 높이차가 1초과가 아닌 상황이므로 -1이 아니면 True를 리턴하게 한다.
    return check(root) != -1




