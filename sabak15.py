### Функция 

# def test():
#     print("бул функция")


# test()
# print("программа соны")



# def greeting(name):
#     print(f"Salem {name}!")

# greeting('Alan')
# greeting('Abay')

# x='Berik'
# greeting(x)




# def greeting(name,age):
#     print(f"Salem {name}!")
#     print(f"Zhasyniz: {age}")
#     print()

# greeting('Alan',26)
# greeting('Abay',21)

# x='Berik'
# n=20
# greeting(x,n)



# print(max(4,8))

# def my_max(a,b):  #v1
#     if a>b:
#         print(a)
#     else:
#         print(b)

# my_max(9,6)


# def my_max(a,b):    #v2
#     if a>b:
#         return a
    
#     return b


# x=my_max(9,6)
# print(x)
# print(my_max(4,6),12) # 3 саннын макс табу 






# def my_max(*args):   #v3 сонгы накты версиясы 
#     mx=args[0]   
#     for el in args:
#         if el>mx:
#             mx=el
#     return mx

# print(my_max(4,5,68,9,456,81))









# def one_to_n(number):
#     ans=[]
#     for i in range(1,number+1):
#         ans.append(i)
#     return ans

# print(one_to_n(5))    # 1 2 3 4 5 
# print(one_to_n(5)[2]) ## 3 шгады 
# print(one_to_n(10))








# def print_list(arr,i=0, j=-1):
#     if j==-1:
#          print(*arr[i:])
#     else:
#          print(*arr[i:j])

# x=[2,6,812,3,4864,123]

# print_list(x,1,3)







# x=5

# def test():
#     global x  ###  x айнымалыны озгертуге лицензия
#     x*=3 
# test()
# print(x)





# def has_negative(arr):  ##терис сан бар ма соны тексеру 
#     for el in arr:
#         if el<0:
#             return True

#     return False

# x=[int(el) for el in input().split() ]

# print(has_negative(x))   











### CW 15 
###Easy A 

# def text():
#     print("hi there,Im using WhatsApp")

# text()



####Easy B 

# def a(age):
#     print(f"I am {age} years old")

# n=int(input())

# a(n)





###Easy C 
# def a(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")

# n=int(input())

# a(n)


###Easy D 

# def my_sum(x):
#     sm=0
#     for i in range(x+1):
#         sm+=i
#     return sm

# print(my_sum(5))




####Medium A 

# def  have_digit(text):
#     for el in text:
#         if el.isdigit():
#             return "cool"
        
#     return "hot"
# n=input()
# print(have_digit(n))


####Medium B 

# def  is_prime(x):
#     if x>=2:
#         cnt=0
#         for i in range(1,x+1):
#             if x%i==0:
#                 cnt+=1
#         if cnt>2:
#             return False
#         else:
#             return True
#     else:
#         return True

# n=int(input())    
# print(is_prime(n))




############HW 15
####Easy A 

# def power(a, n):
#     return(a**n)

# a=int(input())
# n=int(input())
# print(power(a,n))


########Easy B 

# def is_year_leap(year):
#     if (year%4==0 or year%400==0) and year%100!=0:
#         print("True")
#     else:
#         print("False")

# n=int(input())
# is_year_leap(n) 



######## Medium A   30/18 ost=12          18/12  ost=6      12/6 ost=0    nod=6      
# def NOD(a,b):
#     if a<b:
#         a,b=b,a
#     ost=0
#     while True:
#         ost=a%b
#         if ost==0:
#             return b
#         a=b
#         b=ost

# a=int(input())
# b=int(input())

# print(NOD(a,b))


#####Medium B 

# def mas(arr):
#     sum=0
#     len=0
#     for el in arr:
#         sum+=el
#         len+=1
#     return sum/len


# x=[int(el) for el in input().split()]

# print(mas(x))



##sort жане sorted 

# arr=["abc","16551","decode","pythonlang"]
                                                         
# arr.sort(key=len,reverse=True) ###узындыктары бойынша 
#                 ##керисинше шгару


####max   min
# print(min(arr,key=len))
# print(max(arr,key=len))









#####Hard A 

# def sum_of_digit(num):
#     ans=0
#     while num!=0:
#         ans+=num%10
#         num//=10
    
#     return ans


# arr=[int(el) for el in input().split()]

# print(*sorted(arr,key=sum_of_digit))


    

######Hard B 


# def my_reverse(arr):
#     return arr[::-1]

# arr=input().split()

# print(*my_reverse(arr))


