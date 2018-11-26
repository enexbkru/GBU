# config : utf-8

import os
import sys
import psutil
import shutil

print ('Hi, Jackson!')
name = input("What's your name?")
print ("Hi, ", name)

answer = ''
while answer != 'q':
    answer = input("Shal we? y/n/q")
    if answer == "y":
        print ("OK")
        print ("1 - вывести инфо о системе")
        print ("2 - список файлов текущей дирректории")
        print ("3 - список ID активных процессов")
        print ("4 - дублирование файлов текущей дирректории")
        print ("5 - удаление дубликатов файлов текущей дирректории")


        do = int(input("Что делаем?  "))

        if do == 1:
            print ("процессоров: ", psutil.cpu_count())
            print ("Платформа: ", sys.platform)
            print ("Пользователь: ", os.getlogin())
        elif do == 2:
            print ("Список файлов: ", os.listdir())
        elif do == 3:
            print ("Списк процессов (ID): ", psutil.pids())
        elif do == 4:
            print("Дублирование файлов указанной дирректории")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]):
                    newfile = file_list[i] + '.dupl'
                    shutil.copy(file_list[i], newfile)
                    i += 1
                else:
                    pass

        else:
            pass

    elif answer == "n":
        print ("Sad")
    else:
        print ("Pitty")
