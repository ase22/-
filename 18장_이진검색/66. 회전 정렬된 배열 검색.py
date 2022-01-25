# 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target값의 인덱스를 출력하라.

nums, target = [4, 5, 6, 7, 0, 1, 2], 1

# 풀이 실패
class Solution:
  def search(self, nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
      mid = left + (right - left) // 2

      if nums[mid] > target:
        right = mid - 1
      elif nums[mid] < target:
        left = mid + 1
      else:
        return mid
    
    return -1
  
  def find_rotate_count(self, nums):
    index1 = nums.index(nums[0])
    sortedIndex = nums.sorted()
    
    index2 = sortedIndex.index(nums[0])

    return index1 - index2

# 예시 풀이 1. 피벗을 기준으로 한 이진검색
class ex1:
  def search(self, nums: list[int], target: int) -> int:
    # 예외 처리
    if not nums:
      return -1
    
    # 최솟값을 찾아 피벗 설정
    left, right = 0, len(nums) - 1

    while left < right:
      mid = left + (right - left) // 2

      if nums[mid] > nums[right]:
        left = mid + 1
      else:
        right = mid
    
    pivot = left

    # 피벗 기준 이진 검색
    left, right = 0, len(nums) - 1

    while left <= right:
      mid = left + (right - left) // 2
      mid_pivot = (mid + pivot) % len(nums)

      if nums[mid_pivot] < target:
        left = mid + 1
      elif nums[mid_pivot] > target:
        right = mid - 1
      else:
        return mid_pivot
    
    return -1

ex1 = ex1()

print(ex1.search(nums, target))
  

