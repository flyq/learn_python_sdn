def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
for i in range(4):
    print(next(gen))
