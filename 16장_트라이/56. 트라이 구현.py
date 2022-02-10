# 트라이의 insert, search, startsWith 메소드를 구현하라.

import collections

# 풀이 실패
class Node:
  def __init__(self):
    self.value = False

class Solution:
  def __init__(self):
    self.head = Node()

  def insert(self, string):
    a = Node('')

    for i in range(len(string)):
      if not a.value:
        a.string[i] = Node(string[i])

      a = a.string[i + 1]

# 예시 풀이
# class TrieNode:
#   def __init__(self):
#     self.word = False
#     self.children = collections.defaultdict(TrieNode)

# class Trie:
#   def __init__(self):
#     self.root = TrieNode()

#   def insert(self, word):
#     node = self.root

#     for char in word:
#       if char not in node.children:
#         node.children[char] = TrieNode()

#       node = node.children[char]

#     node.word = True

#   def search(self, word):
#     node = self.root

#     for char in word:
#       if char not in node.children:
#         return False
#       node = node.children[char]

#     return node.word

#   def startsWith(self, prefix):
#     node = self.root

#     for char in prefix:
#       if char not in node.children:
#         return False
#       node = node.children[char]

#     return True

# 구현 연습
class trieNode:
  def __init__(self):
    self.word = False
    self.children = collections.defaultdict(trieNode)

class trie:
  def __init__(self):
    self.root = trieNode()

  def insert(self, word):
    node = self.root

    for char in word:
      # node.children[char] = trieNode() 이게 아니라
      node = node.children[char] # 이거고 char로 키값을 넣는 순간 char이 키가 돠고 값은 node.children[char]이 되고 이건 디폴트값인 trieNode이다.
    node.word = True


  def search(self, word):
    node = self.root

    for char in word:
      if char not in node.children:
        return False
      node = node.children[char]
    
    return node.word

  def startsWith(self, prefix):
    node = self.root

    for char in prefix:
      if char not in node.children:
        return False
      node = node.children[char]
    
    return True

trie = trie()
trie.insert('apple')
print(trie.search('apple'))






