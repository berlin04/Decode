# class Human:    ###класс
#     # x=5
#     # y=10
#     # name='abay'
#     number_of_eyes=2               #атрибут/поля
#     def __init__(self,name,age):   ###self-оз озине силтеме
#         self.name=name             ### универсальный обьект
#         self.age=age
    
#     def show_info(self):          ###метод 
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"Eyes:{self.number_of_eyes}")
#         print(f"Is elder:{self.is_elder()}\n")
#     def is_elder(self):
#         return self.age>=18


# human1=Human('Abay',21)   ###обьект
# human2=Human('Erlan',19)  ###обьект

######isinstance  
# x=5
# arr=[]

# print(isinstance(human1,Human))  ####True
# print(isinstance(x,int))         ####True
# print(isinstance(arr,list))      ###True
# print(isinstance(x,Human))       ####False





# human2.age=20      ###озгеруге болады 

# del human2.age     ##ощру ушин бир атрибитты 


# human1.show_info()
# human2.show_info()









#####CW 22 

##Easy A 

# class Point:
#     x=5
#     y=10


# s=input()
# if s=='x':
#         print(Point.x)
# elif s=='y':
#         print(Point.y)
# else:
#     print("error")



#####Easy B 
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

# s=input()
# y=input()
# pp=Point(s,y)

# b=input()
# if b=='x':
#         print(pp.x)
# elif b=='y':
#         print(pp.y)
# else:
#     print("error")




####Easy C 

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def dist(self,point):
#           return pow(pow(point.x-self.x,2)+pow(point.y-self.y,2),0.5)

# x1=int(input())
# y1=int(input())
# p1=Point(x1,y1)

# x2=int(input())
# y2=int(input())
# p2=Point(x2,y2)


# print(p1.dist(p2))



####Medium  A 
# class Rect:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def  is_square(self):
#         return self.x==self.y 

# a=int(input())
# b=int(input())


# rect=Rect(a,b)

# print(rect.is_square())



####Medium B 

# class Rect:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def get_perimeter(self):
#         return 2*(self.x+self.y)
#     def  get_area(self):
#         return self.x*self.y
#     def get_diagonal(self):
#         return (self.x**2+self.y**2)**0.5

# a=int(input())
# b=int(input())


# rect=Rect(a,b)

# print(rect.get_perimeter())
# print(rect.get_area())
# print(rect.get_diagonal())




####Hard A 
# class Shop:
#     phones={
#         'iphone':1000,
#         'samsung':900,
#         'nokia':500,
#         'xioami':800
#     }

#     busket={}
    
#     def get_phone(self,phone):
#         if phone not in self.phones.keys():
#             print('У нас нет такого смартфона!!!')
        
#         elif phone not in self.busket.keys():
#             self.busket[phone]=1
#         else:
#             self.busket[phone]+=1
    
#     def remove_phone(self,phone):
#         if phone in self.busket.keys():
#             if self.busket[phone]==1:
#                 del self.busket[phone]
#             else:
#                 self.busket[phone]-=1
#         else:
#             print("Такого товара нет в корзине")
    
#     def show_busket(self):
#         for phone,cnt in self.busket.items():
#             print(f"Смартфон:{phone},Количество:{cnt},Цена:{self.phones[phone]}")


# shop=Shop()

# shop.get_phone("iphone")
# shop.get_phone("iphone")
# shop.get_phone("iphone")
# shop.get_phone("abc")
# shop.get_phone("samsung")
# shop.get_phone("xioami")

# shop.remove_phone("xioami")
# shop.remove_phone("iphone")

# shop.show_busket()






##########HW 22 
###########Easy A 

# class Almira:
#     def __init__(self,name,age):
#         self.name='Альмира'
#         if name!=self.name:
#             print(f'Я не {name},я {self.name}')
#         else:
#             print(self.name)


# person_name=input()
# person_age=int(input())

# pers=Almira(person_name,person_age)

    



##########Medium A 

# class Gazirovka: 
#     def __init__(self,gaz=""):
#         self.gaz=gaz

#     def show_my_drink(self):
#         if self.gaz=="":
#             print("Обычная газировка")
#         else:
#             print(f"Газировка и {self.gaz}")

# gaz=input()

# sok=Gazirovka(gaz)
# sok.show_my_drink()       



#######Hard A 

# class Triangle: 
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
    
#     def is_it_triangle(self):
#         try:
#             self.x=float(self.x)
#             self.y=float(self.y)
#             self.z=float(self.z)
#         except:
#             print("нужно вводить только числа")
#             return
#         if self.z<0 or self.x<0 or self.y<0:
#             print(" С отрицательными числами ничего не выйдет!")    
#         elif (self.x+self.y)>self.z and (self.x+self.z)>self.y and (self.z+self.y)>self.x:
#             print("Ура, можно построить треугольник!")
#         else:
#             print("Жаль, но из этого треугольник не сделать")


# a,b,c=input().split()

# tri=Triangle(a,b,c)
# tri.is_it_triangle()






