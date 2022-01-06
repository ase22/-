import itertools
# 서로 다른 정수를 입력받아 가능한 모든 수열을 리턴하라.
input = [1, 2, 3]

# 풀이 실패
def permutations(input):
  result = []
  input_length = len(input)
  
  def dfs(index, number_list):
    if input_length == len(number_list):
      result.append(number_list)
      return

    for i in range(index, len(input)):
      number_list.append(input[i])
      dfs(i + 1, number_list)

  dfs(0, [])
  return result

# 예시 풀이 1
def permute(nums):
  results = []
  prev_elements = []

  def dfs(elements):
    # 리프 노드일 때 결과 추가
    if len(elements) == 0:
      results.append(prev_elements[:])

    # 순열 생성 재귀 호출
    for e in elements:
      next_elements = elements[:]
      next_elements.remove(e)

      prev_elements.append(e)
      dfs(next_elements)
      prev_elements.pop()
  
  dfs(nums)

  return results

# print(permute(input))

def permute2(nums):
  return list(map(list, itertools.permutations(nums)))
  
# print(permute2(input))

def practice(nums):
  results = []
  prev_elements = []

  def dfs(elements):
    if len(elements) == 0:
      results.append(prev_elements)
    
    for e in elements:
      next_elements = elements[:]
      next_elements.remove(e)

      prev_elements.append(e)
      dfs(next_elements)
      prev_elements.pop()
  
  dfs(nums)

  return results

# 파이썬은 모든 데이터가 객체다. 숫자, 문자 포함
# 숫자, 문자: 불변 객체

# 참조가 되지 않도록 값 자체를 복사하는 방법
# 1. [:]로 처리 
# 2. d = a.copy()

# 복잡한 리스트의 경우에는 copy.deepcopy()로 처리해야 한다.
# import copy
# a = [1, 2, [3, 5], 4]
# b = copy.deepcopy(a)
