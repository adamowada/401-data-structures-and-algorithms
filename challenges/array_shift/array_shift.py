import math

def insertShiftArray(list, element):
  index = math.ceil(len(list)/2)
  list.insert(index, element)
  return list