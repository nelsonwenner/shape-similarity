from functools import reduce

def array_sum(numberArray):
  return reduce((lambda acc, val: val + acc), numberArray, 0)
  
def array_average(numberArray):
  summ = reduce((lambda acc, val: val + acc), numberArray, 0)
  return summ / len(numberArray)