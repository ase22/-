# 배열 nums가 주어졌을 때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

import collections


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# 내 풀이 - 브루트 포스
class Solution:
  def slidingWindow(self, nums, K):
    if len(nums) < k:
      return -1

    result = []

    for i in range(len(nums) - K + 1):
      arr = []

      for j in range(i, i + K):
        arr.append(nums[j])

      result.append(max(arr))

    return result

# 예시 풀이 1. 브루트 포스로 계산
# 내가 푼 대로 for문으로 풀었지만 파이썬의 특징인 배열 분할 기법으로 배열을 계쏙 생성하지 않고 for문을 1개로 줄였다.
class ex1:
  def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    if not nums:
      return nums

    result = []

    for i in range(len(nums) - k + 1):
      result.append(max(nums[i:i + k]))

    return result

# 큐를 이용한 최적화
# 슬라이딩윈도우를 한칸씩 움직이는건 무조건 해야하는 부분이므로 최적화가 어렵다.
# 따라서 해당 슬라이딩 윈도우 내 요소의 최댓값을 구하는 부분을 최적해보자.
class ex2:
  def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
    if not nums:
      return nums

    result = []
    current_max = float('-inf')
    dict = collections.deque([])

    for i in range(len(nums)):
      dict.append(nums[i])

      if i < k - 1:
        continue;

      # 슬라이딩 윈도우를 한 칸 이동할 때 새롭게 들어온 값이 기존의 최댓값보다 큰 경우에 최대값을 새로운 값으로 갱신한다.
      if current_max == float('-inf'):
        current_max = max(dict)
      elif current_max < nums[i]:
        current_max = nums[i]

      result.append(current_max)

      # 기존의 최댓값이 한칸 움직이기 전에 맨 처음 인덱스에 있던 값이라면 다시 현재 최대값을 -값으로 초기화시켜준다.
      if current_max == dict.popleft():
        current_max = float('-inf')

    return result

ex2 = ex2()
print(ex2.maxSlidingWindow(nums, k))



