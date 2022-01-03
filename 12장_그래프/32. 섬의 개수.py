graph = {
  1: [2, 3, 4],
  2: [5],
  3: [6],
  4: [7],
  5: [],
  6: [],
  7: [8],
  8: [9],
  9: []
}

graph2 = {
  1: [2, 3, 4],
  2: [],
  3: [],
  4: [],
  5: [6],
  6: [],
  7: []
}

# 내 풀이
def numberOfIslands(start_v):
  island_count = 0
  discovered = []
  stack = [start_v]

  while stack:
    v = stack.pop()

    if v not in discovered:
      discovered.append(v)

      for w in graph2[v]:
        stack.append(w)
  
  island_count += 1

  for i in range(start_v, len(graph2) + 1):
    if i not in discovered:
      island_count += numberOfIslands(i)
      break

  return island_count

print(numberOfIslands(1))

grid = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [1, 1, 0, 1, 1]
]
# 예시 풀이 1
# 키포인트: dfs가 끝난 곳의 값을 0으로 바꿔주는 것 -> 한번 거친곳에 오면 return해주기 위해서
def numIslands(grid):
  def dfs(i, j):
    # 더 이상 땅이 아닌 경우 종료
    if i < 0 or i >= len(grid) or \
      j < 0 or j >= len(grid[0]) or \
      grid[i][j] != 1:
        return
    
    grid[i][j] = 0

    # 8방향 탐색
    dfs(i + 1, j) # 이 dfs가 끝나고 나면 그리드의 모든 값은 0이 된다.
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)
    dfs(i + 1, j + 1)
    dfs(i + 1, j - 1)
    dfs(i - 1, j + 1)
    dfs(i - 1, j - 1)

  count = 0
  
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == 1:
        dfs(i, j) # dfs를 하는데 계속 dfs가 이루어지면서 모든 1이 0이 된다면 count += 1이 된 이후로 grid[i][j] == 0이기 때문에 count = 1에서 끝나지만 dfs가 끝났는데 1이 남아있으면 해당 dfs가 진행된 이후 또한번 count += 1이 이루어진다.

        # 모든 육지 탐색 후 카운트 1 증가
        count += 1

  return count

print(numIslands(grid))