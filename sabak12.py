#dictonary

# d1={}
# d2=dict()
# print(d1,d2)

# d1={
#     -1: 4,
#     2.5:6,
#     'abc':4,
#     True:1,
#     False:156
# }
# print(d1)
# d1[4]="barca"  #жана элемент косуга болады 



# d=dict(abc=123,qwe='decode')  #тек ключ строка болады 


#метод 
# d1={
#     -1: 4,
#     2.5:6,
#     'abc':4,
#     True:1,
#     False:156
# }
# print(d['abc'])
# print(d.get('qwe'))  # бар ма жок па карап береды жок болса none шгарадаы 

# d1.popitem()   # словардагы сонгы параны шгарп беред 
# print(d1.popitem()) 

# d1.pop('2.5')  # ключ бойынша алып тастайды 
# print(d1.pop('2.5'))

# d1.update({10:100,20:200}) # екы dict косады 

# print(d1)
# s='decode'
# d1=dict.fromkeys(s,0) # decode ты аркайсысын ключ кылтып мандерин 0 кылады 

# print(d1)
# lst=[1,2,3,4]
# s='abcd'
# d=dict(zip(s,lst))  # s тар ключ болады lst тар элемент болады 

# d1.values() #  мандерин бир массивке жинап береды 
# d1.keys()   #  ключтарды бир массивке жинап береды 
# d1.items()  #  букил параларды бир массивке жинап береды 

# for v in d1.values():
#     print(v)




### tuple 
#  0 1    2       3
# a=(7,5,"decode",False)
# -4 -3   -2      -1

# print(a[2])
# a.index('decode')  
# a.count(5)
# тек екы методы бар 





######## input

# n=int(input())
# d={}
# for i in range(n):
#     k,v=input().split()
#     d[k]=v

# print(d)




# keys= ['Ten','Twenty','Thirty']
# values=[10,20,30]
# d=dict(zip(keys,values))
# print(d)

# sampleDict={
#     "class":{
#         "student":{
#             "name":"Mike",
#             "marks":{
#                 "physics":70,
#                 "history":80
#             }
#         }
#     }
# }
# print(sampleDict['class']['student']['marks']['history'])







# sample_dict={
#     'Physics':82,
#     'Math':65,
#     'history':75
# }
# a=min(sample_dict.values())
# for k,v in sample_dict.items():
#     if v==a:
#         print(k)




# info={
#     'name':'aidana',
#     'grades': [96,78,67,73,90]
#     }
# sum=0
# b=info['grades']

# for el in b:
#     sum+=el
# print(sum/len(b))

# n=int(input())
# d={}
# for i in range(n):
#     k,v=input().split()
#     d[k]=v 
# print(d)

# text=input().split()
# d={}
# for el in text:
#     d[el]=text.count(el)

# for k,v in d.items():
#     print(k,v,sep=":")

# n=int(input())
# d={}

# while n!=0:
#     last=n%10
#     if last not in d.keys():
#         d[last]=0
#     d[last]+=1
#     n//=10
# for v,k in d.items():
#     print(v,k)

# n=int(input())   
# d={}
# for i in range(n):
#     k,v=input().split()
#     d[k]=int(v)
# ball=d.values()
# print(ball)
#  for i in range(len(ball)):
    
    





n=int(input())
d1={}    
for i in range(n):
    log,pwd=input().split()
    d1[log]=pwd 

m=int(input())
d2={}
for c in range(m):
    user_log,user_pwd=input().split()
    d2[user_log]=user_pwd
    if log==user_log:
        if d1[log]==d2[user_log]:
            print("welcome")
        else:
            print("wrong password")
    else:
        print("user not defined")



arr=d1.keys()
user_arr=d2.keys()
parol=d1.values()
user_parol=d2.values()






# a=int(input())
# b=int(input())
# d={}
# for i in range(a,b+1):
#     d[i]=i**2
# print(d) 



    
    
    
    

 
    
    
    

