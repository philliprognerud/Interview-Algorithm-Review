#Largest continous sum of numbers, find the largest subset
#
# [0, 5, 4, -4, 3, -10, 10]
# answer: 10


def sum(arr1):
  d1 = {}
  sums = 0

  for i, x in enumerate(arr1):
    if len(d1) > 0:
      sums += x
      d1[i] = sums
    else:
      d1[i] = x
      sums = x

  print(d1)


sum([1, 2, -1, 4, 3, -1])
