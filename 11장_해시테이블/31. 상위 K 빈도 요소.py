# k번 이상 등장하는 요소를 추출해라
import collections
import heapq
nums = [1, 1, 1, 2, 2, 3]
k = 2

# 내 풀이
def kTimesNumbers(nums):
  count = collections.Counter(nums)
  list = []

  for number in count:
    if count[number] >= k:
      list.append(number)

  print(list)

kTimesNumbers(nums)

# 예시 풀이 1. Counter를 이용한 음수순 추출
def topKFrequent(nums):
  freqs = collections.Counter(nums)
  freqs_heap = []
  
  # 힙에 음수로 삽입
  for f in freqs:
    heapq.heappush(freqs_heap, (-freqs[f], f))
  topk = list()
  # k번 만큼 추출, 최소 힙(Min Heap) 이므로 가장 작은 음수 순으로 추출
  for _ in range(k):
    topk.append(heapq.heappop(freqs_heap)[1])

  return topk

print(topKFrequent(nums))

