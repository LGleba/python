# 2020
# Calculator
# Powered by LGleba


from tkinter import *
from tkinter import ttk


# Main
fl = 0
tree = 0
kol = 0
numberOp = 1
def main():

    # Create window
    root = Tk()
    root.title("Calculator")

    # geometry
    line = Entry(bg='white', fg='black', width=32)
    line.grid(row=0, column=0, columnspan=3)

    num13 = Button(text="D", width=12, height=3, font="Arial")
    num13.grid(row=1, column=0)

    num14 = Button(text="E", width=12, height=3, font="Arial")
    num14.grid(row=1, column=1)

    num15 = Button(text="F", width=12, height=3, font="Arial")
    num15.grid(row=1, column=2)

    num10 = Button(text="A", width=12, height=3, font="Arial")
    num10.grid(row=2, column=0)

    num11 = Button(text="B", width=12, height=3, font="Arial")
    num11.grid(row=2, column=1)

    num12 = Button(text="C", width=12, height=3, font="Arial")
    num12.grid(row=2, column=2)

    num7 = Button(text="7", width=12, height=3, font="Arial")
    num7.grid(row=3, column=0)

    num8 = Button(text="8", width=12, height=3, font="Arial")
    num8.grid(row=3, column=1)

    num9 = Button(text="9", width=12, height=3, font="Arial")
    num9.grid(row=3, column=2)

    num4 = Button(text="4", width=12, height=3, font="Arial")
    num4.grid(row=4, column=0)

    num5 = Button(text="5", width=12, height=3, font="Arial")
    num5.grid(row=4, column=1)

    num6 = Button(text="6", width=12, height=3, font="Arial")
    num6.grid(row=4, column=2)

    num1 = Button(text="1", width=12, height=3, font="Arial")
    num1.grid(row=5, column=0)

    num2 = Button(text="2", width=12, height=3, font="Arial")
    num2.grid(row=5, column=1)

    num3 = Button(text="3", width=12, height=3, font="Arial")
    num3.grid(row=5, column=2)

    num0 = Button(text="0", width=25, height=3, font="Arial")
    num0.grid(row=6, column=0, columnspan=2)

    numac = Button(text="AC", width=12, height=3, font="Arial")
    numac.grid(row=1, column=3)

    numinfo = Button(text="Info Developer", width=12, height=3, font="Arial")
    numinfo.grid(row=2, column=3)

    num1016 = Button(text="10 --> 16", width=12, height=3, font="Arial")
    num1016.grid(row=3, column=3)

    num1610 = Button(text="16 --> 10", width=12, height=3, font="Arial")
    num1610.grid(row=4, column=3)

    numTochka = Button(text=".", width=12, height=3, font="Arial")
    numTochka.grid(row=6, column=2)

    numDelete = Button(text="<- Delete", width=12, height=3, font="Arial")
    numDelete.grid(row=0, column=3)

    def operatTochka(event):
        line.insert(END, ".")

    def operat0(event):
        line.insert(END, 0)

    def operat1(event):
        line.insert(END, 1)

    def operat2(event):
        line.insert(END, 2)

    def operat3(event):
        line.insert(END, 3)

    def operat4(event):
        line.insert(END, 4)

    def operat5(event):
        line.insert(END, 5)

    def operat6(event):
        line.insert(END, 6)

    def operat7(event):
        line.insert(END, 7)

    def operat8(event):
        line.insert(END, 8)

    def operat9(event):
        line.insert(END, 9)

    def operat10(event):
        line.insert(END, "A")

    def operat11(event):
        line.insert(END, "B")

    def operat12(event):
        line.insert(END, "C")

    def operat13(event):
        line.insert(END, "D")

    def operat14(event):
        line.insert(END, "E")

    def operat15(event):
        line.insert(END, "F")

    def operat1016(event):
        global numberOp
        chislo = line.get()
        line.delete(0, END)
        n = len(chislo)

        kolTochka = 0
        index = n

        for i in range(n):
            if ("0" <= chislo[i] <= "9") or (chislo[i] == "."):
                if chislo[i] == ".":
                    index = i
                    kolTochka += 1

            else:
                line.delete(0, END)
                line.insert(END, "Error!")
                return
        if kolTochka > 1:
            line.delete(0, END)
            line.insert(END, "Error!")
            return

        newChislo = ""

        if chislo[:index]:
            chislo1 = int(chislo[:index])
            while chislo1 > 0:
                temp = chislo1 % 16
                if 10 <= temp <= 15:
                    temp = chr(temp + 55)
                else:
                    temp = str(temp)
                newChislo += temp
                chislo1 = chislo1 // 16
            newChislo = newChislo[::-1]


        if chislo[index:] and kolTochka == 1:
            chislo2 = float("0" + chislo[index:])
            kl = 0
            newChislo += "."
            while kl < 20 and chislo2 != 0:
                chislo2 *= 16
                tmp = chislo2 // 1
                if 10 <= tmp <= 15:
                    newChislo += chr(int(tmp) + 55)
                else:
                    newChislo += str(tmp)[:-2]
                chislo2 -= tmp
                kl += 1

        line.insert(END, newChislo)
        tree.insert('', '0', 'item{:}'.format(numberOp), text="{:}".format(numberOp))
        tree.set('item{:}'.format(numberOp), '1', "{:}".format(chislo))
        tree.set('item{:}'.format(numberOp), '2', "{:}".format("10 --> 16"))
        tree.set('item{:}'.format(numberOp), '3', "{:}".format(newChislo))
        numberOp += 1

    def operat1610(event):
        global numberOp
        chislo = line.get()
        line.delete(0, END)
        n = len(chislo)
        kol = 0
        kolTochka = 0
        for i in range(n):
            if ("0" <= chislo[i] <= "9") or ("A" <= chislo[i] <= "F") or (chislo[i] == "."):
                if chislo[i] == ".":
                    kolTochka += 1
                elif kolTochka == 0:
                    kol += 1
            else:
                line.delete(0, END)
                line.insert(END, "Error!")
                return
        if kolTochka > 1:
            line.delete(0, END)
            line.insert(END, "Error!")
            return

        newChislo = 0
        for i in range(n):
            if "0" <= chislo[i] <= "9":
                newChislo += int(chislo[i]) * 16**(kol - i - 1)
            elif "A" <= chislo[i] <= "F":
                newChislo += (ord(chislo[i]) - 55) * 16**(kol - i - 1)
            else:
                kol += 1
        line.insert(END, newChislo)
        tree.insert('', '0', 'item{:}'.format(numberOp), text="{:}".format(numberOp))
        tree.set('item{:}'.format(numberOp), '1', "{:}".format(chislo))
        tree.set('item{:}'.format(numberOp), '2', "{:}".format("16 --> 10"))
        tree.set('item{:}'.format(numberOp), '3', "{:}".format(newChislo))
        numberOp += 1

    def operatac(event):
        line.delete(0, END)

    def operatdelete(event):
        s = line.get()
        line.delete(0, END)
        line.insert(0, s[:-1])

    def operatinfo(event):
        line.delete(0, END)
        line.insert(0, "Developer @LGleba")

    num0.bind('<Button-1>', operat0)
    num1.bind('<Button-1>', operat1)
    num2.bind('<Button-1>', operat2)
    num3.bind('<Button-1>', operat3)
    num4.bind('<Button-1>', operat4)
    num5.bind('<Button-1>', operat5)
    num6.bind('<Button-1>', operat6)
    num7.bind('<Button-1>', operat7)
    num8.bind('<Button-1>', operat8)
    num9.bind('<Button-1>', operat9)
    num10.bind('<Button-1>', operat10)
    num11.bind('<Button-1>', operat11)
    num12.bind('<Button-1>', operat12)
    num13.bind('<Button-1>', operat13)
    num14.bind('<Button-1>', operat14)
    num15.bind('<Button-1>', operat15)
    num1016.bind('<Button-1>', operat1016)
    num1610.bind('<Button-1>', operat1610)
    numTochka.bind('<Button-1>', operatTochka)
    numac.bind('<Button-1>', operatac)
    numDelete.bind('<Button-1>', operatdelete)
    numinfo.bind('<Button-1>', operatinfo)

    # Table
    tree = ttk.Treeview(root)

    tree.config(columns=('1', '2', '3'))  # Column index
    tree.column('#0', width=40, anchor='center')
    tree.heading('#0', text="№")
    tree.column('1', width=300, anchor='center')
    tree.heading('1', text="Initial number")
    tree.column('2', width=75, anchor='center')
    tree.heading('2', text="Method")
    tree.column('3', width=300, anchor='center')
    tree.heading('3', text="Finite number")

    tree.grid(row=1, column=4, rowspan=6, sticky="n")

    root.mainloop()

# Code
main()