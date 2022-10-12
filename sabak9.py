#индекс    0        1      2       3      4
names=   ["Alan","Erlan","Abay","Серик","Nurtas"]
#           -5      -4       -3      -2     -1
# print(names[2])
# print(names[-1])

# print(len(names)) #узындыгын корсетеды 

# for i in range(len(names)):
#     print(names[i])


# for el in names:
#     print(el)


# slice-срез
# print(names[0:5:2])
#[бастау:токтау:кадам]

# print(names[::-1]) #керисинше карастыру



# Тизимге колданылатын операциялар 
# print([1,2,3]*3)
# print([1,2,3]+[7,8,9])

#split()- текстты пробел аркылы болеД, боликтерды тизимге толтырады 
# arr=input().split()   # тексттер тизимин енгизу 

# for i in range(len(arr)):   # инт ке айналдыру 1 вариант
#     arr[i]=int(arr[i])
# print(arr)


# arr=[int(el) for el in input().split()]    # инт ке айналдыру  2 вариант



# list()- аудармашы функция    
# arr=[]
# arr1=list()
# print(arr,arr1)


# map()-барлыгын бир типке айналдырады 
# ["2",2, 2.8]
#int 
# arr=list(map(int,input().split()))
# print(arr)



#Тизимнин методтары 

arr=[1,2,3,4]
arr.append(7)  # сонынан бир элемент косу
print(arr)

arr.insert(0,5) # (кай жерге косу,  кандай элемент косу)
print(arr)

arr.insert(2,9)
print(arr)

arr.extend([5,6,7]) # артынан бирнеше элемент косу немесе баска массив элементтерын осы массивке косу 
print(arr)



names=   ["Alan","Erlan","Abay","Серик","Nurtas"]
names.pop(3) # индекс бойынша алып тастау 
print(names)


# names.remove("Серик") #элементтын мани бойынша жою
# print(names)


a=[0,8,9]
# b=a   # булай жасасак екеуине бир бирине тауелды болып калады
# print(b)
# b=a.copy() # коширмесин жасау

a.clear() # букил элементтерды тазарту

a=[4,7,8,14,15,28,65,19]
# print(a.count(4))  # берилген элементтын неше рет кездесетинин санап береды 

a=['x','y','z','k']
print(a[2])          # индекс бойынша элемент табу 
print(a.index('z'))  # элемент бойынша индекс табу

a=[4,7,8,14,15,28,65,19]
a.sort()   #  кишисинен бастау сорттау
print(a)
a.reverse #   керисинше шгару массивты 

