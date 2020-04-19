def fun():
    n = 1
    while n<=10:
        sol = n * n
        yield sol
        n = n + 1


def ownfun():
    yield 'sai1'
    yield 'sai2'
    yield 'sai3'
    yield 'sai4'
    yield 'sai5'


#print(next(ownfun()))
#print(ownfun().__next__())

for i in ownfun():
    print(i)

for i in fun():
    print(i)

