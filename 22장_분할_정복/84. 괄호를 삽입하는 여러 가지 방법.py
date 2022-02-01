# 숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라.

input = '2*3-4*5'

# 풀이 순서
# 분할 -> 정복
# 분할: 숫자 하나만 있을 때 까지 분리한다.
# 이걸 구현하려면 if input.isdigit(): 써서 input이 digit인지 확인 후 리턴한다.
# 이렇게 하면 리턴된 값은 숫자 1개를 가지는 배열이 되고 이렇게 left와 right값이 모이면 compute로 들어가서 값이 계산된다.
# 이 과정이 재귀적으로 일어나기 때문에 가장 깊숙한 곳에서부터 순회를 하면서 계산되고 맨 마지막에 다 계산된 후의 compute값이 계산된다.
# 이 과정이 끝나면 맨 첫번째 순회에서 첫 인덱스인 경우가 끝난거고 나머지 인덱스인 경우를 다시 수행한다.

# 이걸 풀기 위해서는 분할 정복이 필요함을 느껴야 하고 가장 작은 단계에서 어떤 코드가 필요할지 생각
# 
class Solution:
  def diffWaysToCompute(self, input: str) -> list[int]:
    def compute(left, right, operator):
      results = []

      for l in left:
        for r in right:
          results.append(eval(str(l) + operator + str(r)))

      return results

    if input.isdigit():
      return [int(input)]

    results = []

    for index, value in enumerate(input):
      if value in '-+*':
        left = self.diffWaysToCompute(input[:index])
        right = self.diffWaysToCompute(input[index + 1:])

        results.extend(compute(left, right, value))

    return results

class practice1:
  def getDiffs(self, input):
    if input.isdigit():
      return [int(input)]

    def compute(left, right, operator):
      print(type(left[0]), type(right[0]))
      results = []
      results.append(eval(str(left[0]) + operator + str(right[0])))

      return results

    results = []

    for index, value in enumerate(input):
      if value in '-+*':
        left = self.getDiffs(input[:index])
        right = self.getDiffs(input[index + 1:])

        results.extend(compute(left, right, value))

    return results