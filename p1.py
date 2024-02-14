num = 123
func0 = lambda x: list(str(x))
func1 = sum(list(map(lambda x: int(x), func0(num))))
print(func1)