# x=5 

# arr=[123,456,789]

# d={
#     'python':5,
#     'pip':22,
#     'decode':4
# }


# def summa(a,b):
#     return a+b


# if __name__=="__main__":
#     print(summa(45,87))



####Hard A



from cgitb import text


def sum_index(arr):
    mx=max(arr)
    mn=min(arr)
    
    return arr.index(mx)+arr.index(mn)



#### Easy A 

var = [13, 4, 7, 5, 6, 9]


######Easy B 

Student={
    'name':'Aidana',
    'age':21,
    'gpa':3.88

}


####Medium A 
def my_reverse(text):
    return text[::-1] 








########HW 18 
##Medium A 
def summ(num):
    sum=0
    while num>0:
        a=num%10
        sum+=a
        num//=10
    return sum




