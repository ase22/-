# 딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다. 1개인 엘리먼트를 찾아라.

import collections

nums = [2, 2, 1]

# collections.Counter로 개수 센 후 값이 1인 키값 추출
class Solution:
  def singleNumber(self, nums):
    a = collections.Counter(nums)

    number = [a[number] for number in a if a[number] == 1]

    return number.pop()

s = Solution()

print(s.singleNumber(nums))

# 예시 풀이 1. XOR 풀이
class ex1:
  def singleNumber(self, nums: list[int]) -> int:
    result = 0
    
    for num in nums:
      result ^= num
    
    return result

