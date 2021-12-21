nums = [7, 1, 5, 3, 6, 4]
import sys
# 간단한 브루트 포스
def myFunc(nums):
  maxProfit = 0;

  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      maxProfit = max(maxProfit, nums[j] - nums[i])
  
  return maxProfit

print(myFunc(nums))

# 예시풀이1. 브루트 포스토 계산
def maxProfit(nums):
  max_price = 0

  for i, price in enumerate(nums):
    for j in range(i, len(nums)):
      max_price = max(nums[j] - price, max_price)

  return max_price
# 더 효율적인 풀이가 필요하다.

# 예시풀이2. 저점과 현재 값과의 차이 계산
def maxProfit2(nums):
  profit = 0
  min_price = sys.maxsize

  # 최솟값과 최대값을 계속 갱신

  for price in nums:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

  return profit
print(maxProfit2(nums))
