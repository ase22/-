# BFS는 DFS보다 쓰임새가 적지만, 최단 경로를 찾는 다익스트라 알고리즘 등에 매우 유용하게 쓰인다.
# BFS는 재귀로 구현할 수 없다.

graph = {
  1: [2, 3, 4],
  2: [5],
  3: [5],
  4: [],
  5: [6, 7],
  6: [],
  7: [3]
}

# 1. 큐를 이용하여 반복 구조로 BFS 구현
def iterative_bfs(start_v):
  discovered = [start_v]
  queue = [start_v]

  while queue:
    v = queue.pop(0) # 큐는 선입선출이라 pop(0)으로 해서 맨 앞 요소를 추출한다.
    
    for w in graph[v]:
      if w not in discovered:
        discovered.append(w)
        queue.append(w)
  
  return discovered

print(iterative_bfs(1))

def practice_queue_bfs(start_v):
  discovered = [start_v]
  queue = [start_v]

  while queue:
    v = queue.pop(0)

    for w in graph[v]:
      if w not in discovered:
        discovered.append(w)
        queue.append(w)
