# # Задача Д 
# # easy
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     a=int(input())
#     if a%10==8:
#         sum+=1
# print(sum)

# n=int(input())
# x=int(input())
# a=x
# for i in range(1,n+1):
    
#     print(a,end=" ")
#     a+=x
    
# a=int(input())
# b=int(input())
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print(sum)



# n=int(input())
# for i in range(1,n+1):
#     print(" "*(n-i),"*"*i,sep="")
   

# n=int(input())
# nuli=0
# for i in range(n):
#     x=int(input())
#     while x > 0:
#         if x%10==0:
#             nuli+=1
#         x //= 10
# print(nuli)




# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     for c in range(2,a-1):
#         if a%c==0:
#             continue
#         print(i,end=" ") 

# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if i**2>b:
#         continue   
#     print(i**2)


# a=int(input())
# for i in range(1,a+1):
#     if a%i==0:
#         print(i,end=" ")   
 
nuli=0
polozh=0
otr=0
n=int(input())
for i in range(n):
    a=int(input())
    if a>0:
        polozh+=1
    elif a<0:
        otr+=1
    else:
        nuli+=1
print(nuli,polozh,otr,sep="\n")


    
    
    


           
    
        

    
 
    

   