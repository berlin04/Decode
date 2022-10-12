### двумерный массив 


# print(arr[1][-1])  ## n 

from math import radians


arr=[[1,2,3],[4,5,6],[7,8,9]]

# print(arr[2][0])  ## 7 
# print(len(arr))     #  3
# for row in arr:
#     print(*row)


###### итерация 

# for row in arr:
#     for el in row:
#         print(el**2,end=" ")
#     print()



# for i in range(len(arr)):  ##индекс бойынша 
#     for j in range(len(arr[i])):
#         print(arr[i][j]*2,end=" ")
#     print()



### сумма
# ans=0
# for row in arr:
#     ans+=sum(row)

# print(ans)



####генерация 


#####1variant
# arr=[]
# for i in range(3):
#     arr.append([0]*5)
# arr[1][1]=5

#####2variant 
# arr=[[0]*5 for i in range(3)]
# arr[1][1]=5



######input

# n,m=map(int,input().split())

# arr=[]
# for i in range(n):
#     x=[int(el) for el in input().split()]
#     arr.append(x)

# for row in arr:
#     print(*row)



###### практика 

# n=int(input())
# arr=[['x']*n for i in range(n)]


# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i==j:
#             arr[i][j]=1
#         elif i>j:
#             arr[i][j]=2
#         elif i<j:
#             arr[i][j]=0    
            
# for row in arr:
#     print(*row)

# n,m=map(int,input().split())

# arr=[["x"]*m for i in range(n)]

# # for i in range(len(arr)):
# #     for j in range(len(arr[i])):
# #         arr[i][j]=i*j

# # for row in arr:
# #     print(*row)
# print(arr)

####CW 14 
#### Easy B
# arr=[]
# for i in range(2):
#     x=[int(el) for el in input().split()]
#     arr.append(x)
# print(arr)


#####Easy C 
# n=int(input())
# arr=[]
# for i in range(n):
#     x=[int(el) for el in input().split()]
#     arr.append(x)
# cnt=0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]<0:
#             cnt+=1

# print(cnt)



#### Easy D 
# n,m=map(int,input().split())
# arr=[]
# for i in range(n):
#     x=[int(el) for el in input().split()]
#     arr.append(x)

# for i in range(len(arr)):
#     print(*arr[i][::-1])


#####Medium A 
# n,m=map(int,input().split())
# arr=[]
# for i in range(n):
#     x=[int(el) for el in input().split()]
#     arr.append(x)
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if (i+j)%2==0:
#             arr[i][j]+=1
#         else:
#             arr[i][j]-=1

# for row in arr:
#     print(*row)


####Medium B 
# n,m=map(int,input().split())

# arr=[]
# for i in range(n):
#     x=[int(el) for el in input().split()]
#     arr.append(x)
# mx=max(arr[0])

# for row in arr:
#     max_of_row=max(row)
#     if max_of_row>mx:
#         mx=max_of_row
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]==mx:
#             print(i,":",j)




###Medium C
# arr=[]
# for i in range(8):
#     x=input().split()
#     arr.append(x)

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]=="x":
#             arr[i][j]='x'
#             arr[i-1][j]='x'
#             arr[i+1][j]='x'
#             arr[i][j+1]='x'
#             arr[i][j-1]='x' 
# for row in arr:
#     print(*row)





 #####HW 14 

 ####Easy A 
# arr=[]
# n,m=map(int,input().split())
# for i in range(n):
#     x=[int(el) for el in input().split()][:m]
#     arr.append(x)
# mx=arr[0][0]
# a,b=0,0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j]>mx:
#             mx=arr[i][j]
#             a,b=i,j
# print(a,b)


####Medium A 

# arr=[]
# n,m=map(int,input().split())
# for i in range(n):
#     x=[int(el) for el in input().split()][:m]
#     arr.append(x)

# for row in arr[::-1]:
#     print(*row[::-1])


#####Hard C 
# n=int(input())
# arr=[['.']*n for i in range(n)]

# for i in range(n):
#     arr[i][i] = '*'
#     arr[n // 2][i] = '*'
#     arr[i][n // 2] = '*'
#     arr[i][n - i - 1] = '*'
# for row in arr:
#     print(*row)


