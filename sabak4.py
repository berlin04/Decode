# from random import randint
# n=int(input("Санды енгизиниз:"))
# x=randint(1,9)
# if n==x:
#     print("Сиз таптыныз")
# elif n!=x:
#     n=int(input("Санды енгизиниз:"))
#     if n==x:
#         print("Сиз таптыныз")
#     elif n!=x:
#         n=int(input("Санды енгизиниз:"))
#         if n==x:
#              print("Сиз таптыныз")
#         else:
#              print("Сиз утылдыныз")



# p1=input("1:")
# p2=input("2:")
# if p1=="камень":
#     if p2=="ножница":
#         print("1 игрок выиграл")
#     elif p2=="бумага":
#         print("2 игрок выиграл")
#     elif p2=="камень":
#         print("ничья")
# elif p1=="ножница":
#     if p2=="камень":
#         print("2 игрок выиграл")
#     elif p2=="бумага":
#         print("1 игрок выиграл")
#     elif p2=="ножница":
#         print("ничья")
# elif p1=="бумага":
#     if p2=="камень":
#         print("1 игрок выиграл")
#     elif p2=="ножница":
#         print("2 игрок выиграл")
#     elif p2=="бумага":
#         print("ничья")

# from random import randint
# x=randint(1,3)  
# # 1-камень
# # 2-ножница
# # 3-бумага 
# n=int(input("Я:"))
# print(x)
# if x==n:
#     print("ничья")
# elif x==1:
#     if n==2:
#         print("1 win")
#     elif n==3:
#         print("2 win")
# elif x==2:
#     if n==1:
#         print("1 win")
#     elif n==3:
#         print("2 win")
# elif x==3:
#     if n==1:
#         print("1 win")
#     elif n==2:
#         print("2 win")           
    
# x=int(input("Введите ваш номер:"))
# n=x//10000000
# if n==7727 or n==8727:
#     print("●	Актив (Activ) +7 727")
# elif n==7708 or n==8708 :
#     print("●	Алтел (ALTEL) 4G. +7 708")
# elif n==7777 or n==8777:
#     print("●	Билайн (Beeline) Казахстан +7 777")
# elif n==7701 or n==8701:
#     print("●	Кселл (Kcell) +7 701")
# elif n==7747 or n==8747:
#     print("●	Теле2 (Tele2) +7 747")
# else:
#     print("error")

a=int(input("1 san:"))
b=int(input("2 san:"))
x=input("Операция:") 
if x=="+":
    print(a+b)
elif x=="-":
    print(a-b)    
elif x=="*":
    print(a*b)
elif x=="/":
    if b==0:
        print("error")
    print(a/b)
    
elif x=="**":
    print(a**b)    
elif x=="//":
    if b==0:
        print("error")
    print(a//b)
elif x=="%":
    print(a%b)
else:
    print("error")                