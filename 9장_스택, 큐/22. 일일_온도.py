T = [73, 74, 75, 71, 69, 72, 76, 73]
result = []

# 못풀었다.
def Temperature(tempList):
  for i in range(len(T)):
    count = 0

    for j in range(i + 1, len(T)):
      if T[i] < T[j]:
        count += 1
        result.append(count)
        break

      count += 1

  return result

# 예시 풀이1 스택 값 비교
def dailyTemperatures(T):
  answer = [0] * len(T)
  stack = []
  
  for i, cur in enumerate(T):
    #현재 온도가 스택 값보다 높다면 정답 처리
    while stack and cur > T[stack[-1]]:
      last = stack.pop()
      answer[last] = i - last
    stack.append(i)
  
  return answer
print(dailyTemperatures(T));


def practice(T):
  stack = []
  answer = [0] * len(T)

  for index, curTemp in enumerate(T):
    while stack and curTemp > T[stack[-1]]:
      last = stack.pop() # pop은 stack의 마지막 요소를 빼내기 때문에 이 특성을 이용한 while문 풀이법이다.
      answer[last] = index - last
    stack.append(index)
  
  return answer