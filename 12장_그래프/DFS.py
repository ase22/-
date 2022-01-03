graph = {
  1: [2, 3, 4],
  2: [5],
  3: [5],
  4: [],
  5: [6, 7],
  6: [],
  7: [3]
}

# 1. 재귀를 이용한 DFS(깊이 우선 탐색) 구현
def recursive_dfs(v, discovered = []):
  discovered.append(v)

  for w in graph[v]:
    if w not in discovered:
      discovered = recursive_dfs(w, discovered)

  return discovered

# print(recursive_dfs(1))

# 2. 스택을 이용한 반복 구조로 구현
def iterative_dfs(start_v):
  discovered = []
  stack = [start_v]

  while stack:
    v = stack.pop()

    if not v in discovered:
      discovered.append(v)

      for w in graph[v]:
        stack.append(w)

  return discovered

# print(iterative_dfs(1))

def practice_stack_dfs(start_v):
  stack = [start_v]
  discovered = []

  while stack:
    v = stack.pop()

    if not v in discovered:
      discovered.append(v)

      for w in graph[v]:
        stack.append(w)
  
  return discovered

def practice2_stack_dfs(start_v):
  discovered = []
  stack = [start_v]

  while stack:
    v = stack.pop()

    if v not in discovered:
      discovered.append(v)

      for w in graph[v]:
        stack.append(w)
  
  return discovered
  