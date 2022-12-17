# f=open("a.txt","r")
# # q=f.readlines()
# # print(q)
# l=[]
# for line in f.readlines():
#     l.append(list(map(int,line.split())))
# print(l)

# f=open("a.txt","r")
# p = []
# for new in f.read():
#     p.append(list(map(int,new.split())))
# print(p)


#............................create file.....................................................

# create = open("create.txt","a")
# create.write("hello there.\n 1 2 3")

#......................................................................................

# result = open("fir.txt"+"sec.txt","w")
# result.write()

f=open("fir.txt","r")
q=open("sec.txt","r")
t=open("res.txt","w")
a,b = [],[]

for vol in f.readlines():
    a.append(int(vol))
for vol in q.readlines():
    b.append(int(vol))
for i in range(len(a)):
    t.write(str(a[i]+b[i])+'\n')






f = open("fir.txt","a')
f.write()