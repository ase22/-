def quicksort(A, lo, hi):
  def partition(lo, hi):
    pivot = A[hi]
    left = lo

    for right in range(lo, hi):
      if A[right] < pivot:
        A[left], A[right] = A[right], A[left]
        left += 1

    A[left], A[hi] = A[hi], A[left]

    return left

  if lo < hi:
    pivot = partition(lo, hi)
    quicksort(A, lo, pivot - 1)
    quicksort(A, pivot + 1, hi)

# 정렬에는 안정 정렬과 불안정 정렬이 있다.
# 지역과 시간이 하나의 데이터로 묶여 있고 이것들이 여러개인 데이터를 정렬하는 상황일때

# 안정 정렬은 기존 순서가 유지된 상태에서 정렬이 이뤄진다.
# 불안정 정렬은 시간 순으로 정렬한 값을 지역명으로 재정렬하면 기존의 정렬 순서는 무시된 채 모두 뒤죽박죽 섞인다.

# 안정 정렬의 종류
  # 1. 버블 정렬
  # 2. 병합 정렬

# 불안정 정렬의 종류
  # 1. 퀵 정렬

# 이러한 고르지 않은 성능 탓에 실무에서는 병합 정렬이 활발히 쓰이고 파이썬의 기본 정렬 알고리즘은 병합 정렬과 삽입 정렬을 휴리스틱하게 조합한 팀소트를 사용한다.

