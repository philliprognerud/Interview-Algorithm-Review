# QUESTION:
# Given an integer array, output all the unique pairs that sum up to a specific value k.

# So the input:

# pair_sum([1,3,2,2],4)

# would return 2 pairs:

# (1,3)
# (2,2)

###############################################################################


def pair_sum(array, targetVal):

  dict = {}
  maxVal = 0
  minVal = 0
  counter = 0

  #O(n) loop + O(1) look up time
  for key in array:
    if maxVal < key:
      maxVal = key

    if minVal > key:
      minVal = key

    if key in dict:
      dict[key] += 1
    else:
      dict[key] = 1

  #O(n) loop + O(1) look up time
  for x in range(minVal, int(maxVal / 2) + 1):
    lowVal = x
    highVal = targetVal - x

    if lowVal in dict and highVal in dict:
      if dict[lowVal] >= 1 and dict[highVal] >= 1:
        counter += 1

        if (lowVal == int(maxVal / 2) and dict[lowVal] < 2):
          counter -= 1

      dict[lowVal] = 0
      dict[highVal] = 0

  return counter


#O(n + n) runtime analysis
print(pair_sum([1, 2, 3, 1, -1, -2, 4, 0], 2))
