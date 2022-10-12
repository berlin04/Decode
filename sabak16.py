###рекурсия 

# def rec():
#     print("hello")
#     rec()

# rec()


# def one_to_n(num,i=1):
#     print(i,end=" ")

#     if i==num:
#         return
#     else:
#         one_to_n(num,i+1)


# n=int(input())

# one_to_n(n)








# def reverse_print(arr,i=-1):
#     print(arr[i],end=" ")
#     if i*(-1)==len(arr):
#         return
#     else:
#         reverse_print(arr,i-1)


# arr=input().split()
# reverse_print(arr)









# def one_to_n(num):
#     if num==1:
#         return 1
#     else:
#         return one_to_n(num-1)+num

# num=int(input())

# print(one_to_n(num))






# def factorial(num):
#     if num==0 or num==1:
#         return 1
#     else:
#         return factorial(num-1)*num

# num=int(input())
# print(factorial(num))







# def sum_of_array(arr):
#     if len(arr)==0:        ##базовый случай 
#         return 0 
#     elif len(arr)==1:      #базовый случай
#         return arr[0]
#     else:
#         return arr[0]+sum_of_array(arr[1:])        #рекурсивный случай 

# arr=[7, 9, 10]

# print(sum_of_array(arr))







####cw 16 
##Easy B 

# def n_to_one(num,i=1):
#     print(num,end=" ")
#     if num==i:
#         return
#     else:
#         return n_to_one(num-1)


# num=int(input())
# n_to_one(num)




###Easy C
 

# def a(m,n):
#     if m==0:
#         return n+1
#     elif m>0 and n==0:
#         return a(m-1,1)
#     else:
#         return a(m-1,a(m,n-1))

# m=int(input())
# n=int(input())

# print(a(m,n))





#####Medium A 


# def my_sum(num):
#     if num==0:
#         return 0
    
#     return num%10+my_sum(num//10)

    
# n=int(input())
# print(my_sum(n))


# def my_sum(arr,i=0):
#     if len(arr)==0:
#         return 0
#     elif len(arr)==1:
#         return arr[0]
#     else:   
#         return arr[i]*my_sum(arr[1:]) 
    

# arr=[int(el) for el in input().split()]

# print(my_sum(arr))



## s[10,15,13,5]=10*s[15,13,5]
## s[15,13,5]=15*s[13,5]
## s[13,5]=13*s[5]
## s[5]=5




######Medium C 


# def step(num):
#     if num==1:
#         print("Yes")
#         return
#     elif num<1:
#         print("NO")
#         return
#     step(num/2)

# num=int(input())
# step(num)




####HW 16 

# #####Easy A 

# def rev(num):
#     if num>0:
#         print(num%10,end="")
#         rev(num//10)

# n=int(input())
# rev(n)
 


######Medium A 

# def power(x,y):
#     if y==0:
#         return 1

#     return x*power(x,y-1)

# x=int(input())
# y=int(input())

# print(power(x,y))


## power(3,4)=3*power(3,3)
## power(3,3)=3*power(3,2)
## power(3,2)=3*powe(3,1)
## powe(3,1) =3*power(3,0)



#####Hard A 
# def func(num,i=1,cnt=0):
#     if num==0:
#         return 
#     elif i==cnt:
#         func(num,i+1,0)
#     else:
#         print(i,end=" ")
#         func(num-1,i,cnt+1)
        

# n=int(input())
# func(n)

