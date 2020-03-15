# 2020
# FunctionGUI
# Powered by LGleba
import numpy as np
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt
from math import *
# Main
fl = 0
tree = 0
def main():

    # Создание окна
    root = Tk()
    root.title("Уточнение корней")

    # root.geometry
    fx0l = Label(bg='white', fg='black', width=9, text="Функция y =", font="Arial 20")
    fx0l.grid(row=0, column=0, sticky="e")

    fx0 = Entry(bg='white', fg='black', width=30)
    fx0.grid(row=0, column=1, sticky="w")

    dfdx0l = Label(bg='white', fg='black', width=22, text="Производная от функции y' =", font="Arial 20")
    dfdx0l.grid(row=1, column=0, sticky="e")

    dfdx0 = Entry(bg='white', fg='black', width=30, )
    dfdx0.grid(row=1, column=1, sticky="w")

    start0l = Label(bg='white', fg='black', width=14, text="Начальная точка =", font="Arial 20")
    start0l.grid(row=2, column=0, sticky="e")

    start0 = Entry(bg='white', fg='black', width=30)
    start0.grid(row=2, column=1, sticky="w")
    stop0l = Label(bg='white', fg='black', width=13, text="Конечная точка =", font="Arial 20")
    stop0l.grid(row=3, column=0, sticky="e")
    stop0 = Entry(bg='white', fg='black', width=30)
    stop0.grid(row=3, column=1, sticky="w")
    shag0l = Label(bg='white', fg='black', width=4, text="Шаг =", font="Arial 20")
    shag0l.grid(row=4, column=0, sticky="e")
    shag0 = Entry(bg='white', fg='black', width=30)
    shag0.grid(row=4, column=1, sticky="w")
    eps0l = Label(bg='white', fg='black', width=4, text="EPS =", font="Arial 20")
    eps0l.grid(row=5, column=0, sticky="e")
    eps0 = Entry(bg='white', fg='black', width=30)
    eps0.grid(row=5, column=1, sticky="w")
    err = Label(bg='white', fg='black', width=30, text="", font="Arial 40")
    err.grid(row=6, column=0, columnspan=2)

    b = Button(text="Найти корни", width = 89, height= 2, font="Arial")
    b.grid(row=7, column=0, columnspan=2, sticky="w")

    def operat(event):
        global fl
        global tree
        A2 = []
        A3 = []
        A4 = []
        A5 = []
        A6 = []
        # Проверка на дурака
        try:
            x = 1
            fer = fx0.get()
            ferd = dfdx0.get()
            fun = eval(fer)
            fund = eval(ferd)
            start = float(start0.get())
            stop = float(stop0.get())
            shag = float(shag0.get())
            eps = float(eps0.get())
            err['text'] = "Готово!"
            flag = 1
        except:
            err['text'] = "Ошибка! Данные не верны"
            if fl:
                tree.grid_forget()
                fl = 0
            flag = 0

        # Функция
        def f(x, fer):
            y = eval(fer)
            return y

        # Производная от функции
        def dfdx(x, ferd):
            y = eval(ferd)
            return y

        # Метод Ньютона

        def Newton(x, eps):
            # Значение функции
            f_value = f(x, fer)

            # Количесвто итераций
            iteration_counter = 0

            # Считаем корни
            while abs(f_value) > eps and iteration_counter < 10000:
                try:
                    x = x - f_value / dfdx(x, ferd)
                except:
                    break
                f_value = f(x, fer)
                iteration_counter += 1

            # Проверка на погрешность
            if abs(f_value) > eps:
                iteration_counter = -1

            # Возвращаем корень и количество итераций
            return x, iteration_counter

        if flag:

            # Количество итераций
            if (abs(stop - start) / shag) != (abs(stop - start) // shag):
                r = abs(stop - start) // shag + 1
            else:
                r = abs(stop - start) // shag
            # Нахождение корней
            r = r + 1
            for k in range(int(r)):
                x, iters = Newton(start + shag * k, eps)
                x = round(x, 3)
                if x not in A4 and start <= x <= stop and iters != -1:
                    for i in np.arange(start, stop, shag):
                        if i <= x < i + shag:
                            A2.append(i)
                            if i + shag > stop:
                                A3.append(stop)
                            else:
                                A3.append(i + shag)
                            A4.append(x)
                            A5.append(f(x, fer))
                            A6.append(iters)

            # Таблица
            n = len(A4)
            for i in range(n - 1):
                if flag:
                    flag = 0
                    for j in range(n - i - 1):
                        if A4[j] > A4[j + 1]:
                            A4[j], A4[j + 1] = A4[j + 1], A4[j]
                            A2[j], A2[j + 1] = A2[j + 1], A2[j]
                            A3[j], A3[j + 1] = A3[j + 1], A3[j]
                            flag = 1
            if n:
                if fl:
                    tree.pack_forget()
                tree = ttk.Treeview(root)

                tree.config(columns=('1', '2', '3', '4', '5'))  # Колонка индекс
                tree.column('#0', width=40, anchor='center')
                tree.heading('#0', text="№")
                tree.column('1', width=200, anchor='center')
                tree.heading('1', text="Интервал")
                tree.column('2', width=200, anchor='center')
                tree.heading('2', text="Знач. корня")
                tree.column('3', width=100, anchor='center')
                tree.heading('3', text="Знач. функции")
                tree.column('4', width=100, anchor='center')
                tree.heading('4', text="Кол-во итерац.")
                tree.column('5', width=70, anchor='center')
                tree.heading('5', text="Код ошибки")

                for i in range(n):
                    tree.insert('', 'end', 'item{:}'.format(i + 1), text="{:}".format(i+1))
                for i in range(n):
                    tree.set('item{:}'.format(i + 1), '1', "{:<15.4} - {:>15.4}".format(A2[i], A3[i]))
                for i in range(n):
                    tree.set('item{:}'.format(i + 1), '2', "{:}".format(A4[i]))
                for i in range(n):
                    tree.set('item{:}'.format(i + 1), '3', "{:12.4}".format(A5[i]))
                for i in range(n):
                    tree.set('item{:}'.format(i + 1), '4', "{:}".format(A6[i]))
                for i in range(n):
                    tree.set('item{:}'.format(i + 1), '5', "NO")

                tree.grid(row=8, column=0, columnspan=2, sticky="w")
                fl = 1

                # Функция
                xlist = [i for i in np.arange(start, stop, 0.1)]
                ylist = []

                # Экстремумы
                ex = []
                ey = []

                for i in xlist:
                    if (dfdx(i, ferd) < 0 and dfdx(i + 0.1, ferd) > 0) or (dfdx(i, ferd) > 0 and dfdx(i + 0.1, ferd) < 0):
                        ex.append(i + 0.05)
                        ey.append(f(i + 0.05, fer))

                for i in xlist:
                    ylist.append(f(i, fer))

                ax = plt.subplot()
                ax.plot(xlist, ylist, label="y = {:}".format(fer))
                plt.title("График")
                ax.legend()

                plt.grid()
                plt.xlabel('Значение аргумента')
                plt.ylabel('Значение функции')
                plt.axhline(y=0, color='k')
                plt.axvline(x=0, color='k')


                for i in range(len(ex)):
                    plt.plot(ex[i], ey[i], marker='o', color="r")

                for i in range(len(A4)):
                    plt.plot(A4[i], f(A4[i], fer), marker='o', color="b")

                plt.show()
            else:
                err['text'] = "Корней нет!"
                if fl:
                    tree.grid_forget()
                    fl = 0

    b.bind('<Button-1>', operat)

    root.mainloop()

# Code
main()