a = int(input("Enter any value:"))
m = a
l = 0
while(a>0):
  k = a % 10
  l = l * 10 + k
  a = a//10

if(m != l):
  print("Rev is:",l)
else:
  print("Same")
