# filter
ages = [5,12,17,18,24,32]
def myFunc(x):
  if x>=18:
    return True
  else:
    return False
adults = filter(myFunc,ages)
print(list(adults))

# Map
def caliculate(x):
  return x**2
numbers = (1,2,3,4)
result = map(caliculate,numbers)
print(list(result))


# reduce
from functools import reduce

d = reduce(lambda a,b : a+b,[12,43,67,53])
print(d)