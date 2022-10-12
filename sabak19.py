

# s=input()
# pattern = r'^decode'

# print(bool(re.search(pattern,s)))  ###берген паттерн бар ма жок па тексеред  



# s=input()
# pattern = r'decode$'

# print(bool(re.search(pattern,s)))





# s=input()
# pattern = r'\.(jpg|png|svg)$'

# print(bool(re.search(pattern,s)))



# s=input()
# pattern = r'^[a-zA-Z]+$'

# print(bool(re.search(pattern,s)))




# s=input()
# pattern = r'[!@#\$%\^\*]' 

# print(bool(re.search(pattern,s)))





# s=input()
# pattern = r'^[^!@#\$%\^\*]$' 

# print(bool(re.search(pattern,s)))




# s=input()
# pattern = r'^[0-9]+\$?$'

# print(bool(re.search(pattern,s)))



# s=input()
# pattern = r'^[0-9]+\$?$'

# print(bool(re.search(pattern,s)))



# s=input()
# pattern = r'^[0-9]+\$*$'

# print(bool(re.search(pattern,s)))


# ? [0,1]
# + [1,inf)
# * [0,inf)




# s=input()
# pattern = r'^[0-9]{3}$'

# print(bool(re.search(pattern,s)))




# s=input()
# pattern = r'^[0-9]{2,4}$'

# print(bool(re.search(pattern,s)))



# s=input()
# pattern = r'^[0-9]{2}/[0-9]{2}/([0-9]{4})$'

# res=re.search(pattern,s)

# print(res.group(0)) 
# # print(res.group(1))




#####ФУНКЦИИ 


# s=input()

# print(re.findall(r'\b\d{2}\b',s))        ####барин тауып беред бир массивке салып 




# s=input()
# print(re.split(r'[0-9]',s))                ####болип береды белгили бир символмен 




# s='HelloWorld'

# print(re.sub(r'[A-Z]',r'_',s))                 ####  ауыстыру ушин мысалы улкен ариты нижни пробелге








#CW 19 
##Easy A 

# import re 

# pattern=r'\d'
# s=input()
# print(bool(re.search(pattern,s)))


##Easy B 

# import re 

# pattern=r'^[a-zA-Z0-9]+$'
# s=input()
# if re.search(pattern,s):
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")


###Easy C

# import re
# pattern= r'[A-Z][a-z]+'
# s=input()
# if re.search(pattern,s):
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")



##Medium A 

# import re
# s=input()

# pattern=r'cool$'

# print(bool(re.search(pattern,s)))



## Medium B 
# import re
# s=input()

# pattern=r'^a.+b$'

# if re.search(pattern,s):
#     print("Нашел совпадение!")
# else:
#     print("Не нашел совпадение!")



###Medium C 

# import re
# s=input()

# pattern=r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
# if re.search(pattern,s):
#     print("IP")
# else:
#     print("SOMETHING ELSE")



##Hard A 
# import re
# s=input()
# pattern= r'^(87|77)\d{9}$'
# if re.search(pattern,s):
#     print("call me")
# else:
#     print("SOMETHING ELSE")










######HW 19
#Easy A 
# import re 
# s=input()
# pattern=r'[0-9]{2}\-[0-9]{2}\-[0-9]{4}'

# print(re.findall(pattern,s))

#Easy B 
# import re 
# s=input()
# pattern=r'\b[AEOIUaeoiu][A-Za-z]+\b'
# print(re.findall(pattern,s))


##Medium A 
# import re 
# s=input()
# pattern=r'[0-9]$'

# print(True if re.search(pattern,s) else False)


##Medium B 
# import re
# s=input()

# pattern=r'[0-9]+'

# res=re.search(pattern,s)

# print(res.group(0))
# print("Индекс:",res.start())



###Hard A
# import re 
# s=input()
# pattern=r'\b[A-Za-z]{5}\b'
# print(re.findall(pattern,s))


###Hard B 
# import re
# s=input()

# s=re.sub(r'([A-Z])',r'_\1',s)[1:].lower()

# print(s)


