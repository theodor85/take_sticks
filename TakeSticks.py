#-*-coding: utf-8 -*-

import random
import codecs, sys
outf = codecs.getwriter('utf-8') (sys.stdout, errors = 'replace')
sys.stdout = outf

# шапка и приглашение
def Head():
    print u"**********************************************************"
    print u"************* Игра с палочками ***************************"
    
def Menu():
    print u"\n1 - Начать новую игру"
    print u"2 - Правила игры"
    print u"Любая другая клавиша - выход"
    return raw_input("-->")

# правила игры
def Rules():
    print u""" Правила игры:
Правила игры заключаются в том, что нужно забирать от 1 до 3-х палочек.
Проигрывает тот, кто заберет последнюю палочку.
Нажмите Enter для продложения
"""
    raw_input()

# функция определяет, кто первый ходит. 1 - человек, 0 - комп.
def WhoTheFirst():
    if random.random() <= 0.5:
        return 0
    else: return 1     

# функция выводит палочки с помощью псевдографики
def SticksPrint(sticks):
    print '\n'
    for i in range(0, sticks):
        print '|',

# действия человека
def Man():
    ToTake = 0
    while True:
        try:
            ToTake = int(raw_input(u"Ваш ход: "))
        except:
            print u"Ошибка! вы должны ввести число от 1 до 3."
        if 1 <= ToTake <= 3:
            break
        else:
            print u"Ошибка! вы должны ввести число от 1 до 3."
    return ToTake

# алгоритм компьютера для выбора количества палочек на своём ходу
def GenerateToTake(sticks):
    # если число палочек 4n+1, тогда выбраем любое число
    # иначе, делаем так, чтобы сопернику досталось 4n+1
    n = (sticks-1)%4 
    if n == 0:
        return int( round(2*random.random() + 1) )
    else:
        return n 

# действия компьютера
def CPU(sticks):
    ToTake = GenerateToTake(sticks)
    print u"Ход CPU: %d" % ToTake
    return ToTake 

# тело игры
def Game():
    # начальные установки: генерируется окличество палочек, 
    sticks = int( round(10*random.random() + 15) )

    # определяется, кто первый ходит
    first = WhoTheFirst()
    
    print u"Здесь начинается игра."
    print u"Прервым ходит %d.\n"%first   
    
    while sticks > 0:        
        token = 0
        if first == 1:

            SticksPrint(sticks)
            print u"\nКoличество палочек сейчас: %d" % sticks

            token = Man()
            sticks = sticks - token
            if  sticks<= 0:
                print u"\nУвы! Вы проиграли!" 
                break 

            SticksPrint(sticks)
            print u"\nКoличество палочек сейчас: %d" % sticks

            token = CPU(sticks)
            sticks = sticks - token
            if  sticks<= 0:
                print u"\nПоздравляем! Вы победили!" 
                break
        else: 

            SticksPrint(sticks)
            print u"\nКoличество палочек сейчас: %d" % sticks

            token = CPU(sticks)
            sticks = sticks - token
            if  sticks<= 0:
                print u"\nПоздравляем! Вы победили!" 
                print u"Нажмите Enter для продложения."
                raw_input()
                break

            SticksPrint(sticks)
            print u"\nКoличество палочек сейчас: %d" % sticks

            token = Man()
            sticks = sticks - token
            if  sticks<= 0:
                print u"\nУвы! Вы проиграли!" 
                print u"Нажмите Enter для продложения."
                raw_input()
                break 


# глобальная программа
Head()

while True:
    command = 0
    try:
        command = int(Menu())
    except:
        command = 0
    
    if command == 0:
        break
    elif command == 1:
        Game()
    elif command == 2:
        Rules()
    else: break


