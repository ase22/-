# 힙은 트리구조인데 트리 중에서도 부모 노드의 값이 이 부모의 모든 자식보다 작은 이진트리이다.
# 이 규칙만 지키면 되는게 힙이다.
# 힙이 활용되는 분야: 다익스트라 알고리즘 구현에 우선순위 큐을 사용해서 O(V^2) -> O(ElogV)로 줄어들었다.

# 1. 삽입
  # 큐에 삽입하는 순서는 다음과 같다.
    # 1. 가장 밑줄의 가장 왼쪽 빈 노드에 삽입할 노드를 삽입한다.
    # 2. 부모와 값 크기 비교를 하면서 부모보다 더 작으면 부모와 값을 바꾼다.
    # 3. 부모가 더 큰 값일 때까지 반복한다.

# 2. 추출
  # 큐를 추출하는 순서는 다음과 같다.
    # 1. 우선 가장 위에 있는 부모 노드를 추출해야 한다.
    # 2. 추출하면 맨 위 노드가 비게 되는데 여기에 큐의 가장 마지막 노드를 넣는다.
    # 3. 맨 위 노드와 이 노드의 자식 노드 2개와 크기를 비교하면서 작으면 교체하면서 재귀 수행한다.
class BinaryHeap(object):
  def __init__(self):
    self.items = [None]

  def __len__(self):
    return len(self.items) - 1

  # 삽입 시 실행, 반복 구조 구현, 내부함수: _ 사용
  def _percolate_up(self):
    i = len(self)
    parent = i // 2

    while parent > 0:
      if self.items[i] < self.items[parent]:
        self.items[parent], self.items[i] = self.items[i], self.items[parent]

      i = parent
      parent = i // 2

  def insert(self, k):
    self.items.append(k)
    self._percolate_up()

  # 추출 시 실행, 재귀 구조로 구현
  def _percolate_down(self, index):
    left = index * 2
    right = index * 2 + 1
    smallest = index

    if left <= len(self) and self.items[left] < self.items[smallest]:
      smallest = left

    if right <= len(self) and self.items[right] < self.items[smallest]:
      smallest = right

    # 위 if문에서 부모 노드가 자식 노드보다 컸으면 smallest에 새로운 값이 할당되기 때문에 smallest != index인 상황이 된다.
    if smallest != index:
      # 노드간에 값을 교체한다.
      self.items[index], self.items[smallest] = self.items[smallest], self.items[index]
      # 교체 후 다시 교체된 값의 인덱스값을 인자로 넣어서 재귀 수행한다.
      self._percolate_down(smallest)

  def extract(self):
    extracted = self.items[1]
    self.items[1] = self.items[len(self)]
    self.items.pop()
    self._percolate_down(1)

    return extracted

