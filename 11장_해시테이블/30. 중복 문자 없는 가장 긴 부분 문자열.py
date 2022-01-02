import collections
myString = 'bbb'

def longestString(myStr):
  dict = collections.defaultdict(int)
  list = []
  count = 0

  for char in myStr:
    if dict[char] != 1:
      dict[char] += 1
      count += 1

    elif dict[char] == 1:
      list.append(count)
      dict = collections.defaultdict(int)
      dict[char] += 1
      count = 1

  print(max(list))
longestString(myString)
  