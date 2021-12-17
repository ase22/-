import time
t1 = time.time()


nums = [2, 7, 11, 15]
target = 26

# 1. 브루트 포스(Brute-Force) 방법, 무차별 대입 방식, 비효율적인 방법
def FindTwoNumbers(numList, targetNumber):
  for i in range(len(numList)):
    for j in range(1, len(numList)):
      if numList[i] + numList[j] == targetNumber:
        return [i, j]

# print(FindTwoNumbers(nums, target))

# 2. in을 이용한 탐색
def FindTwoNumbers2(numList, targetNumber):
  for i in range(len(numList)):
    secondNumber = targetNumber - numList[i]

    if secondNumber in numList[i + 1:]:
      return [i, numList.index(secondNumber)]

def twoSum(nums, target):
  for i, n in enumerate(nums):
    complement = target - n
    if complement in nums[i + 1:]:
      return nums.index(n), nums[i + 1:].index(complement) + (i + 1)

# print(twoSum(nums, target))

#in의 시간 복잡도는 O(n)이므로 전체 시간 복잡도는 이전과 동일한 O(n^2)이지만 in이 훨씬 가볍다.

# 3. 딕셔너리를 활용한 풀이 시간복잡도 O(n)
def twoSum2(nums, target):
  nums_dict = {}

  for i, num in enumerate(nums):
    second_number = target - num

    if second_number in nums_dict:
      return i, nums_dict[second_number]
    nums_dict[num] = i

# print(twoSum2(nums, target))

# 4. 투포인터를 활용한 풀이, 시간복잡도 O(n)
def twoSum3(nums, target):
  # nums.sort() # 투포인터를 활용하기 위해서는 수가 오름차순 정렬되어있어야 한다. 그러나 이렇게 하면 인덱스가 뒤죽박죽으로 섞이게 되므로 원래의 인덱스를 구하기가 어려워진다.
  left, right = 0, len(nums) - 1

  while left != right:
    two_sum = nums[left] + nums[right]

    if two_sum > target:
      right -= 1
    elif two_sum < target:
      left += 1
    else:
      return left, right

print(twoSum3(nums, target));

t2 = time.time()

duration = t2 - t1
print(duration, '초')