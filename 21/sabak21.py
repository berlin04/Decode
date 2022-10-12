##### mod 'x' 

# file=open('test.txt','x')  ##файл ашу ушин
# file.close()

##### mod 'r'

# file=open('test.txt','r')   ##файл оку ушин 


#v1 
# print(file.read())

#v2
# print(file.readline())       # ар жолды жеке окиды бириншы жолды 
# print(file.readline())       # ар жолды жеке окиды екинши жолды
# print(file.readline())       # ар жолды жеке окиды ушинши жолды 

#v3 
# print(file.readlines())       #ар жолдв массивке сактауга болады 

# file.close()





#### mod 'w'
 
# file=open('test.txt','w')
# file.write('file_manager')        #перезапись ягни ишиндегы барлыгы оширилип сосын осы соз жазылдаы 

# file.close()


####  mod  'a'

# file=open("test.txt",'a')         ###дозапись ягни ишиндегы оширилмейд 

# file.write("\nfile_manager")
# file.write("\npython")
# file.write("\nabay")



######модуль os,shutil 

# import os 
# import shutil
# os.rename("test.txt",'abc.txt')   ## файл мен папка атын озгертуге 

# os.remove('abc.txt')    ## файл оширу ушин 

# shutil.rmtree("test_folder")   ### папка оширу ушин 

# os.mkdir('folder')             ## папка косу ушин 

# shutil.copy('test.txt','text_copy.txt')    #копия жасау ушин 

# shutil.move('text_copy.txt','folder')    ### бир файлды баска папкага салу ушин 






## CW 21 
# Easy A 

# file=open('task1.txt','x')  ##файл ашу ушин
# file.close()



# Easy B 

# import os 
# os.remove('task1.txt')



# Easy C 

# s=input()
# format=input()

# file=open(f"{s}.{format}",'x')
# file.close()



# Easy D 
# import os
# s=input()

# try:
#     os.remove(s)
#     print(f"Файл {s} успешно удален!")
# except:
#     print(f"Файл {s} не найден!")



# Medium A 
# import os 
# name=input()
# new_name=input()

# try:
#     os.rename(name,new_name)
#     print("done")
# except:
#     print("error")




##Medium B 



# file=open("main.txt",'a') 

# num=int(input())

# for i in range(num):
#     text=input()
#     file.write(text+" ")

# file.close()


##Medium C 
# file=open("main.txt",'a') 

# num=int(input())
# file.write("\n")
# for i in range(num):

#     text=input()
   
#     file.write(text+" ")

# file.close()



#### Hard A 

# file=open('hardA.txt','r')

# for i in range(5):
#     print(file.readline().upper(),end="")










#######HW 21

###Easy 

# def file_exist(file_name):
#     try:
#         file= open(file_name,'r')
#         file.close()
#         return True
#     except:
#         return False




# while True:
#     file_name=input()
#     if file_exist(file_name)==True:
#         break
#     else:
#         print("Файл не найден попробуйте еще раз")


# file= open(file_name,'r')

# for i in range(5):
#     print(file.readline())

# file.close()



#####Medium 

# file= open('ethics.txt','r')

# lines=file.readlines()

# print("Нечетные линий:")
# for line in lines[::2]:
#     print(line.strip('\n'))

# print("Четные линий:")
# for line in lines[1::2]:
#     print(line.strip('\n'))

# file.close()





#####Hard 
# import os 
# import shutil
# file= open('ethics.txt','r')
# new_file=open('new_ethics.txt',"w")


# for i in range(6):
#     new_file.write(file.readline())


# file.close()
# new_file.close()

# for i in range(1,4):
#     shutil.copy('new_ethics.txt',f'new_ethics_copy{i}.txt')
#     os.mkdir(f'ethics{i}')
#     shutil.move(f"new_ethics_copy{i}.txt",f"ethics{i}")

# os.remove('new_ethics.txt')








