import os
import sys
import time
import random
import datetime


money = 100
currency = "$"
win = False
Loose = False

#functions.getBet()

from ctypes import *
windll.Kernel32.GetStdHandle.restype = c_ulong
h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

def color(c): #setconsoletextcolor
	windll.Kernel32.SetConsoleTextAttribute(h,c)

def colorLine(c, s): #Win color text
	#os.system("cls")
	color(c)
	print("*" * (len(s) +2))
	print(" " + s)
	print("*" * (len(s) +2))


def choice():
	colorLine(11, 'Желаете еще раз сыграть? 1 - да, 2 - нет')
	choiceAgain = int(input('>>> '))
	if ((choiceAgain < 0) or (choiceAgain > 2)):
		startGame()
	elif(choiceAgain == 2):	
		writeMoney()
		startGame()
	elif (choiceAgain == 1):
		getDice()

def writeMoney():
	global money
	f = open("money.dat", "w", encoding="utf-8")
	f.write(str(money))
	f.close()

def readMoney():
	f = open("money.dat", "r", encoding="utf-8")
	moneyStatus = int(f.readline())
	f.close()
	
	return print(moneyStatus)

def getDice():
	
	global money
		
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
		color(10)
		print('Покер!')
		win = True
		money = money + 100
		print(F'Вы выиграли комбинацию покер. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((a == y == z) or (a == x == y) or (a == y == z)):
		color(10)
		print('три одинаковых!')
		win = True
		money = money + 600
		print(F'Вы выиграли комбинацию Три одинаковых. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((a == b == z) or (a == b == y) or (a  == b == z)):
		color(10)
		print('три одинаковых!')	
		win = True
		money = money + 500
		print(F'Вы выиграли комбинацию Три одинаковых. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((b == x == y) or (b == x == z) or (b  == y == z)):
		color(10)
		print('три одинаковых!')	
		win = True
		money = money + 500
		print(F'Вы выиграли комбинацию Три одинаковых. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((a == b) or (b == x) or (x == y) or (y == z) or (a == x) or (a == y) or (a == z)):
		color(10)
		print('Одна пара!')
		win = True
		money = money + 5
		print(F'Вы выиграли комбинацию Одна пара. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((b == y) or (b == z) or (z == x)):
		color(10)
		print('Одна пара!')	
		win = True
		money = money + 5
		print(F'Вы выиграли комбинацию Одна пара. Ваш выигрыш составил {money, currency}')
		choice()
	elif (((a == b) and (x == y)) or ((b == x) and (y == z)) or ((a == x) and (x == z))):	
		color(10)
		print('Две пары!')	
		win = True
		money = money + 15
		print(F'Вы выиграли комбинацию Две пары. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((a == x) and ((b == y) or (a == z))):	
		color(10)
		print('Две пары!')
		win = True
		money = money + 15
		print(F'Вы выиграли комбинацию Две пары. Ваш выигрыш составил {monew, currency}')
		choice()
	elif (a == b == x == z):		
		color(10)
		print('Четыре одинаковых!')
		win = True
		money = money + 50
		print(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {money, currency}')
		choice()
	elif (a == y == b == x):		
		color(10)
		print('Четыре одинаковых!')
		win = True
		money = money + 50
		print(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {money, currency}')
		choice()
	elif (a == b == z == y):		
		color(10)
		print('Четыре одинаковых!')
		win = True
		money = money + 50
		print(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {money, currency}')
		writeMoney()
		choice()
	elif (a == z == b == x):		
		color(10)
		print('Четыре одинаковых!')	
		win = True
		money = money + 50
		print(F'Вы выиграли комбинацию Четыре одинаовых. Ваш выигрыш составил {money, currency}')		
		choice()
	elif ((a != b != x != y != z) and (a != 6 and b != 6 and x != 6 and y != 6 and z != 6)):	
		color(10)
		print ('Первый стрит')	
		win = True
		money = money + 25
		print(F'Вы выиграли комбинацию Первый стрит. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((a != b != x != y != z) and (a != 1 and b != 1 and x != 1 and y != 1 and z != 1)):	
		color(10)
		print ('Второй стрит')
		win = True
		money = money + 25
		print(F'Вы выиграли комбинацию Второй стрит. Ваш выигрыш составил {money, currency}')
		choice()
	elif ((a == b == x) and (y == z)):
		color(10)
		print ('Флешрояль!')
		win = True
		money = money + 75
		print(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {money, currency}')	
		choice()
	elif ((a == x == y) and (z == b)):
		color(10)
		print ('Флешрояль!')	
		win = True
		money = money + 75
		print(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {money, currency}')	
		choice()
	elif ((a == y == z) and (b == x)):
		color(10)
		print ('Флешрояль!')
		win = True
		money = money + 75
		print(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {money, currency}')				
		choice()
	elif ((a == b == z) and (y == x)):
		color(10)
		print ('Флешрояль!')		
		win = True
		money = money + 75
		print(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {money, currency}')	
		choice()
	elif ((a == b == y) and (x == z)):
		color(10)
		print ('Флешрояль!')
		win = True
		result = money + 75
		print(F'Вы выиграли комбинацию Флешрояль. Ваш выигрыш составил {money, currency}')	
	elif ((a != b != x != y != z)):
		if((resultDice >= 20) and (resultDice >= 30)):
			color(10)
			print (F'Удачный Шанс! {resultDice}')			
			money = money + (resultDice * 5)
			choice()
		else:
			color(12)
			print (F'Неудачный Шанс! {resultDice}')
			money = money - (resultDice * 5)
			choice()
						
def startGame():
	
	switch = True
	colorLine(14, 'Добро пожаловать в игру \"Покер на костях\" Ваш баланс \n')
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

startGame()
