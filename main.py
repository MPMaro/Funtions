
# Global Vars
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
  reverse = aList[::-1]
  return reverse

def swap(aList, index1, index2):
  save = aList[index1]
  aList[index1] = aList[index2]
  aList[index2] = save
  return aList

def indexofmin(aList):
  position = 0
  for i in range(1, len(aList)):
    if aList[i] < aList[position]:
      position = i
  return position


# Testing

if contains(test, 7):
  print("Number is in  list")
else:
  print("Number is not in the list")

index = indexOf(test, 8)
if index != -1:
  print(f"8 IN list at {index}")
else:
  print("8 NOT in list")

print(reverse(test))

print(swap(test, 2, 4))

print(indexofmin(test))
    