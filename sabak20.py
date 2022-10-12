import re 
###CW 20
#Easy A 
# s=input()

# pattern=r'[0-9]+'

# res=re.sub(pattern,r'',s)

# print(res)



##Easy B 
# s=input()

# pattern=r'\b[a=zA-z]+\b'

# print(re.split(r'[\.,\s]',s))




##Easy C 
# s=input()

# pattern=r'^the|The'

# print('Нашел совпадение' if re.search(pattern,s) else 'Не нашел совпадение ')



##Medium A 

# s=input()
# pattern=r'decode'
# text=s.lower()
# if re.search(pattern,text):
#     res=re.search(pattern,text)
#     print(res.start())
#     print(res.end())
# else:
#     print('Совпадений нет!')


###Medium B 
# s=input()
# pattern=r'^(https|http)://[a-z]+\.[a-z]+/?$'

# print(bool(re.search(pattern,s)))



####HW 20 

#Easy A 

# s=input()

# pattern=r'^([0-9]{4})/([0-9]{2})/([0-9]{2})$'

# res=re.search(pattern,s)

# year=int(res.group(1))
# if year>=1000 and year<=2012:
#     print("yes")
# else:
#     print("no")



#Easy B 






###Medium A 
# s=input()

# s=re.sub(r'\b[Aa]([a-zA-Z]+)[Aa]\b',r'!\1!',s)
# print(s)



###Medium B 
# s=input()

# words=re.findall(r'\b[a-zA=Z]+\B',s)
# cnt=0

# for word 

    

##Hard A 

# s=input()
# patt=r'^\+7(747|707)[0-9]{7}$'

# if re.search(patt,s):
#     print("hello")
# else:
#     print("declined")


