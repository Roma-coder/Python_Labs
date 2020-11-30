from tkinter import *
import math


class Block:
    def __init__(self, master):

        self.radioValue = IntVar() 
        self.radioValue.set(0)

        self.lab1 = Label(master, width=20, text=' Перше число:', pady=10)
        self.ent1 = Entry(master, width=20)

        self.lab2 = Label(master, width=20, text='Друге число:', pady=10)
        self.ent2 = Entry(master, width=20)

        self.lab3 = Label(master, width=20, text='Третэ число:', pady=10)
        self.ent3 = Entry(master, width=20)

        self.r1but = Radiobutton(master, width=20, text='Периметр:', pady=10, variable=self.radioValue, value=0)

        self.r2but = Radiobutton(master, width=20, text='Площа:', pady=10, variable=self.radioValue, value=1)

        self.but = Button(master, text="Порахувати", pady=10)

        self.num = Label(master, width=40, pady=20, text='Відповідь:')

        self.but['command'] = self.count
        self.lab1.pack()
        self.ent1.pack()
        self.lab2.pack()
        self.ent2.pack()
        self.lab3.pack()
        self.ent3.pack()
        self.r1but.pack()
        self.r2but.pack()
        self.but.pack()
        self.num.pack()

    def count(self):
        val1 = self.ent1.get()
        val2 = self.ent2.get()
        val3 = self.ent3.get()


        if val1 == '' or val2 == '' or val3 == '':
            self.num['text'] = 'Будь ласка, введіть всі числа'
            return

        if val1 == 0 or val2 == 0 or val3 == 0:
            self.num['text'] = 'Сторона не може бути відємною або 0'
            return

        if not val1.isnumeric() or not val2.isnumeric() or not val3.isnumeric():
            self.num['text'] = 'Будь ласка, введіть числові значення'
            return

        num1 = int(val1)
        num2 = int(val2)
        num3 = int(val3)

        perimeter = num1 + num2 + num3

        half_perimeter = perimeter / 2

        square = math.sqrt((half_perimeter - num1)*(half_perimeter - num2)*(half_perimeter - num3))

        if self.radioValue.get() == 0:
            self.num['text'] = 'Результат: ' + str(perimeter)
        elif self.radioValue.get() == 1:
            self.num['text'] = 'Результат: ' + str(square)    


root = Tk()
root.title('Варіант 11')

main = Block(root)

root.mainloop()