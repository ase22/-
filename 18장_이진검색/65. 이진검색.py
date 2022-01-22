# 정렬된 nums를 입력받아 이진 검색으로 targt에 해당하는 인덱스를 찾아라.

from audioop import bias
import bisect


nums = [-1, 0, 3, 5, 9, 12]
target = 9

class TreeNode:
  def __init__(self, val):
    self.value = val
    self.left = None
    self.right = None

root = TreeNode(5)
n2 = TreeNode(0)
n3 = TreeNode(9)
n4 = TreeNode(-1)
n5 = TreeNode(3)
n6 = TreeNode(12)

root.left = n2
root.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

# 풀이 실패
class Solution:
  def __init__(self):
    self.depth = 0

  def binarySearch(self, root, target):
    if root == None:
      return None

    self.depth += 1

    if root.value > target and root.left != None:
      self.binarySearch(root.left, target)

    if root.value < target and root.right != None:
      self.binarySearch(root.right, target)

    if root.value == target:
      return self.depth

# 예시 풀이 1. 재귀 풀이
class ex1:
  def search(self, nums: list[int], target: int) -> int:
    def binary_search(left, right):
      if left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
          return binary_search(mid + 1, right)
        elif nums[mid] > target:
          return binary_search(left, mid - 1)
        else:
          return mid

      else:
        return -1

    return binary_search(0, len(nums) - 1)

class practice1:
  def search(self, nums, target):
    def binary_search(left, right):
      if left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
          binary_search(mid + 1, right)
        elif nums[mid] < target:
          binary_search(left, mid - 1)
        else:
          return mid

      else:
        return -1

    return binary_search(0, len(nums) - 1)

# 예시 풀이 2. 반복 풀이
class ex2:
  def search(self, nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
      mid = (left + right) // 2

      if nums[mid] < target:
        left = mid + 1
      elif nums[mid] > target:
        right = mid - 1
      else:
        return mid

    return -1

class practice2:
  def search(self, nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
      mid = (left + right) // 2

      if nums[mid] < target:
        left = mid + 1
      elif nums[mid] > target:
        right = mid - 1
      else:
        return mid

    return -1

# 예시 풀이 3. 이진 검색 모듈
# 파이썬은 이진 검색 알고리즘을 지원하는 bisect모듈을 기본으로 제공한다.
class ex3:
  def search(self, nums, target):
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
      return index
    else:
      return -1

class practice4:
  def search(self, nums, target):
    index = bisect.bisect_left(nums, target)

    if index <= len(nums) - 1 and nums[index] == target:
      return index
    else:
      return -1

# 예시 풀이 4. 이진 검색을 사용하지 않는 index 풀이
# 파이썬에서 제공하는 해당 값의 인덱스를 찾아내는 index() 메소드를 활용
# index() 메소드는 존재하지 않는 값을 넣으면 에러가 발생하므로 ValueError를 예외처리해서 -1을 리턴하도록 한다.

class ex4:
  def search(self, nums, target):
    try:
      return nums.index(target)
    except ValueError:
      return -1

s = ex4()
print(s.search(nums, target))