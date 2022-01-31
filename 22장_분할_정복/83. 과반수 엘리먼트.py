# 과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라.
import collections

elements = [1, 4, 1, 3]

# 내 풀이
class Solution:
  def getMajorityElement(self, elements):
    counter = collections.Counter(elements)

    return max(counter)

# 예시 풀이 1. 브루트 포스로 과반수 비교
# 앞에서부터 하나씩 과반수를 넘는지 일일이 체크하다가 과반수를 넘으면 바로 정답 처리
# 시간초과로 타임아웃 발생
# 원인: nums에는 중복해서 같은 값이 들어가 있는데 이 값들을 순회하면서 이미 해당 값이 몇개가 이 nums에 들어있는지를 계산했는데도 다시 계산을 
# 하게되므로 불필요한 시간이 소요되기 때문이다.
class ex1:
  def majorityElement(self, nums: list[int]) -> int:
    for num in nums:
      if nums.count(num) > len(nums) // 2:
        return num

# 예시 풀이 2. 다이나믹 프로그래밍
# 디폴트값이 0인 딕셔너리를 하나 만든 후 nums를 순회하면서 num을 키값으로 가지게 한 후 value가 0이면 count메서드로 개수 센 후 저장하고 바로 과반수인지 판별한다.
# 같은 값이 들어왔을 때 다시 해당 요소의 개수를 계산하는게 아니라 이전에 저장해놨던 자료를 활용하기 때문에 시간 요소가 적다.
class ex2:
  def majorityElement(self, nums: list[int]) -> int:
    counts = collections.defaultdict(int)

    for num in nums:
      if counts[num] == 0:
        counts[num] = nums.count(num)
      
      if counts[num] > len(nums) // 2:
        return num


# 예시 풀이 3. 분할 정복
# 우아한 풀이
# elements = [1, 4, 1, 3]일때 1이 안나온다.
class ex3:
  def majorityElement(self, nums: list[int]) -> int:
    if not nums:
      return None
    
    if len(nums) == 1:
      return nums[0]
    
    half = len(nums) // 2

    a = self.majorityElement(nums[:half])
    b = self.majorityElement(nums[half:])

    return [b, a][nums.count(a) > half]

ex3 = ex3()
print(ex3.majorityElement(elements))

# 예시 풀이 4. 파이썬다운 방식
# 과반수가 넘는 숫자는 배열 안에서 중간값이어야 한다.
class ex4:
  def majorityElement(self, nums):
    return sorted(nums)[len(nums) // 2]
