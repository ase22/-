import time
nums = [1, 2, 3, 4]

def multipyExceptMe(nums):
  results = []
  
  for i in range(len(nums)):
    result = 1
    for j in range(len(nums)):
      if i == j:
        continue
      result *= nums[j]
    
    results.append(result)
  
  return results

def multiplyExceptMe2(nums):
  results = []
  multyplyAll = 1

  for i in range(len(nums)):
    multyplyAll *= nums[i]
  
  for i in range(len(nums)):
    results.append(multyplyAll // nums[i])
  
  return results

print(multiplyExceptMe2(nums))
print(multipyExceptMe(nums))

# 풀이1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
# 제약사항: 나누기를 하지 않고 O(n)에 풀이해라

def ex(nums):
  out = []
  p = 1
  #왼쪽 곱셈
  for i in range(0, len(nums)):
    out.append(p)
    p = p * nums[i]

  p = 1
  # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
  for i in range(len(nums) - 1, 0 - 1, -1):
    print(i)
    out[i] = out[i] * p
    p = p * nums[i]

  return out

print(ex(nums))

