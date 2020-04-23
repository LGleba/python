# 2020
# Research on sorting methods
# Powered by LGleba


from datetime import datetime
import random
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt


def insertionSort(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
    return arr


def firstOperation(event):
    try:
        arr = list(map(int, sizeArrayEntry.get().split()))

        arr = insertionSort(arr)

        SortArrayEntry.delete(0, END)
        for i in arr:
            SortArrayEntry.insert(END, str(i) + " ")
    except:
        SortArrayEntry.delete(0, END)
        SortArrayEntry.insert(END, "Error!")


def secondOperation(event):
    try:
        n1 = int(SizeFirstArrayEntry.get())
        n2 = int(SizeSecondArrayEntry.get())
        n3 = int(SizeThirdArrayEntry.get())

        if n1 < 0:
            n1 = abs(n1)
            SizeFirstArrayEntry.delete(0)
        if n2 < 0:
            n2 = abs(n2)
            SizeSecondArrayEntry.delete(0)
        if n3 < 0:
            n3 = abs(n3)
            SizeThirdArrayEntry.delete(0)

        listN = [n1, n2, n3]

        A = [0] * 3
        for i in range(3):
            A[i] = [0] * 3

        index = 0
        for n in listN:
            firstArray = [i for i in range(n)]
            start_time = datetime.now()
            firstArray = insertionSort(firstArray)
            A[0][index] = datetime.now() - start_time

            secondArray = [random.randint(0, 10) for i in range(n)]
            start_time = datetime.now()
            secondArray = insertionSort(secondArray)
            A[1][index] = datetime.now() - start_time

            thirdArray = [i for i in range(n - 1, -1, -1)]
            start_time = datetime.now()
            thirdArray = insertionSort(thirdArray)
            A[2][index] = datetime.now() - start_time

            index += 1

        tree = ttk.Treeview(root)

        tree.config(columns=('1', '2', '3'))  # Column index
        tree.column('#0', width=183, anchor='center')
        tree.heading('#0', text="Type / Size array")
        tree.column('1', width=200, anchor='center')
        tree.heading('1', text="N1 = {:} elements".format(n1))
        tree.column('2', width=200, anchor='center')
        tree.heading('2', text="N2 = {:} elements".format(n2))
        tree.column('3', width=200, anchor='center')
        tree.heading('3', text="N3 = {:} elements".format(n3))

        tree.insert("", 'end', 'item1', text="Ordered array")
        tree.insert("", 'end', 'item2', text="Random array")
        tree.insert("", 'end', 'item3', text="Back ordered array")

        for i in range(3):
            for j in range(3):
                temp = A[i][j]
                tree.set('item{:}'.format(i + 1), "{:}".format(j + 1), str(temp.microseconds) + " ms")

        tree.grid(row=10, column=0, columnspan=2, sticky="w")

    except:
        try:
            n1 = int(SizeFirstArrayEntry.get())
        except:
            n1 = SizeFirstArrayEntry.get()
            if n1[-10:] != "<- Error!":
                SizeFirstArrayEntry.insert(END, " <- Error!")

        try:
            n2 = int(SizeSecondArrayEntry.get())
        except:
            n2 = SizeSecondArrayEntry.get()
            if n2[-10:] != "<- Error!":
                SizeSecondArrayEntry.insert(END, " <- Error!")

        try:
            n3 = int(SizeThirdArrayEntry.get())
        except:
            n3 = SizeThirdArrayEntry.get()
            if n3[-10:] != "<- Error!":
                SizeThirdArrayEntry.insert(END, " <- Error!")


def thirdOperation(event):
    try:
        start = int(primarySizeArrayEntry.get())
        interval = int(intervalArrayEntry.get())

        if start < 0:
            start = abs(start)
            primarySizeArrayEntry.delete(0)
        if interval < 0:
            interval = abs(interval)
            intervalArrayEntry.delete(0)

        xList = [start + i * interval for i in range(10)]
        yList = []
        for n in xList:
            array = [random.randint(0, 10) for i in range(n)]
            start_time = datetime.now()
            array = insertionSort(array)
            temp = datetime.now() - start_time
            yList.append(temp.microseconds)

        xList.insert(0, 0)
        yList.insert(0, 0)
        graph = plt.subplot()
        graph.plot(xList, yList, label="graph")
        plt.title("Graph of sorting time versus array size")
        # graph.legend()
        plt.grid()
        plt.xlabel('The number of elements in the array')
        plt.ylabel('Time in "ms"')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()

    except:
        try:
            start = int(primarySizeArrayEntry.get())
        except:
            temp = primarySizeArrayEntry.get()
            if temp[-10:] != "<- Error!":
                primarySizeArrayEntry.insert(END, " <- Error!")

        try:
            interval = int(intervalArrayEntry.get())
        except:
            temp = intervalArrayEntry.get()
            if temp[-10:] != "<- Error!":
                intervalArrayEntry.insert(END, " <- Error!")


# Create window
root = Tk()
root.title("@LGleba Research on sorting methods")

# Root geometry
LabelForFirstTask = Label(bg='white', fg='black', width=64, text="@LGleba ~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font="Arial 20")
LabelForFirstTask.grid(row=0, column=0, columnspan=2, sticky="s")

sizeArrayLabel = Label(bg='white', fg='black', width=25, text="Enter array elements with a space", font="Arial 20")
sizeArrayLabel.grid(row=1, column=0, sticky="e")
sizeArrayEntry = Entry(bg='white', fg='black', width=40)
sizeArrayEntry.grid(row=1, column=1, sticky="w")

SortArrayLabel = Label(bg='white', fg='black', width=13, text="Your sorted array", font="Arial 20")
SortArrayLabel.grid(row=2, column=0, sticky="e")
SortArrayEntry = Entry(bg='white', fg='black', width=40)
SortArrayEntry.grid(row=2, column=1, sticky="w")

SortArrayButton = Button(text="Sort array", width=98, height=2, font="Arial")
SortArrayButton.grid(row=3, column=0, columnspan=2, sticky="w")


freeLabel = Label(bg='white', fg='black', width=24, text="", font="Arial 20")
freeLabel.grid(row=4, column=0, sticky="e")


LabelForSecondTask = Label(bg='white', fg='black', width=64, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~2~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font="Arial 20")
LabelForSecondTask.grid(row=5, column=0, columnspan=2, sticky="s")

SizeFirstArrayLabel = Label(bg='white', fg='black', width=10, text="Size N1 array", font="Arial 20")
SizeFirstArrayLabel.grid(row=6, column=0, sticky="e")
SizeFirstArrayEntry = Entry(bg='white', fg='black', width=40)
SizeFirstArrayEntry.grid(row=6, column=1, sticky="w")

SizeSecondArrayLabel = Label(bg='white', fg='black', width=10, text="Size N2 array", font="Arial 20")
SizeSecondArrayLabel.grid(row=7, column=0, sticky="e")
SizeSecondArrayEntry = Entry(bg='white', fg='black', width=40)
SizeSecondArrayEntry.grid(row=7, column=1, sticky="w")

SizeThirdArrayLabel = Label(bg='white', fg='black', width=10, text="Size N3 array", font="Arial 20")
SizeThirdArrayLabel.grid(row=8, column=0, sticky="e")
SizeThirdArrayEntry = Entry(bg='white', fg='black', width=40)
SizeThirdArrayEntry.grid(row=8, column=1, sticky="w")

MakeTableButton = Button(text="Create a time table", width=98, height=2, font="Arial")
MakeTableButton.grid(row=9, column=0, columnspan=2, sticky="w")


freeLabel = Label(bg='white', fg='black', width=24, text="", font="Arial 20")
freeLabel.grid(row=11, column=0, sticky="e")


LabelForThirdTask = Label(bg='white', fg='black', width=64, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~3~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font="Arial 20")
LabelForThirdTask.grid(row=12, column=0, columnspan=2, sticky="s")

primarySizeArrayLabel = Label(bg='white', fg='black', width=12, text="Initial Array Size", font="Arial 20")
primarySizeArrayLabel.grid(row=13, column=0, sticky="e")
primarySizeArrayEntry = Entry(bg='white', fg='black', width=40)
primarySizeArrayEntry.grid(row=13, column=1, sticky="w")

intervalArrayLabel = Label(bg='white', fg='black', width=6, text="Interval", font="Arial 20")
intervalArrayLabel.grid(row=14, column=0, sticky="e")
intervalArrayEntry = Entry(bg='white', fg='black', width=40)
intervalArrayEntry.grid(row=14, column=1, sticky="w")

MakeGraphButton = Button(text="Create a plot of sorting time versus array size", width=98, height=2, font="Arial")
MakeGraphButton.grid(row=15, column=0, columnspan=2, sticky="w")


SortArrayButton.bind('<Button-1>', firstOperation)
MakeTableButton.bind('<Button-1>', secondOperation)
MakeGraphButton.bind('<Button-1>', thirdOperation)


root.mainloop()
