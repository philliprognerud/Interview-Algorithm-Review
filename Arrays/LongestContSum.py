#Largest continous sum of numbers, find the largest subset
#
# [0, 5, 4, -4, 3, -10, 10]
# answer: 10


def sum(arr1):

  current_sum = max_sum = arr1[0]

  if len(arr1) == 0:
    return 0

  if len(arr1) == 1:
    return arr1[0]

  for elem in arr1[1:]:
    current_sum = max(current_sum + elem, elem)
    max_sum = max(current_sum, max_sum)

  return max_sum


print(sum([1, 2, -1, 4, 3, -1]))
