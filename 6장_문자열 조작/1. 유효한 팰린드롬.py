from collections import deque
import collections

str1 = 'A man, a plan, a canal: Panama'

# 나의 풀이
class Palindrome:
  def palindrome(self, myStr: str) -> bool:
    new_str_list = []

    for char in myStr:
      if char.isalnum():
        new_str_list.append(char.capitalize())

    index = 0

    for elem in new_str_list:
      if elem != new_str_list[len(new_str_list) - index - 1]:
        return False

      index = index + 1

    return True

# 파이썬 메서드 중 pop이 있다는 걸 몰랐기 때문에 인덱스 변수를 생성한 후 수작업으로 for문에서 해당 인덱스에 해당하는 요소와 비교를 했다.


#파이썬식 풀이
class Palindrome2:
  def palindrome(self, myStr: str) -> bool:
    strs = []

    for char in myStr:
      if char.isalnum():
        strs.append(char.lower())
    
    while len(strs) > 1:
      if strs.pop(0) != strs.pop():
        return False
    
    return True
    


# 데크형 자료구조를 이용한 풀이
# deque는 선입선출인 queue와 비슷하지만 양쪽에서 O(1)으로 넣고 뺄 수 있다는 장점이 있다.

class Palindrome3:
  def palindrome(self, myStr: str) -> bool:
    strs: deque = collections.deque()

    for char in myStr:
      if char.isalnum():
        strs.append(char.lower())

    while len(strs) > 1:
      if strs.popleft() != strs.pop():
        return False
    
    return True

a = Palindrome3()
print(a.palindrome(str1))
