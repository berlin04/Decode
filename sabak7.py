# for ____ in
# text=input()

# for bukva in text:
#     print(bukva,end=" ")

# i=0
# while i<5:
#     print(i)
#     i+=1



# for i in range(5):
    
#     print(i)  # 0 1 2 3 4 

# for i in range(5,9):
    
#     print(i)   # 5 6 7 8 

# for i in range(5,10,2):
               
#     print(i)   # 5 7 9 
 
 # for i in range(басталуы,соны, кадам)


# print(1,2,3, sep="-")  # араларына символ кою #1-2-3

# print("decode", end="\n")
# print("school", end=" ")   #келесы жолга отуды аныктайды
# print("python")



# n=int(input())
# for i in range(1,n+1):
#     print(i,end=" ")

# l=int(input())
# r=int(input())
# for i in range(r,l-1,-1):
#     if i%2==0:
#         continue
#     else:
#         print(i,end=" ")

# a=int(input())
# b=int(input())
# sum=0
# for i in range(a,b+1):
#     sum+=i
# print(sum)

# a=int(input())
# b=int(input())

#for i in range(a,a*b+1):
#     if i%a==0 and i%b==0:
#         print(i)
#         break

a=int(input())
b=int(input())
x=int(input())
for i in range(a,b+1):
    for c in range(10):
        if (i/10)+c==x:
            
            print(i+c,end=" ") 

