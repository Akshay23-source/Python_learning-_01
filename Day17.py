numbers = [1, 2, 3]
for n in numbers:
    print(n)
    
    
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


def count():
    return [1, 2, 3]


def count():
    yield 1
    yield 2
    yield 3

for num in count():
    print(num)
    
    def numbers(n):
    for i in range(n):
        yield i

for num in numbers(5):
    print(num)
    
    gen = (x*x for x in range(5))

for value in gen:
    print(value)
    