import collections
myString = 'bcb'

# 내 풀이
# 문자열 순서대로 중복되지 않은 경우에 카운트를 더해주다가,
# 중복된 문자가 나오면 dict를 초기화한 후 해당 문자부터 다시 새로운 최대 부분문자열의 길이를 찾는 함수
def longestString(myStr):
  dict = collections.defaultdict(int)
  max_count = 0
  count = 0

  for char in myStr:
    if dict[char] != 1:
      dict[char] += 1
      count += 1

    elif dict[char] == 1:
      max_count = max(max_count, count)
      dict = collections.defaultdict(int)
      dict[char] += 1
      count = 1

  print(max_count)

longestString(myString)

# 예시 풀이 1. 슬라이딩 윈도우와 투 포인터로 사이즈 조절
def longestString2(myStr):
  used = {}
  max_length = start = 0

  for index, char in enumerate(myStr):
    # 이미 등장했던 문자라면 'start' 위치 갱신
    # start는 슬라이딩 윈도우 내에서 같은 문자가 나왔을 경우에는 start는 used[char] + 1을 해줘야 중복을 포함하지 않고 새롭게 문자열을 받을 수 있다.
    if char in used and start <= used[char]: 
      start = used[char] + 1
    else: # 최대 부분 문자열 길이 갱신
      max_length = max(max_length, index - start + 1)

  # 현재 문자의 위치 삽입
    used[char] = index

  return max_length

def practice(string):
  used = {}
  max_length = start = 0

  for index, char in enumerate(string):
    if char in used and start <= used[char]:
      start = used[char] + 1
    else:
      max_length = max(max_length, index - start + 1)

    used[char] = index
  
  return max_length

def practice2(str):
  used = {}
  max_length = start = 0

  for index, char in enumerate(str):
    if char in used and start <= used[char]:
      start = used[char] + 1
    else:
      max_length = max(max_length, index - start + 1)
    
    used[char] = index
  
  return max_length