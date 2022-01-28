from turtle import back


cargo = [
  (4, 12),
  (2, 1),
  (10, 4),
  (1, 1),
  (2, 2)
]

capacity = 15

class Solution:
  def fillInBackpack(self, cargo, capacity):
    backpack_capacity = capacity
    pack = []
    money = 0

    for i in range(len(cargo)):
      pack.append([cargo[i][0] / cargo[i][1], cargo[i][0], cargo[i][1]])

    pack.sort(reverse=True)

    for i in range(len(pack)):
      if backpack_capacity - pack[i][2] >= 0:
        backpack_capacity -= pack[i][2]
        money += pack[i][1]
      else:
        remained_kg_proportion = backpack_capacity / pack[i][2]
        backpack_capacity = 0
        money += pack[i][0] * remained_kg_proportion

    return int(money)

s = Solution()

print(s.fillInBackpack(cargo, capacity))