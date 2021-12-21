list1 = ['h', 'e', 'l', 'l', 'o']

# 내 풀이
class ReverseList:
  # 나의 풀이
  def reverse_list(self, myList: str) -> bool:
    tempList = []

    index = len(myList) - 1

    while index >= 0:
      tempList.append(myList[index])
      index = index - 1

    for i in range(len(tempList)):
      myList[i] = tempList[i]

  # 풀이 1: 투 포인터를 이용한 스왑
  def reverseString(self, s: list[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
  # left와 right라는 포인터를 만든 후 left는 더하고 right는 빼주면서 둘이 같아질 때 까지 진행한다.
  # 23번째 줄 처럼 두 변수값이 스왑이 되는걸 몰랐다.

  # 풀이 2: 파이썬다운 방식
  def reverseString2(self, s: list[str]) -> None:
    s.reverse()

a = ReverseList()
a.reverseString2(list1)
print(list1)
