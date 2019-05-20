# -*- coding: UTF-8 -*-
import datetime,sys
from openpyxl import Workbook, load_workbook



data = []


while True:
	money = input(">>輸入金額 ")
	item_name = input(">>輸入細目 ")
	print('\n金額:{}, 細目:{}'.format(money, item_name))
	double_check = input('>>確認? y or n  ')

	if double_check == "y":
		data.append(item_name)
		data.append(int(money))
		data.append(datetime.datetime.now())
		wb = load_workbook(r"C:\Users\re438\Dropbox\un_finished\ben_expense.xlsx")
		ws = wb.active
		ws.append(data)
		wb.save(r"C:\Users\re438\Dropbox\un_finished\ben_expense.xlsx")
		sys.exit()
	elif double_check == "n":
		print('再輸入一次吧')
	else:
		print("請輸入y or n")



	
