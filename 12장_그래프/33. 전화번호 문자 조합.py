# 2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.

# 설계
# input = '23'이라면 ['a', 'b', 'c'] for 돌리고 이 안에서 ['d', 'e', 'f'] for 문
# 제일 깊은 곳에서 word 생성 후 append

input = '23'

# 못풀음
def letterCombination(numbers):
  numbersDict = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
  }
  numList = [int(number) for number in input]
  charList = []
  wordList = []

  for num in numList:
    charList.append(numbersDict[num])
  
  def ex1(charListList):
    for charList in charListList:
      count = 0
      for char in charList:
        word = ''

        if charListList:
          charListList.pop(0)
          count += 1
          word += char + ex1(charListList)

          if count == len(numList) - 1:
            wordList.append(word)
          else:
            return word

        else:
          return ''
    return ''
  ex1(charList)

  print(wordList)
  # def ex1(numList):
  #   for num in numList:
  #     for char in numbersDict[num]:
  #       word = ''
  #       word = word + char

  #   return word  

# 예시 풀이 1. 모든 조합 탐색
digits = '234'

def letterCombinations(digits):
  dic = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
  }

  result = []

  numList = [number for number in digits]
  combination_count = 1

  for i in range(len(numList)):
    combination_count *= len(dic[numList[i]])

  def dfs(index, path):
    # 끝까지 탐색하면 백트래킹
    if len(path) == len(digits):
      result.append(path)
      return
    
    

    # 입력값 자릿수 단위 반복
    for i in range(index, len(digits)):
      if combination_count == len(result):
        break

      # 숫자에 해당하는 모든 문자열 반복
      for j in dic[digits[i]]:
        dfs(i + 1, path + j)

  # 예외 처리
  if not digits:
    return []
  
  dfs(0, '')
  return result

print(letterCombinations(digits))


# 연습
def practice1(digits):
  dic = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
  }

  result = []

  def dfs(index, path):
    if len(path) == len(digits):
      result.append(path)
      return
    
    for i in range(index, len(digits)):
      for j in dic[digits[i]]:
        dfs(i + 1, path + j)

  dfs(0, '')

  return result

print(practice1(digits))