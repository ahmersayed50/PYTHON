l1=[1,3,5,10,12,15,18,20,21,30]
l=[x for x in filter(lambda a:True if a%3==0 and a%5==0 else False,l1)]
print(l)
