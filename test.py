s=input().lower()

d=dict.fromkeys(s,0)

for i in s:
    d[i]=s.count(i)


for k,v in sorted(d.items()):
    print(k,v,sep="---")



     



