l1=[7,6,4]
l2=[2,3,5]
l={m:v for m,v in map(lambda a,b:(a,b**2)if a>b else (b,a**2),l1,l2)}
print(l)
