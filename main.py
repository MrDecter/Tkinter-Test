#Привязать рецепты к Tkiner
from tkinter import *


window = Tk()
window.title("LiteFood - Простые рецепты")
window.geometry('500x700')
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Новый')
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
window.config(menu=menu)
window.mainloop()