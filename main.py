
# Global List
test = [4, 7, 2, 5, 10]


# Functions
def contains(aList, item):
  for i in range(len(aList)):
    if (aList[i]) == (item):
      return True


def indexOf(aList, item):
    for index, element in enumerate(aList):
        if element == item:
            return index
    return -1

def reverse(aList):
  rev = aList[::-1]
  return rev

def swap(aList, index1, index2):
  save = aList[index1]
  aList[index1] = aList[index2]
  aList[index2] = save
  return aList

def indexofmin(aList):
  minpos = 0
  for i in range(1, len(aList)):
    if aList[i] < aList[minpos]:
      minpos = i
  return minpos



