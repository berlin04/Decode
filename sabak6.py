# from random import randint
# print("Угадайте число!")
# print("У вас есть неограниченное количество попыток.")
# print("Игра начинается...")
# n=int(input("Попытка №1:",)) 
# x=randint(1,100)
# popyt=1
# while True:
#     if n==x:
#         popyt+=1
#         print("Вы угадали")
#         print("Количество попыток:",popyt)
#         break
#     if n!=x:
#         popyt+=1
#         print("Вы не угадали,попробуйте еще!")
#         if n<x:
#             print("Введенное вами число,ниже чем надо")
#         elif n>x:
#             print("Введенное вами число,больше чем надо")
#         print("Попытка №"+str(popyt)+":")
#         n=int(input())


# from random import randint
# print("1------Камень")
# print("2------Ножница")
# print("3------Бумага")
# n=int(input("Ваш выбор:")) #chelovek
# x=randint(1,3)             #computer
# print("Выбор компьютера:",x)
# comp=0
# chel=0
# while True:
#     if n==x:
#         print("Ничья!")
#         print("Cчет(Компьютер:"+str(comp)+","+"Человек:"+str(chel)+")")
#     if n==1:
#         if x==2:
#             chel+=1
#             print("Cчет(Компьютер:"+str(comp)+","+"Человек:"+str(chel)+")")
#         elif x==3:
#             comp+=1
#             print("Cчет(Компьютер:"+str(comp)+","+"Человек:"+str(chel)+")")
#     elif n==2:
#         if x==1:
#             comp+=1
#             print("Cчет(Компьютер:"+str(comp)+","+"Человек:"+str(chel)+")")
#         elif x==3:
#             chel+=1
#             print("Cчет(Компьютер:"+str(comp)+","+"Человек:"+str(chel)+")")
#     elif n==3:
#         if x==1:
#             chel+=1
#             print("Cчет(Компьютер:"+str(comp)+","+"Человек:"+str(chel)+")")
#         elif x==2:
#             comp+=1
#             print("Cчет(Компьютер:"+str(comp)+","+"Человек:"+str(chel)+")")
#     if comp==3:
#         print("Победа компьютера!!!")
#         break 
#     if chel==3:
#         print("Победа человека!!!")
#         break
#     n=int(input("Ваш выбор:"))
#     x=randint(1,3)
#     print("Выбор компьютера:",x)

# from random import randint 
# x=randint(1,3) #предсказание 1-режим 
# y=randint(1,2) #вопрос 1-да, 2-нет      2-режим


# while True:
#     print("\nРежимы:")
#     print("1)Предсказание.")
#     print("2)Задать вопрос.\n")
#     n=int(input("Выберите режим:")) #режим
#     if n==1:
#         x=randint(1,3)
#         if x==1:
#             print("У вас будет удачный день!!")
#             a=input("Продолжаем? ")
#             if a=="Да":
#                 continue 
#             elif a=="Нет":
#                 print("Good bye")
#                 break
#             else:
#                 print("Error")
#                 break
#         elif x==2:
#              print("У вас будет неудачный день!!")
#              a=input("Продолжаем? ")
#              if a=="Да":
#                 continue
#              elif a=="Нет":
#                 print("Good bye")
#                 break
#              else:
#                 print("Error")
#                 break
#         elif x==3:
#              print("Все зависит от вас!!")
#              a=input("Продолжаем? ")
#              if a=="Да":
#                 continue
#              elif a=="Нет":
#                 print("Good bye")
#                 break
#              else:
#                 print("Error")
#                 break
#         else:
#             print("Error")
#             break
#     elif n==2:
#         y=randint(1,2)
#         b=input("Ваш вопрос:")
#         if y==1:
#             print("Ответ:Да")
#             a=input("Продолжаем? ")
#             if a=="Да":
#                 continue
#             elif a=="Нет":
#                 print("Good bye")
#                 break
#             else:
#                 print("Error")
#                 break
#         elif y==2:
#             print("Ответ:Нет")
#             a=input("Продолжаем? ")
#             if a=="Да":
#                 continue
#             elif a=="Нет":
#                 print("Good bye")
#                 break
#             else:
#                 print("Error")
#                 break
#         else:
#             print("Error")
#             break
#     else:
#         print("Error")
#         break

from random import randint
print("Консольный калькулятор")
print("Здес вы сможете делать простые математические вещи\n")
while True:
    print("________________________________________________")
    a=int(input("Введите первое число:"))
    print("('+','-','*','/','**','//','%')")
    x=input("Выберите операцию: ")
    b=int(input("Введите второе число:"))
    print("\nРезультат:")
    if x=="+":
        print(a,"+",b,"=",a+b)
   
    
    elif x=="-":
        print(str(a)+str(x)+str(b)+"=",a-b)
       
  
    
    elif x=="*":
        print(str(a)+str(x)+str(b)+"=",a*b)
       
    
    elif x=="/":
        if b==0:
            print("Делить на ноль нельзя")
           
        else:
            print(str(a)+str(x)+str(b)+"=",a/b)
           
    elif x=="**":
        print(str(a)+str(x)+str(b)+"=",a**b)
       
    elif x=="//":
        if b==0:
            print("Делить на ноль нельзя")
            
        else:
            print(str(a)+str(x)+str(b)+"=",a//b)
           
           
    elif x=="%":
        if b==0:
            print("Делить на ноль нельзя")
            
        else:
            print(str(a)+str(x)+str(b)+"=",a%b)
           
            
    else:
        print("Error")
        break
    n=input("Продолжаем?")
    if n=="Да" or n=="да":
            continue
    elif n=="Нет" or n=="нет":
            print("Goodbye")
            break

