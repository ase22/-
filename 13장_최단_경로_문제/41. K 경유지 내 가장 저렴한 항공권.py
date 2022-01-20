# 시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라. 경로가 존재하지 않을 경우 -1을 리턴한다.
# 전에 구현했던 다익스트라 알고리즘을 가져와서 수정한다.

# 추가해야할 기능들
# 1. 도착점
# 2. K개 경유지 이내 도착
# 3. 경로가 존재하지 않을 경우 -1 리턴
import collections
import heapq

n = 3
edges = [
  [0, 1, 100],
  [1, 2, 100],
  [0, 2, 500]
]
src, dst, k = 0, 2, 0

def cheapestTicket(n, edges, src, dst, k):
  graph = collections.defaultdict(list)

  for u, v, w in edges:
    graph[u].append((v, w))
  
  dist = collections.defaultdict(list)
  Q = [(0, src)]
  count = -1

  while Q:
    price, node = heapq.heappop(Q)

    if node == dst:
      if count <= k:
        return price
      count = -1
      
    if node not in dist:
      dist[node] = price

      for v, w in graph[node]:
        alt = price + w
        count += 1
        heapq.heappush(Q, (alt, v))
  
  return -1

print(cheapestTicket(n, edges, src, dst, k))


# 예시 풀이 1. 다익스트라 알고리즘 응용
# 큐에 추가할 때 K 이내일 때만 경로를 추가해서 K를 넘어서는 경로는 더 이상 탐색되지 않게 하면 된다.
def findCheapestPrice(n, flights, src, dst, K):
  graph = collections.defaultdict(list)

  for u, v, w in flights:
    graph[u].append((v, w))

  k = 0
  Q = [(0, src, K)]

  while Q:
    price, node, k = heapq.heappop(Q)

    if node == dst:
      return price

    if k >= 0:
      for v, w in graph[node]:
        alt = price + w
        heapq.heappush(Q, (alt, v, k - 1))
  
  return -1

print(findCheapestPrice(n, edges, src, dst, k))