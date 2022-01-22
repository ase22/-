import collections
import heapq
# K부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 리턴한다. 입력값 (u, v, w)는 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 N으로 입력받는다.

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
times2 = [
  [3, 1, 5],
  [3, 2, 2],
  [2, 1, 2],
  [3, 4, 1],
  [4, 5, 1],
  [5, 6, 1],
  [6, 7, 1],
  [7, 8, 1],
  [8, 1, 1]
]

N, K = 4, 2

# 1차 풀이 실패
def networkDelayTime(N, K, times):
  path = collections.defaultdict(list[list])

  for x, y, z in times:
    path[x].append([y, z])

  visited = set()

  def dfs(i, time):
    visited.add(i)

    if len(visited) == N:
      return time

    for node in path[i]:
      time += dfs(node[0], time + node[1])

    return time

  return dfs(K, 0)

# 2차 풀이 성공
def networkDelayTime2(N, K, times):
  path = collections.defaultdict(list[list])

  for x, y, z in times:
    path[x].append([y, z])

  visited = set()
  arr = []

  def dfs(i, count):
    if i not in visited:
      visited.add(i)

    if len(visited) == N:
      arr.append(count)
      return

    for node in path[i]:
      dfs(node[0], count + node[1])

    arr.append(count)
    count = 0

  dfs(K, 0)

  return max(arr)

print(networkDelayTime2(8, 3, times2))

# 예시 풀이 1. 다익스트라 알고리즘 구현

# 판별해야 하는 것들
#   1. 모든 노드가 신호를 받는 데 걸리는 시간
#     -> 다익스트라 알고리즘으로 구현 가능
#   2. 모든 노드에 도달할 수 있는지 여부
#     모든 노드의 다익스트라 알고리즘 계산값이 존재하는지 유무로 판별 가능

def networkDelayTime3(times, N, K):
  graph = collections.defaultdict(list)

  # 그래프 인접 리스트 구성
  for u, v, w in times:
    graph[u].append((v, w))

  # 큐 변수: [(소요 시간, 정점)]
  Q = [(0, K)]
  dist = collections.defaultdict(int)

  # 우선순퀴 큐 최솟값 기준으로 정점까지 최단 경로 삽입
  while Q:
    time, node = heapq.heappop(Q)

    if node not in dist:
      dist[node] = time

      for v, w in graph[node]:
        alt = time + w
        heapq.heappush(Q, (alt, v))

  # 모든 노드의 최단 경로 존재 여부 판별
  if len(dist) == N:
    return max(dist.values())

  return -1

# print(networkDelayTime3(times2, 8, 3))

# heapq는 heappop() 할 경우 가장 작은 값이 추출된다.
# heappush

def practice(times, N, K):
  graph = collections.defaultdict(list)

  for u, v, w in times:
    graph[u].append((v, w))

  dist = collections.defaultdict(list)

  Q = [(0, K)]

  while Q:
    time, node = heapq.heappop(Q)

    if node not in dist:
      dist[node] = time
      for v, w in graph[node]:
        alt = time + w
        heapq.heappush(Q, (alt, v))

  if len(dist) == N:
    return max(dist.values())

  return -1

def practice2(times, N, K):
  graph = collections.defaultdict(list)

  for u, v, w in times:
    graph[u].append((v, w))

  dist = collections.defaultdict(list)

  Q = [(0, K)]

  while Q:
    time, node = heapq.heappop(Q)

    if node not in dist:
      dist[node] = time

      for v, w in graph[node]:
        alt = time + w
        heapq.heappush((alt, v))

  if len(dist) == N:
    return max(dist.values())
  return -1


def practice4(times, N, K):
  graph = collections.defaultdict(list)

  for u, v, w in times:
    graph[u].append((v, w))

  dist = collections.defaultdict(list)

  Q = [(0, K)]

  while Q:
    time, node = heapq.heappop(Q)

    if node not in dist:
      dist[node] = time
      for v, w in graph[node]:
        alt = time + w
        heapq.heappush(Q, (alt, v))

  if len(dist) == N:
    return max(dist.values())

print(practice4(times2, 8, 3))