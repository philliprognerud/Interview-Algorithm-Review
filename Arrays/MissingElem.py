def finder(arr1, arr2):
  a = set(arr1)
  b = set(arr2)
  c = a ^ b

  return c.pop()


print(finder([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6]))
