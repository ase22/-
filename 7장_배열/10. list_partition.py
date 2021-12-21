nums = [1, 4, 3, 2, 5, 6]

def maxSum(nums):
  nums.sort(reverse = True)
  sum = 0
  
  for i in range(len(nums) // 2):
    sum += min(nums[2 * i], nums[2 * i + 1])
  
  return sum

# print(maxSum(nums))

# 1. 첫 번째 풀이
# 페어를 담는 리스트를 만들고 이 리스트의 길이가 2가 되면 sum에 더하는 구조
# 이 풀이대로 출력하면 숫자 개수가 홀수인 경우에는 최대값을 얻을 수 없다.
def ex1(nums):
  sum = 0
  pair = []
  nums.sort()

  for n in nums:
    pair.append(n)
    if len(pair) == 2:
      sum += min(pair) # min 메서드에는 배열도 올 수 있다.
      pair = [] # 배열 초기화

  return sum

# print(ex1(nums))

# 2. 짝수 번째 값 계산
# 역시 숫자가 홀수개일 경우 잘못된 값이 나온다.
def ex2(nums):
  sum = 0
  for i in range(len(nums) // 2):

    sum += nums[2 * i]
  
  return sum

# print(ex2(nums))

# 3. 파이썬다운 방식
def ex3(nums):
  return sum(sorted(nums)[::2])

print(ex3(nums))