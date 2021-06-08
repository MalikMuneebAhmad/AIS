def tri_recursion(k):
  global result
  if(k >= 1):
    result = k * tri_recursion(k - 1)  #recursion will happen in that step
  else:
    result = 1
  return result


print("\n\nRecursion Example Results")
tri_recursion(6)
print(result)

