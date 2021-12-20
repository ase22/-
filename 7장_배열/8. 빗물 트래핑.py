from typing import List
import time

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# 인덱스 = 0에서부터 시작하는 for문 작성
# left, right = 0, 2
# count = 0

# while 
# if left + 1 <= right and height[left] <= height[right] and height[left] > 0:
#   for i in range(left + 1, right):
#     if height[left] > height[i]:
#       count += height[i] - height[left]
#   left += 1
#   right += 1

# else:
#   right += 1

# 내 풀이, 대략 1시간 소요
left = 0
right = len(height) - 1
count = 0
history_dic = {}

while left != right:
  if height[left] == height[right] and height[left] > 0:
    for i in range(left + 1, right):
      if height[i] < height[left]:
        count += height[left] - height[i]
        height[i] = height[left]
    left += 1
    right -= 1
  elif height[left] < height[right]:
    left += 1
  elif height[left] > height[right]:
    right -= 1

# print(count)

# 2. 투포인터 이용 예시답안 O(n)
# 투 포인터에 해당하는 빗물양의 최대값을 계속 갱신시키면서 현재 포인터와의 차이를 volume에 더해주는 방식이다.
# 이렇게 하면 한번 빗물이 부어진 위치는 다시 생각할 필요가 없어진다.
def trap(height: List[int]) -> int:
  if not height:
    return None

  volume = 0
  left, right = 0, len(height) - 1
  left_max, right_max = height[left], height[right]

  while left < right:
    left_max, right_max = max(height[left], left_max), max(height[right], right_max)
    # 더 높은 쪽을 향해 투 포인터 이동
    if left_max <= right_max:
      volume += left_max - height[left]
      left += 1
    else:
      volume += right_max - height[right]
      right -= 1

  return volume

  def trap1Myself(height):
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    volume = 0;

    while left < right:
      left_max = max(height[left], left_max)
      right_max = max(height[right], right_max)

      if height[left] <= height[right]:
        volume += left_max - height[left]
        left += 1
      else:
        volume += right_max - height[right]
        right -= 1
    
    return volume


# print(trap(height))

# 3. 스택 쌓기 O(n)

def trap2(height: List[int]) -> int:
  stack = []
  volume = 0

  for i in range(len(height)):
    #변곡점을 만나는 경우
    while stack and height[i] > height[stack[-1]]:
      #스택에서 꺼낸다
      top = stack.pop()

      if not len(stack):
        break
      
      # 이전과의 차이만큼 물 높이 처리
      distance = i - stack[-1] - 1
      waters = min(height[i], height[stack[-1]]) - height[top]

      volume += distance + waters

    stack.append(i)
  return volume
print(trap2(height))


