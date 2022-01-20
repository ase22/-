import collections

n, courses = 2, [[0, 1], [3, 4]]

# 풀이 실패
def make_plan(n, courses):
  plan = collections.defaultdict(list)

  for a, b in range(courses):
    plan[a].append(b)
  
  def dfs(a):
    if a not in plan:
      return True
    return False
  
  dfs(1)

  
# 예시 풀이 1. DFS로 순환 구조 판별
def canFinish(numCourses, prerequisites):
  graph = collections.defaultdict(list)

  # 그래프 구성
  for x, y in prerequisites:
    graph[x].append(y)
  
  traced = set()

  def dfs(i):
    # 순환 구조이면 False
    if i in traced:
      return False
    
    traced.add(i)
    
    for y in graph[i]:
      if not dfs(y):
        return False
    # 탐색 종료 후 순환 노드 삭제
    traced.remove(i)

    return True

  # 순환 구조 판별
  for x in list(graph):
    if not dfs(x):
      return False
  
  return True

# print(canFinish(n, courses))

def practice(prerequisites):
  dict = collections.defaultdict(list)

  for x, y in prerequisites:
    dict[x].append(y)
  
  traced = set()

  def dfs(i):
    if i in traced:
      return False
    
    traced.add(i)
    
    for a in dict[i]:
      if not dfs(a):
        return False
    
    traced.remove(i)

    return True
  
  for i in list(dict):
    if not dfs(i):
      return False

  return True


def practice2(prerequisites):
  graph = collections.defaultdict(list)

  for x, y in prerequisites:
    graph[x].append(y)
  
  traced = set()

  def dfs(i):
    if i in traced:
      return False
    
    traced.add(i)

    for j in graph[i]:
      if not dfs(j):
        return False

    traced.remove(i)

    return True
  
  for i in list(graph):
    if not dfs(i):
      return False
  
  return True

# 예시 풀이 2. 가지치기를 이용한 최적화
# 한 번 방문했던 노드를 저장하기 위한 visited라는 별도의 set() 집합 변수를 만든다.
# 이미 방문했던 노드라면 더 이상 진행하지 않고 True를 리턴한다.
def canFinish2(prerequisites):
  graph = collections.defaultdict(list)

  for x, y in prerequisites:
    graph[x].append(y)

  traced = set()
  visited = set()

  def dfs(i):
    # 순환 구조이면 False
    if i in traced:
      return False
    # 이미 방문했던 노드이면 True
    if i in visited:
      return True
    
    traced.add(i)

    for y in graph[i]:
      if not dfs(y):
        return False
    
    # 탐색 종료 후 순환 노드 삭제
    traced.remove(i)
    # 탐색 종료 후 방문 노드 추가
    visited.add(i)

    return True

  # 순환 구조 판별
  print(list(graph))
  for x in list(graph):
    if not dfs(x):
      return False
  
  return True

print(canFinish2(courses))

def practice3(prerequisites):
  graph = collections.defaultdict(list)

  for x, y in prerequisites:
    graph[x].append(y)
  
  traced = set()
  visited = set()

  def dfs(i):
    if i in traced:
      return False
    
    if i in visited:
      return True
    
    traced.add(i)

    for y in graph[i]:
      if not dfs(y):
        return False

    traced.remove(i)
    visited.add(i)

    return True
  
  for i in list(graph):
    if not dfs(i):
      return False
  
  return True

