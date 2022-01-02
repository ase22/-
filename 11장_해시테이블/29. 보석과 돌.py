import collections

J = 'aA'
S = 'aAAbbbb'


# 풀이 1. 해시 테이블을 이용한 풀이
def jewelsAndStones(j, s):
  stones = {}
  count = 0

  for stone in s:
    if stone not in stones:
      stones[stone] = 1
    else:
      stones[stone] += 1

  for jewel in j:
    if jewel in stones:
      count += stones[jewel]

  print(count)

# jewelsAndStones(J, S)

# 풀이 2. defaultdict를 이용한 비교 생략
def jewelsAndStones2(J, S):
  freqs = collections.defaultdict(int)
  count = 0

  # 비교 없이 돌의 빈도 수 계산
  for char in S:
    freqs[char] += 1
  
  # 비교 없이 보석 빈도 수 합산
  for char in J:
    count += freqs[char]

  return count

print(jewelsAndStones2(J, S))

# 풀이 3. Counter로 계산 생략
# Counter는 존재하지 않는 키를 조회할 경우 KeyError를 발생시키는 게 아니라 0을 출력해 주기 때문에 에러에 대한 예외 처리를 할 필요가 없다.
def jewelsAndStones3(J, S):
  freqs = collections.Counter(S)
  count = 0

  for char in J:
    count += freqs[char]

  return count  

# 풀이 4. 파이썬다운 방식: 리스트 컴프리헨션
def jewelsAndStones(J, S):
  return sum(s in J for s in S)


