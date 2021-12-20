nums = [-1, 0, 1, 2, 2, 3, -1, -4, 5]

# 1. 내 풀이 2시간정도 걸림, 틀림
def sumOfThreeNumber(nums):
  myNumbers = nums
  myNumbers.sort()
  results = []

  left, right = 0, len(myNumbers) - 1
  
  while left < right:
    sumOfTwo = myNumbers[left] + myNumbers[right]

    if -sumOfTwo in myNumbers and myNumbers.index(-sumOfTwo) != right and myNumbers.index(-sumOfTwo) != right :
      results.append([myNumbers[left], -sumOfTwo, myNumbers[right]])
      if myNumbers[left] == myNumbers[left + 1] and myNumbers[right] == myNumbers[right - 1]:
        left += 2
        right -= 2
      else:
        left += 1
        right -= 1
    elif -sumOfTwo > myNumbers[right - 1]:
      left += 1
    elif -sumOfTwo < myNumbers[right - 1]:
      right -= 1

  return myNumbers, results

print(sumOfThreeNumber(nums))

# 브투르 포스로 계산

def threeSum(nums):
  results = []
  nums.sort()

  #브루트 포스 n^3 반복
  for i in range(len(nums) - 2):
    #중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i - 1]:
      continue
    for j in range(i + 1, len(nums) - 1):
      if j > i + 1 and nums[j] == nums[j - 1]:
        continue
      for k in range(j + 1, len(nums)):
        if k > j + 1 and nums[k] == nums[k - 1]:
          continue
        if nums[i] + nums[j] + nums[k] == 0:
          results.append((nums[i], nums[j], nums[k]))
  
  return results

# 투 포인터로 합 계산
# 오름차순으로 정렬해준다.
# 일단 제일 첫번째 숫자는 for문으로 index = 0부터 index = len(nums) - 3까지 돌리는데,
# 이 for문 안에서 left와 right가 각 i마다 투포인터로 돼서 sum = 0인 숫자쌍을 찾는다.
# 이때 중복숫자를 거르는게 중요한데, 우선 i부터 중복숫자를 걸러준 후
# while 문에서 left가 right 만날때 까지 돌리면서, sum > 0 , sum < 0, sum == 0인 경우 각각 작성한다.
# sum > 0 인 경우는 더 작아져야 하므로 right -= 1
# sum < 0 인 경우는 더 커져야 하므로 left += 1
# sum == 0 인 경우는 일단 results에 넣고 중복숫자를 걸러주기 위해서 while문에서 만약 3이 3개 있다면 마지막 3까지 이동시켜준다.
# 그리고 나서 right -= 1, left += 1 해주면 새로운 두 숫자가 된다.

def threeSum2(nums):
  results = []
  nums.sort()

  for i in range(len(nums) - 2):
    # 중복된 값 건너뛰기
    if i > 0 and nums[i] == nums[i - 1]:
      continue

    # 간격을 좁혀가며 sum 계산
    left, right = i + 1, len(nums) - 1
    
    while left < right:
      sum = nums[i] + nums[left] + nums[right]

      if sum > 0:
        right -= 1
      elif sum < 0:
        left += 1
      else:
        results.append((nums[i], nums[left], nums[right]))

        while left < right and nums[left] == nums[left + 1]:
          left += 1
        while left < right and nums[right] == nums[right - 1]:
          right -= 1
        left += 1
        right -= 1

  return results

print(threeSum2(nums))