# sum min max 
#sorted reversed  

### sum,min,max


# d={
#     1:75,
#     2.5:105
# }

# print(sum(d.values())) #180
# print(sum(d))   #3.5


## sorted reversed 













st={'a','b','c','d'}
# print(sorted(st))  #массивке айналдырып барып сортировка жасайды осу ретимен 

# print(sorted(st),reverse=True) # кему ретимен шгарад

# print(list(reversed(st))) #кему ретимен айналдырад, ,бириншы массивке айналдырады 






#CW 13

# Easy A
# list=[int(i) for i in input().split()]
# if sum(list)>10:
#     print("More")
# elif sum(list)<10:
#     print("Less")
# else:
#     print("Else")



#Easy B
# a=input()
# b=input()

# print(f"http://www.{a}.{b}/")


#Easy C

# s=input()
# st=set(s)

# print(len(st))


##Easy D
# d={}
# text=input().split()
# for el in text:
#     d[el]=len(el)



# for k,v in d.items():
#     print(k,v,sep=":")


#Medium A

# arr=[int(el) for el in input().split()]

# print(*arr[1::2])


### Medium B 
# alp="abcdefghijklmnopqrstuvwxyz "
# s=input().lower()
# l=len(s)

# if s==alp[:l]:
#     print("good")
# else:
#     print("cringe")



##Medium C 

# n=int(input())
# d={}
# for el in range(n):
#     k,v=input().split()
#     d[k]=v

# print(sorted(d.items()))
    




######### HW 13

####Easy A 


# arr=[int(el) for el in input().split()]
# n=arr[0]
# result=[]
# for el in arr:
#     if el>n:
#         result.append(el)
#     n=el
# print(result)



####Easy B


# arr=[int(el) for el in input().split()]
# max=arr[0]
# for el in arr:
#     if el>max:
#         max=el
# if max%2!=0:
#     print("error")    
# else:
#     print(max)


###Medium A

# d={  

# }
# n=int(input())

# for i in range(n):
#     k=input()
#     v=[int(el) for el in input().split()]
#     d[k]=v
   
#     cnt=0    
#     for el in v:
#         cnt+=el
#     b=cnt/len(v)
#     d[k]=b

# print(d)


##Medium B 
# s=input()

# f=s.find('h')
# l=s.rfind('h')

# print(s[:f]+s[l:f-1:-1]+s[l+1:])



### Hard A 
# arr=[int(el) for el in input().split()]
# max=arr[0]
# for el in arr:
#     if el%2!=0:
#         if el>max:
#             max=el
# if max%2==0:
#        print('Error')
# else:
#     print("Число:",max)
#     summ=0
#     while max>0:
#         a=max%10
#         summ+=a
#         max//=10
#     print("Сумма:",summ)




#Hard B

cpp=set()
pyth=set()

n,m=int(input(),int(input()))

for i in range(n):
    name=input()
    cpp.add(name)


for i in range(m):
    name=input()
    pyth.add(name)


ans=cpp.symmetric_difference(pyth) ## екы сеттын айырмашылыктарын бир сетке шгарады 


print(len(ans))
    

print()
print()
print()
print()
