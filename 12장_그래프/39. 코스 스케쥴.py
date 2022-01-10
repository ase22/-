n, courses = 2, [[1, 0]]

T = int(input('케이스 몇개인지 입력해 주세요: '))

for test_case in range(1, T + 1):
  N, K = map(int, input('숫자 개수와 몇번째 숫자인지 입력해 주세요: ').split())
  nums = input('숫자열을 입력해 주세요: ')
  num_list = []
  count = 0

  while count < N / 4:
    for i in range(4):
      num_list.append(nums[int((N/4)*i):int((N/4)*(i+1))])
    nums = nums[-1] + nums[:-1]
    count += 1

  num_list = list(set(num_list))
  num_list.sort(reverse=True, key=lambda number: int(number, 16))

  print('#' + str(test_case) + ' ' + str(int(num_list[K-1], 16)) + '\n')
