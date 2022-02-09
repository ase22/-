# 정렬되지 않은 배열에서 K번째 큰 요소를 추출하라.

import collections
import heapq
from json.encoder import INFINITY


nums = [1, 2, 3, 4, 5, 6]
k = 4

# 풀이 실패
class Solution:
  def getKthElement(self, nums):
    heap = heapq.heappush([None])
    
    answer = -INFINITY
    count = 0

    for i in range(len(nums)):
      heap.heappush(nums[i])
    
    while count < k:
      popped = heap.heappop()

      if answer < popped:
        answer = popped
        count += 1

    return answer

# 예시 풀이 1. heapq 모듈 이용
class ex1:
  def findKthLargest(self, nums: list[int], k: int) -> int:
    heap = list()

    for n in nums:
      heapq.heappush(heap, -n)

    for _ in range(k - 1):
      heapq.heappop(heap)
    
    return -heapq.heappop(heap)

# 예시 풀이 2. heapq 모듈의 heapify 이용
# 위 처럼 nums를 순회하면서 push할 필요 없이 한번에 가능하게 해준다.
class ex2:
  def findKthLargest(self, nums, k):
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
      heapq.heappop(nums)
    
    return heapq.heappop(nums)

# 예시 풀이 3. heapq 모듈의 nlargest 이용
# nlargest는 n번째 큰 값을 추출하는 함수다.
class ex3:
  def ex3(self, nums, k):
    return heapq.nlargest(k, nums)[-1]

# 그냥 정렬 sort 이용해서 풀이
class ex4:
  def ex4(self, nums, k):
    return sorted(nums, reverse=True)[k - 1]

print(ex4().ex4(nums, k))
