#!/usr/bin/env python
# --coding:utf-8--

from tkinter import *
from math import sin, cos, sqrt, exp, pi
 
root = Tk() # главное окно
root.title("Груз на пружине")

labelCanvas = Label(text="График", font=("Helvetica", 12))
labelCanvas.grid(row = 0, column = 1, columnspan = 1, sticky = W)

labelTool = Label(text="Настройки", font=("Helvetica", 12))
labelTool.grid(row = 0, column = 0, columnspan = 1, sticky = W)

c = Canvas(root, width=1000, height=400, bg="#7B68EE")
c.grid(row = 1, column = 1, rowspan = 7, sticky = W)

def  phasePortrait():
	c.delete("all") # очищаем холст канваса 

	# отрисовка осей абцисс и ординат
	c.create_line(0, 165, 1000, 165, fill="#AFEEEE")
	c.create_line(503, 0, 503, 400, fill="#AFEEEE")
	
	dt=0.001 # значение изменения времени

	# инициализация переменных  
	t=0
	v=0
	x=0

	g=9.8 # ускорение свободного падения
	while t<10: # пока время не достигнет 10 секунд 
		t=t+dt # счетчик времени
		# скорость
		v=v-x0.get()*sqrt(k.get()/m.get())*exp(-(u.get()*9.8*cos(alpha.get())*t)/(2*m.get()))*sin(sqrt(k.get()/m.get())*t)
		# координата
		x=x+x0.get()*exp(-(u.get()*g*cos(alpha.get())*t)/(2*m.get()))*cos(sqrt(k.get()/m.get())*t)
		# отрисовка спирали на канвасе
		c.create_line(489 + 5 * x, 69 - 1 * v, 490 + 5 * x, 70 - 1 * v, fill="#F08080")
	# вывод полученных значений скорости и координаты 
	c.create_text(953, 183, text="v="+str(v)+" м/c", anchor=SE)
	c.create_text(683, 20, text="x="+str(x)+" м", anchor=SE)

''' отрисовка интерфейса с использованием библиотеки tkintet (GUI - библиотека):
	графические элементы интерфейса на экране расположены по табличному методу,
	где row-строка, column-столбец, columnspan-количество ячеек занятых в строке,
	sticky-выравнивание элемента в ячейке'''

k = Scale(root, from_=1, to=20, label="коэф. упругости(k), H/м:", orient=HORIZONTAL, length=180)
k.grid(row = 1, column = 0, sticky = W+N+S+E)

m = Scale(root, from_=0.1, to=2.0, resolution=0.1, label="масса(m), кг:", orient=HORIZONTAL)
m.grid(row = 2, column = 0, sticky = W+N+S+E)

x0 = Scale(root, from_=0.1, to=2.0, resolution=0.1, label="нач. деформ(x0), м:", orient=HORIZONTAL)
x0.grid(row = 3, column = 0, sticky = W+N+S+E)

u = Scale(root, from_=0.001, to=0.005, resolution=0.0002, label="коэф. трения(μ), б/р:", orient=HORIZONTAL)
u.grid(row = 4, column = 0, sticky = W+N+S+E)

alpha = Scale(root, from_=pi/120, to=pi/4, resolution=0.03, label="угол плоскости(α), рад:", orient=HORIZONTAL)
alpha.grid(row = 5, column = 0, sticky = W+N+S+E)

btn = Button(root, text ="Построить фазовый портрет", command = phasePortrait)
btn.grid(row = 6, column = 0, sticky = W+N+S+E)
 
root.mainloop()