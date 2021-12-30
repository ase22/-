import collections

from collections import Counter

# 문제 잘못 이해하고 푼 풀이
def removeDuplicateLetters(letters):
  charList = []
  result = ''

  if not letters or type(letters) != type('hi'):
    return letters

  for char in letters:
    if char not in charList:
      charList.append(char)

  charList.sort()

  for char in charList:
    result += char

  return result
print(removeDuplicateLetters('cbacdcbc'))

# 예시 풀이 1. 스택을 이용한 풀이
def ex1(letters):
  counter, seen, stack = Counter(letters), set(), []

  for char in letters:
    counter[char] -= 1
    
    if char in seen:
      continue

    # 뒤에 붙일 문자가 남아있다면 스택에서 제거
    while stack and char < stack[-1] and counter[stack[-1]] > 0:
      seen.remove(stack.pop())
    stack.append(char)
    seen.add(char)
  
  return ''.join(stack)

print(ex1('fasdfas'))

# 예시풀이로 풀어보았다.
def practice(str):
  counter, seen, stack = collections.Counter(str), set(), []

  for char in str:
    counter[char] -= 1
    
    if char in seen:
      continue

    while stack and char < stack[-1] and counter[stack[-1]] > 0:
      seen.remove(stack.pop())
    seen.add(char)
    stack.append(char)

  return ''.join(stack)
