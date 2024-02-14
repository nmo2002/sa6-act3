alist = [1,2,3,4]
blist = [1,3,5,2,10]
d = list(filter(lambda x: x in alist , blist))
print(d)
