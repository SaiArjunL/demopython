from functools import *
from Fourth import *

numbers = []

for i in range(5):
    num = int(input("Enter a list of numbers: "))
    numbers.append(num)

evns = list(filter(lambda a : a % 2 == 0,numbers))

sqrs = list(map(lambda a : a * a, evns))

sum = reduce(lambda a, b : a + b, sqrs)

print(evns)
print(sqrs)
print(sum)
names = ['ladeela', 'sai', 'arjun', 'sai arjun', 'ladeela sai arjun']
function(names)
