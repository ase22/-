# 여러 번의 거래로 낼 수 있는 최대 이익을 산출하라.
stocks = [7, 1, 5, 3, 6, 4]

class Solution:
  def maxProfit(self, stocks):
    profit = 0

    for i in range(len(stocks) - 1):
      if stocks[i] < stocks[i + 1]:
        profit += stocks[i + 1] - stocks[i]
    
    return profit
  
