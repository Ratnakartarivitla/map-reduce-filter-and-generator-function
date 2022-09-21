# Generator function
def samGen(a,b):
  yield a+b
  yield a-b
x=samGen(36,78)
print(x.__next__())
print(x.__next__())