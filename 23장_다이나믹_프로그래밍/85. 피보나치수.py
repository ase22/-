import collections

class Solution:
  def fib(self, n):
    if n == 1 or n == 0:
      return n

    return self.fib(n-1) + self.fib(n - 2)

# 예시 풀이 1. 메모이제이션
# 다이나믹 프로그래밍의 하향식 풀이법
# 클래스에 dp딕셔너리 만들고 여기에 값을 넣어뒀다가 필요할 때 사용하는 방법
class ex1:
  def __init__(self):
    self.dp = collections.defaultdict(int)

  def fib(self, n):
    if n <= 1:
      return n

    if self.dp[n]:
      return self.dp[n]

    self.dp[n] = self.fib(n - 1) + self.fib(n - 2)

    return self.dp[n]

# 예시 풀이 2. 타뷸레이션
# 다이나믹 프로그래밍의 상향식 풀이법(작은걸 미리 계산한 후 큰거로 가는 방식)
class ex2:
  def __init__(self):
    self.dp = collections.defaultdict(int)

  def fib(self, N):
    self.dp[0], self.dp[1] = 0, 1

    if N <= 1:
      return N

    for i in range(2, N + 1):
      self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

    return self.dp[N]

# 예시 풀이 3. 두 변수만 이용해 공간 절약
# 딕셔너리 사용 안하고 변수 두 개만 이용해서 풀이
# 시간복잡도 O(n)으로 매우 효율적이다.
class ex3:
  def fib(self, N):
    x, y = 0, 1

    for i in range(0, N):
      x, y = y, x + y
    
    return x

# 예시 풀이 4. 행렬 이용
# 시간복잡도 O(log n)으로 더 빠르다.
# 선형대수 관저에서 행렬의 n승을 계산하는 방식
# 넘파이 모듈을 사용한다.
class ex4:
  def fib(self, n):
    M = np.matrix([[0, 1] [1, 1]])
    vec = np.array([[0], [1]])

    return np.matmul(M ** n, vec)[0]

