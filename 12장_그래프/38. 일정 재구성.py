import collections
from typing import Collection


input = [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]
input2 = [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]
# 내 풀이
# 1. dfs로 탐색 전에 dict를 만들고 키값이 0번째 인덱스에 해당하는 값과 1번째 인덱스
# 에 해당하는 값을 가지게 한다.
# 2. dfs함수에서 일단 dfs는 location 문자열 값을 인자로 받고 바로 append 해준다.
# 3. if 문에서 location이 dict의 키값에 없으면 return, 있으면 다음 dfs 실행
# 4. dfs 내에서 return이 되면 dfs는 종료되고 results 리턴되고 끝

def planSchedule(input):
  results = []
  dict = {}

  for i in range(len(input)):
    dict[input[i][0]] = input[i][1]
  
  def dfs(location):
    results.append(location)

    if location not in dict:
      return

    dfs(dict[location])

  dfs('JFK')

  return results

print(planSchedule(input))

# 예시 풀이 1. DFS로 일정 그래프 구성
def findItinerary(tickets):
  graph = collections.defaultdict(list)
  
  # 그래프 순서대로 구성
  for a, b in sorted(tickets):
    graph[a].append(b)

  route = []

  def dfs(location):
    while graph[location]:
      dfs(graph[location].pop(0))
    route.append(location)

  dfs('JFK')

  # 다시 뒤집어 어휘 순 결과로
  return route[::-1]

print(findItinerary(input2))

# 예시 풀이 2. 스택 연산으로 큐 연산 최적화 시도
# 큐 연산은 O(n)이기 때문에 스택연산O(1)로 최적화 개선 필요
# 정렬 시 뒤집어서 정렬하면 pop()으로 스택 사용 가능

def findItinerary2(tickets):
  graph = collections.defaultdict(list)
  for a, b in sorted(tickets, reverse=True):
    graph[a].append(b)
  
  route = []

  def dfs(a):
    # 마지막 값을 읽어 어휘순 방문
    while graph[a]:
      dfs(graph[a].pop())
    route.append(a)

  dfs('JFK')

  # 다시 뒤집어 어휘 순 결과로
  return route[::-1]

# 예시 풀이 3. 일정 그래프 반복
def findItinerary3(tickets):
  graph = collections.defaultdict(list)

  # 그래프 순서대로 구성
  for a, b in sorted(tickets):
    graph[a].append(b)

  route, stack = [], ['JFK']

  while stack:
    # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
    while graph[stack[-1]]:
      stack.append(graph[stack[-1]].pop(0))
    route.append(stack.pop())
  
  # 다시 뒤집어 어휘 순 결과로
  return route[::-1]

tickets = [['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]
print(findItinerary3(tickets))





def practice(tickets):
  dict = collections.defaultdict(list)

  for a, b in sorted(tickets):
    dict[a].append(b)
  
  results = []

  def dfs(a):
    while dict[a]:
      dfs(dict[a].pop(0))
    results.append(a)
  
  dfs('JFK')
  
  return results[::-1]
      
print(practice(tickets))
def findItinerary(tickets):
  graph = collections.defaultdict(list)
  
  # 그래프 순서대로 구성
  for a, b in sorted(tickets):
    graph[a].append(b)

  route = []

  def dfs(location):
    while graph[location]:
      dfs(graph[location].pop(0))
    route.append(location)

  dfs('JFK')

  # 다시 뒤집어 어휘 순 결과로
  return route[::-1]