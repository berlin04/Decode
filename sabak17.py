#### Try-except


# print("start")



# try:
#     print(x)
# except:
#     print("ошибка!")


# print("stop")
# print("stop")
# print("stop")
# print("stop")





# try:
#     age=int(input("введите возраст "))
# except:
#     age=int(input("введите цифрами  "))

# if age<0:
#     raise Exception("Некорректный возраст! ")   ### ошибканы колдан шакыру озимиз
# else:
#     print('Ваш возраст:',age)




# try:
#     div=int(input())
#     print(100/div)

#     print(div)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")
# except NameError:
#     print("То что вы используете нет в нашем языке")
# except ValueError:
#     print("Введите только целое число")




# try:
#     a=float(input("ребро а="))
#     b=float(input("ребро b="))
# except ValueError:
#     print("Вы ввели не цифру")
# except:
#     print("некая ошибка")
# else:
#     print(f"Площадь прямоугольника  {a*b}cм2")






#######Тернарный оператор

# age=int(input())

# print("добро пожаловать" if age>=21 else "вам сюда нельзя")


# if age>=21:
#     print("добро пожаловать")
# else:
#     print("вам сюда нельзя")



# def abs(num):
#     return num if num>0 else -num

# n=float(input())
# print(abs(n))        



###Easy B 
# try:
#     n=int(input())
#     print(n)
# except ValueError:
#     print("srsly?")



###Easy C 

# name=input()
   
# if not name[0].isupper():
#     raise Exception("чел ты ")
# else:
#     print(name)

    



#####Medium A 


# name=input()
# if name.isalpha():
#     print("welcome")
# else:
#     raise NameError("ошибка!")





# print('even' if int(input())%2==0 else 'odd')









# arr=list(map(int,input().split()))

# try:
#     a,b=arr
# except:
#     a=arr[0]
#     b=int(input())

# print(a+b)



#####Medium B 

# email=input()

# if email.count('@')==1:

#     print("ok")
# else:
#     raise NameError("ОШИБКА")
    




#####HW 17

##Easy A 

# d={
#     'a':1,
#     'b':2,
#     'c':3
# }
# n=input()
# try:
#     if n==d.keys:
#         print()



####Easy B 
# a=int(input())
# b=int(input())

# print(b if a>b else a)


###Medium A 

# arr=[int(el) for el in input().split()]
# s=0
# for el in arr:
#     if el%3==0 and el%5==0:
#         s+=1
# if s!=0:
#     print("Такое число присутствует") 
# else:
#     raise Exception("Такое число отсутствует")


####Medium B 

# a=int(input())
# b=int(input())
# c=int(input())

# if a*b==c:
#     print(True)
# else:
#     raise Exception(False)



###Hard B 



def my_func(num):
    while num>0:
        a=num%10
        return True if a%3==0 else num=//10
    return False 
    
print(my_func(8592))

