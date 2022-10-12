# text='decode'
# print(text[0]) 
# print(text[2:])


#
# string='python'
# for char in string:
#     print(char)

#len
# a="mac book"
# for i in range(len(a)):
#     print(string[i])


#форматирование
# a=input()
# b=input()

# print(f" dfasdfsffsa {a}  {b} ")


#методы

# text='decode'

# print(text.index('c'))
# print(text.find('c'))  # тауып беред таппаса -1 шгад 

# print(text.count('e')) 

# text.replace('d','D') #озгертед d ны D га  Decode 

# text='decode'
# print(text.upper())  # Улкен кылады букваларды 
# print(text.lower())  # киши кылады букваларды
print('TemIrlLan SaIRov'.capitalize()) #бастапкы арипты улкен кылтып содан кейн калганын киши кылады 
print('TemIrlLan SaIRov'.title())      # пробелдерды бас ариптермен жазад

#is



print('Abfsf'.isupper()) #False
print('QWE'.isupper())     #True
print('dsfsa'.islower())   #True

print('123'.isdigit()) #тек кана сандардан тура ма соны тексеред
print('Dec0de'.isalpha())  #тек кана ариптерден тура ма соны тексеред

a="   dfasfa  " 
print(a.strip())   #пробелдерды жояды ягни жакша ишиндегыны жояды 



# with list 

text="decode school python"
print(text.split())  # массивке толтырады 


data='8/17/22'
print(data.split('/'))

time='18:26:21'
print(time.split(":"))



arr=["decode", "is","cool"]
print(" ".join(arr))   #строкага айналдырып береды


arr=["decode",5,False]
print(" ".join([int(el) for el in arr]))  # барлыгын строкага айналдырады

















