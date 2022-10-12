# i=0
# n=int(input())
# while i<n:
#     print("DeCode")
#     i+=1

# sum=0
# i=1
# n=int(input())
# while i<=n:
#     sum+=i
#     i+=1
# print("Сумма:",sum)

# l=int(input())
# r=int(input())
# while l<=r:
#     if l%2==0:
#         print(l)
#     l+=1

# n=int(input())
# x=1
# while True:
#     if x==n:
#         print("yes")
#         break
#     elif x>n:
#         print("no")
#         break
#     x*=2

    
# n=int(input())
# s=0
# while n>=1:
#     n/=2
#     s+=1
# print(s) 

# x=int(input())
# y=int(input())
# day=1
# while True:
#     x=x+x*0.2
#     day+=1
#     if x>y:
#         print(day)
#         break

n=int(input())
sum=0
while True:
    if n==0:
        print(0)
        break
    x=int(input())
    if x>n:
        sum+=1
    n=x    
    if x==0:
        print(sum)
        break

       
    

        
        
    

    
