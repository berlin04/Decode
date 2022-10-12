#1 
 
# import math
# print(math.sqrt(45))
# print(math.pi)


# import random

# print(random.randint(1,10))
# arr=['decode','python','school','abc']
# print(random.choice(arr))


#2 

# from math import sqrt,pi,e 

# print(sqrt(80))
# print(pi)
# print(e)

#2v2

# from math import *   ##маth модулынен барлыгын колдану 

# print(pow(5,5))
# print(hypot(3,4))





# pip -пакетный менеджер 

# pip install ____
# pip uninstall ___ 







# озиннин модулынды куру 

#v1 
# import my_module

# print(my_module.x)
# print(my_module.arr)
# print(my_module.d)



#v2
# from my_module import x,d

# print(x)
# print(d)

#2v2
# from my_module import *
# print(x)
# print(d)
# print(arr)
# print(summa(5,12))





# import my_module as mm   ###as= модуь атын озине ынгайлы етип койып алу 
# print(mm.x)
# print(mm.arr)
# print(mm.d)
# print(mm.summa(5,4))






###cw18 


##Easy A 
# from my_module import var

# print(var[0])



### Easy B 
# from my_module import Student

# print(Student['name'])
# print(Student['age'])


###Easy C 

# from random import randint
# a=int(input())
# b=int(input())


# print(randint(a,b))


###Medium A
# from my_module import my_reverse 
# text=input()
# print(my_reverse(text))                                                 



#Medium B

# from math import sqrt,sin,pow
# x=int(input())
# y=int(input())

# c=(sqrt(sin(x)+pow(y,3))+sqrt(x+y))/(2*x+y)

# print(c)



###Medium C 
# from math import sqrt,sin,pow,exp,cos
# a=(sin(5)+pow(1.75,2))/(3*exp(cos(7)))
# print(a)




###Hard A 

# from my_module import sum_index

# arr=[int(el) for el in input().split()]

# print(sum_index(arr))















#####HW 18
#Easy A 
# from math import sqrt,pow 
# a=int(input())
# b=int(input())

# c=pow((sqrt(a)-sqrt(b)),2)
# print(c)




##Easy B 
# from math import pi,tan
# a=int(input())
# b=int(input())
# print(tan(-a*pi/b))             




###Medium A 
# from random import randint
# from my_module import summ

# a=randint(1000,9999)
# print(a)

# print(summ(a))










###Hard A 

# from random import choice
# arr=[int(el) for el in input().split()]
# sum=0
# while True:
#     for i in range(1,1000):
#         a=int(choice(arr))
#         print(f"{i} попытка",a)
#         if a!=max(arr):
#             sum+=1    
#         else:
#             break
#     break


# print(f"Количество попыток {sum}")




