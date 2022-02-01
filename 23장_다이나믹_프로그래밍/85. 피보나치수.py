class Solution:
  def fib(self, n):
    if n == 1 or n == 0:
      return 1
    
    return self.fib(n-1) + self.fib(n - 2)

s = Solution()
print(s.fib(4))
    