# 모든 부분 집합을 리턴하라.
nums = [1, 2, 3]

# 내 풀이
# 이전에 작성한 조합 알고리즘을 이용해서 간단하게 부분 집합 코드를 작성해 보았다.
def combine(nums, k):
  results = []
  prev_element = []

  def dfs(index, elements):
    if len(elements) == k:
      results.append(elements)
      return
    
    for i in range(index, len(nums)):
      prev_element.append(nums[i])
      new_elements = prev_element[:]
      dfs(i + 1, new_elements)

      prev_element.pop()

  dfs(0, [])

  return results

def subsets(nums):
  result = []

  for i in range(0, len(nums) + 1):
    result += combine(nums, i)

  return result

print(subsets(nums))

# 예시 코드 1. 트리의 모든 DFS 결과
def subsets2(nums):
  results = []

  def dfs(index, path):
    # 매번 결과 추가
    results.append(path)

    # 경로를 만들면서 DFS
    for i in range(index, len(nums)):
      dfs(i + 1, path + [nums[i]])

  dfs(0, [])

  return results

print(subsets2(nums))

def practice(nums):
  results = []

  def dfs(index, elements):
    results.append(elements)
  
    for i in range(index, len(nums)):
      dfs(i + 1, elements + [nums[i]])
  
  dfs(0, [])

  return results

print(practice(nums))