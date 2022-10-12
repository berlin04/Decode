###Наследование


# class Human:
#     def __init__(self,name,surname):
#         self.name=name
#         self.surname=surname
    
#     def get_info(self):
#         print(f"Name:{self.name}")
#         print(f"Surname:{self.surname}")



# class Student(Human):
#     def __init__(self,name,surname,university,course,gpa):
#         super().__init__(name,surname)
#         self.university=university
#         self.course=course
#         self.gpa=gpa

#     def get_info(self):
#         super().get_info()
#         print(f"University:{self.university}")
#         print(f"Course:{self.course}")
#         print(f"GPA:{self.gpa}")


# s1=Student()
# print(s1.name)
# s1.test()

# p=Pervash()
# print(p.name)




###Мысал 1
# class Pervash(Student):
#     pass

###Мысал 2 
# st=Student('Erlan','Kasenov','KBTU',4,3.76)

# st.get_info()


#####issubclass 

# print(issubclass(Student,Human))  ####True
# print(issubclass(int,Human))      ####False





#######андерметод или спец метод 

# class Human:
#     def __init__(self,name,surname,height):
#         self.name=name
#         self.surname=surname
#         self.height=height
     
#     def __str__(self):            #####бир строка кайтару керек 
#         return f"I am {self.name}"      
    
#     def __len__(self):            
#         return self.height
    
#     def __gt__(self,other_human):
#         return self.height>other_human.height


# human1=Human('Erlan','Kasenov',176)
# human2=Human('Almira','Asanova',168)
# print(human1>human2)


# print(human1)
# print(len(human1))






####инкапсуляция 


# class Human:
#     def __init__(self,name,surname,height):
#         self.__name=name            ########### приватный кылу ушин
#         self.surname=surname
#         self.height=height


# human1=Human('Erlan','Kasenov',176)

# print(human1.name)




######CW 23 
###Easy C 

# class Country:
#     def __init__(self,popul):
#         self.popul=popul

#     def getPopulation(self):
#         return self.popul
    
#     def setPopulation(self,new_popul):
#         self.popul=new_popul

# class Germany(Country):
#     pass

# class Russia(Country):
#     pass    
 
# class Canada(Country):
#     pass

# s1=Germany(5000)
# print(s1.getPopulation())
# p=int(input())
# s1.setPopulation(p)
# print(s1.getPopulation())





####Easy A 

# class Games:
#     def __init__(self,year,name_game):
#         self.year=year
#         self.n_g=name_game

#     def getName(self):
#         return self.n_g



# class PCGames(Games):
    
#     def getName(self,new_name_game):
#         return new_name_game


# class Ps4Games(Games):
    
#     def getName(self,new_name_game):
#         return new_name_game


# class XboxGames(Games):
    
#     def getName(self,new_name_game):
#         return new_name_game





#########Medium B 

# class Shape:
#     def get_area(self):
#         return 0 

# class Triangle(Shape):
#     def __init__(self,a,b,c):
#         pass

# class Square(Shape):
#     def __init__(self,a):
#         self.a=a
#     def get_area(self):
#         return self.a**2
# s=Shape()


# s1=Triangle(3,4,5)

# x=int(input())
# s2=Square(x)
# print(s.get_area())
# print(s1.get_area())
# print(s2.get_area())
