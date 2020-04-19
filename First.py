a = input("Enter the first value: ")
a = int(a)
b = input("Enter the second value: ")
b = int(b)
type = input("Enter the type from 1 to 4: ")
type = int(type)
if type == 1:
  k=a
  a=b
  b=k
  print("Type",type,"After Swaping:",a,"and",b)
elif type == 2:
  a = a+b
  b = a-b
  a = a-b
  print("Type",type,"After Swaping:",a,"and",b)
elif type == 3:
  a = a^b
  b = a^b
  a = a^b
  print("Type",type,"After Swaping:",a,"and",b)
elif type == 4:
  a,b = b,a
  print("Type",type,"After Swaping:",a,"and",b)
else:
  print("Wrong Input")



