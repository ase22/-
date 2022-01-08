import itertools

n, k = 4, 2

# 내 풀이
# elements의 길이가 k일 때 results에 넣고 탈출
# dfs함수는 한 칸씩 전진하기 위해 index 받음
def combinations(n, k):
  results = []
  prev_elements = []

  def dfs(index, elements):
    if len(elements) == k:
      results.append(elements)
      return

    for i in range(index, n + 1):
      prev_elements.append(i)
      new_elements = prev_elements[:]
      dfs(i + 1, new_elements)

      prev_elements.pop()
  
  dfs(1, [])

  return results

print(combinations(n, k))

# 예시 풀이 1. DFS로 k개 조합 생성
def combine(n, k):
  results = []

  def dfs(elements, start, k):
    if k == 0:
      results.append(elements[:])
      return

    # 자신 이전의 모든 값을 고정하여 재귀 호출
    for i in range(start, n + 1):
      elements.append(i)
      dfs(elements, i + 1, k - 1)
      elements.pop()

  dfs([], 1, k)

  return results

print(combine(n, k))

# 예시 풀이 2. itertools 모듈 사용
def combine2(n, k):
  return list(map(list, itertools.combinations(range(1, n + 1), k)))
print(combine2(n, k))