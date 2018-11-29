def isMember(value, list1):
  for element in list1:
    if(element == value):
      return True
  return False
    

myList = ["a","b","c",1,2,3]

print(isMember("a",myList)) 
print(isMember(1,myList))