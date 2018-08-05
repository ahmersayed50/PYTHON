file=open('C:\Users\LIC\Desktop','r')
s=file.read()
l=s.split('\n')
l2=[]
for each in l:
    s=each.split(',')
    l2.append(s)
l3=[]
o=[]
for i in range (0,len(l2)):
    l3.append(int(l2[i][0]))
for i in range (0,len(l2)):
    salary=int(l2[i][2])
    if (salary<=2000):
        x=(salary*2/100)
        total1= (x+salary)
        o.extend([l3[0],salary,x,total1])
    elif(salary>2001 and salary<5000):
        y=salary*5/100
        total2=y+salary
        o.extend([l3[1],salary,y,total2])
    elif (salary>5001 and salary<7000):
        z=salary*7/100
        total3=z+salary
        o.extend([l3[2],salary,z,total3])
file.close()

file2=open('C:\\Users\\hp\\Desktop\\abc2.txt','w')
str1=' '.join(str(e) for e in o)
file2.write(str1)
file2.close()
print('executed completly')
