candidates = [2, 3, 5]
target = 8

n = 4
k = 2

# 내 풀이
# 조합 구현 알고리즘을 응용해서 풀었다.
def sum_combination(candidates, target):
  results = []
  prev_elements = []

  def dfs(index, elements, csum):
    if csum == 0:
      results.append(elements)
      return

    if csum < 0:
      return

    for i in range(index, len(candidates)):
      prev_elements.append(candidates[i])
      new_elements = prev_elements[:]

      csum -= candidates[i]
      dfs(i, new_elements, csum)
      prev_elements.pop()
      csum += candidates[i]

  dfs(0, [], target)

  return results

# DFS로 중복 조합 그래프 탐색
def combinationSum(candidates, target):
  result = []

  def dfs(csum, index, path):
    # 종료 조건
    if csum < 0:
      return
    
    if csum == 0:
      result.append(path)
      return
    
    # 자신부터 하위 원소까지의 나열 재귀 호출
    for i in range(index, len(candidates)):
      dfs(csum - candidates[i], i, path + [candidates[i]])

  dfs(target, 0, [])

  return result

print(combinationSum(candidates, target))