#импорт библиотек
#Некоторые особенности игры будут реализованы позже

import os
import sys
import time
import random
import datetime

#Библиотека раскрашивания символов в линукс-консоли
import termcolor


#Объявление переменных

money = 50
currency = "$"
win = False
Loose = False

text = ""

#Функции раскраски текста

def colorPosixLine(text): #Linux color text
	termcolor.cprint(text, 'yellow')
	
def colorWin(text): #Linux color text
	termcolor.cprint(text, 'green')
			
def colorLoose(text): #Linux color text
	termcolor.cprint(text, 'red')
	
def colorChoice(text): #Linux color text
	termcolor.cprint(text, 'blue')	

#Функция покера на костях, пока без анимации	
#конструкция if elif громоздкая, так как нужно проверить множество выигрышных условий	
def getDice():
		
	a = random.randint(1,6)
	b = random.randint(1,6)
	x = random.randint(1,6)
	y = random.randint(1,6)
	z = random.randint(1,6)
			
	print(" " * 8, "----------------------")
	print(" " * 10, f'|{a}| |{b}| |{x}| |{y}| |{z}|')
	print(" " * 8, "----------------------")
	
	resultDice = a + b + x + y + z
	
	if (a == b == x == y == z):
		print('Покер!')
		win = True
		result = money + 100
		colorWin(F'Вы выиграли комбинацию покер. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((a == y == z) or (a == x == y) or (a == y == z)):
		print('три одинаковых!')
		win = True
		result = money + 60
		colorWin(F'Вы выиграли комбинацию Три одинаковых. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((a == b == z) or (a == b == y) or (a  == b == z)):
		print('три одинаковых!')	
		win = True
		result = money + 60
		colorWin(F'Вы выиграли комбинацию Три одинаковых. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((b == x == y) or (b == x == z) or (b  == y == z)):
		print('три одинаковых!')	
		win = True
		result = money + 60
		colorWin(F'Вы выиграли комбинацию Три одинаковых. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((a == b) or (b == x) or (x == y) or (y == z) or (a == x) or (a == y) or (a == z)):
		print('Одна пара!')
		win = True
		result = money + 5
		colorWin(F'Вы выиграли комбинацию Одна пара. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((b == y) or (b == z) or (z == x)):
		print('Одна пара!')	
		win = True
		result = money + 5
		colorWin(F'Вы выиграли комбинацию Одна пара. Ваш выигрыш составил {result, currency}')
		choice()
	elif (((a == b) and (x == y)) or ((b == x) and (y == z)) or ((a == x) and (x == z))):	
		print('Две пары!')	
		win = True
		result = money + 15
		colorWin(F'Вы выиграли комбинацию Две пары. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((a == x) and ((b == y) or (a == z))):	
		print('Две пары!')
		win = True
		result = money + 15
		colorWin(F'Вы выиграли комбинацию Две пары. Ваш выигрыш составил {result, currency}')
		choice()
	elif (a == b == x == z):		
		print('Четыре одинаковых!')
		win = True
		result = money + 50
		colorWin(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {result, currency}')
		choice()
	elif (a == y == b == x):		
		print('Четыре одинаковых!')
		win = True
		result = money + 50
		colorWin(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {result, currency}')
		choice()
	elif (a == b == z == y):		
		print('Четыре одинаковых!')
		win = True
		result = money + 50
		colorWin(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {result, currency}')
		choice()
	elif (a == z == b == x):		
		print('Четыре одинаковых!')
		win = True
		result = money + 50
		colorWin(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {result, currency}')				
		choice()
	elif ((a != b != x != y != z) and (a != 6 and b != 6 and x != 6 and y != 6 and z != 6)):	
		print ('Первый стрит')	
		win = True
		result = money + 30
		colorWin(F'Вы выиграли комбинацию Первый стрит. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((a != b != x != y != z) and (a != 1 and b != 1 and x != 1 and y != 1 and z != 1)):	
		print ('Второй стрит')
		win = True
		result = money + 30
		colorWin(F'Вы выиграли комбинацию Второй стрит. Ваш выигрыш составил {result, currency}')
		choice()
	elif ((a == b == x) and (y == z)):
		print ('Флешрояль!')
		win = True
		result = money + 70
		print(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {result, currency}')	
		choice()
	elif ((a == x == y) and (z == b)):
		print ('Флешрояль!')	
		win = True
		result = money + 70
		colorWin(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {result, currency}')	
		choice()
	elif ((a == y == z) and (b == x)):
		print ('Флешрояль!')
		win = True
		result = money + 70
		colorWin(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {result, currency}')				
		choice()
	elif ((a == b == z) and (y == x)):
		print ('Флешрояль!')		
		win = True
		result = money + 70
		colorWin(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {result, currency}')	
		choice()
	elif ((a == b == y) and (x == z)):
		print ('Флешрояль!')
		win = True
		result = money + 70
		colorWin(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {result, currency}')	
		choice()
	elif ((a != b != x != y != z)):
		if((resultDice >= 20) and (resultDice >= 30)):
			colorWin(F'Удачный Шанс! {resultDice}')			
			result = money + (resultDice * 25)
			choice()
		else:
			colorLoose(F'Неудачный Шанс! {resultDice}')
			result = money - (resultDice * 50)
			choice()

#Функция выбора игры в покер снова
def choice():
	colorChoice('Желаете еще раз сыграть? 1 - да, 2 - нет')
	choiceAgain = int(input('>>> '))
	if ((choiceAgain < 0) or (choiceAgain > 2)):
		startGame()
	elif(choiceAgain == 2):	
		writeMoney()
		startGame()
	elif (choiceAgain == 1):
		getDice()

#Функция записи результата при выходе из игры
def writeMoney():
	global money
	f = open("money.dat", "w", encoding="utf-8")
	f.write(str(money))
	f.close()

#Метод чтения файла 
def readMoney():
	f = open("money.dat", "r", encoding="utf-8")
	moneyStatus = int(f.readline())
	f.close()
	
	return print(moneyStatus)


#Функция начала игры
def startGame():
	
	switch = True
	colorPosixLine('Добро пожаловать в игру \"Покер на костях\" Ваш баланс \n')
	print(f"{money}, так же в игре можно делать ставки: ")
	print('''Выберете соответствующий пункт меню
	1 - начать игру
	2 - выйти из игры''')
	
	select = int(input('>>> '))
	if ((select < 0) or (select > 2)):
		switch = False
	elif (select == 2):
		switch = False
	elif (select == 1):
		getDice()		

#Инициализация игры
startGame()
