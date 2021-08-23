#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
import tkinter
from tkinter import filedialog
import rakudaCommand

def file_select():
  idir = 'C:\\python_test'
  
  filetype = [("excel","*.xlsx")]
  file_path = tkinter.filedialog.askopenfilename(filetypes = filetype, initialdir = idir)
  filename_input.delete(0,tkinter.END)
  filename_input.insert(tkinter.INSERT, file_path)

def button_click():
        listbox_len = Listbox.size()
        Listbox.delete(0,listbox_len-1)

        ElementValue = getElementValue()
        filename = ElementValue["filename"]
        sheet = ElementValue["sheet"]
        name = ord(ElementValue["name_column"])-ord("@")
        order = ord(ElementValue["order_column"])-ord("@")
        price = ord(ElementValue["price_column"])-ord("@")
        url = ord(ElementValue["url_column"])-ord("@")
        Listbox.insert(0,"データ処理中\nしばらくお待ちください。")
        saveFilename=  filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = [("excel","*.xlsx")])
        if ".xlsx" not in saveFilename:
            print("add .xlsx")
            
            saveFilename=saveFilename+".xlsx"
        rakudaCommand.generateFile(filename,sheet,name,order,price,url,saveFilename)
        ErrorMessage_array = rakudaCommand.getErrorMessage()
        
        if ErrorMessage_array != list():
            for message in ErrorMessage_array:
                Listbox.insert(0,message)
                Listbox.itemconfig(0, {'fg':'red'})
                Listbox.insert(0,"終了")
        else:
            Listbox.insert(0,"completed successfully!!")
        ErrorMessage_array = list()
name_column_value="A"
order_column_value="B"
price_column_value="C"
url_column_value="E"


def getElementValue():
    results = dict()
    results["filename"] = filename_input.get()
    results["sheet"]=sheet_input.get()
    results["name_column"]=name_column_value
    results["order_column"]=order_column_value
    results["price_column"]=price_column_value
    results["url_column"]=url_column_value
    return results

def name_select(value):
    global name_column_value
    name_column_value=value
def order_select(value):
    global order_column_value
    order_column_value=value
def price_select(value):
    global price_column_value
    price_column_value=value
def url_select(value):
    global url_column_value
    url_column_value=value

filename_input=None
sheet_input=None
name_column_input=None
order_column_input=None
price_column_input=None
url_column_input=None

excel_column_list =["A","B","C","D","E","F","G","H"]

root = tkinter.Tk()
root.title(u"rakuda")
root.geometry()
filename_rowStart =0
filename_columnStart =0
#file選択
filename_text  = tkinter.Label(root,text=u'コピー元ファイル:')
filename_input = tkinter.Entry(root)
filename_Button = tkinter.Button(text="参照",command=file_select)

filename_text.grid(row =filename_rowStart,column=filename_columnStart)
filename_input.grid(row=filename_rowStart,column=filename_columnStart+1)
filename_Button.grid(row=filename_rowStart,column=filename_columnStart+2)

sheet_rowStart= filename_rowStart+1
sheet_columnStart = filename_columnStart
#sheetの選択
sheet_input= tkinter.Entry(root)
sheet_text = tkinter.Label(root,text=u' シート名 :')

sheet_text.grid(row=sheet_rowStart,column = sheet_columnStart)
sheet_input.grid(row=sheet_rowStart,column = sheet_columnStart+1)
sheet_input.insert(0,"Sheet1")


column_setting_rowStart = sheet_rowStart+1
column_setting_columnStart = filename_columnStart
#column 設定
variable = tkinter.StringVar()
variable.set(excel_column_list[0])
name_column_text  = tkinter.Label(root,text=u'商品名column:')
name_column_input = tkinter.OptionMenu(root,variable, *excel_column_list,command=name_select)

name_column_text.grid(row = column_setting_rowStart,column=column_setting_columnStart)
name_column_input.grid(row = column_setting_rowStart,column=column_setting_columnStart+1)


order_variable = tkinter.StringVar()
order_variable.set(excel_column_list[1])
order_column_text  = tkinter.Label(root,text=u'数量column:')
order_column_input = tkinter.OptionMenu(root,order_variable, *excel_column_list,command=order_select)

order_column_text.grid(row = column_setting_rowStart+1,column=column_setting_columnStart)
order_column_input.grid(row = column_setting_rowStart+1,column=column_setting_columnStart+1)


price_variable = tkinter.StringVar()
price_variable.set(excel_column_list[2])
price_column_text  = tkinter.Label(root,text=u'値段column:')
price_column_input = tkinter.OptionMenu(root,price_variable, *excel_column_list,command=price_select)

price_column_text.grid(row = column_setting_rowStart+2,column=column_setting_columnStart)
price_column_input.grid(row = column_setting_rowStart+2,column=column_setting_columnStart+1)

url_variable = tkinter.StringVar()
url_variable.set(excel_column_list[4])
url_column_text  = tkinter.Label(root,text=u'URLcolumn:')
url_column_input = tkinter.OptionMenu(root,url_variable, *excel_column_list,command=url_select)

url_column_text.grid(row = column_setting_rowStart+3,column=column_setting_columnStart)
url_column_input.grid(row = column_setting_rowStart+3,column=column_setting_columnStart+1)

button_rowStart = column_setting_rowStart+5
button_columnStart = column_setting_columnStart

#button
button = tkinter.Button(root, text = "生成",command = button_click,width="30")
button.grid(row=button_rowStart,column=button_columnStart,columnspan=3)

# Listboxの選択肢
days = list()
lists = tkinter.StringVar(value=days)

# 各種ウィジェットの作成
Listbox = tkinter.Listbox(root, listvariable=lists, height=4,width = "40")

# スクロールバーの作成
scrollbar = tkinter.Scrollbar(root, orient=tkinter.VERTICAL, command=Listbox.yview)



# 各種ウィジェットの設置
Listbox.grid(row=button_rowStart+2, column=0,columnspan =3)
scrollbar.grid(row=button_rowStart+2, column=3, sticky=(tkinter.N, tkinter.S))

root.mainloop()



