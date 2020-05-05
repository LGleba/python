# 2020
# Convex Quadrangles
# Powered by LGleba

# There are many points on the plane. Determine the number of convex
# quadrangles that can be built at these points.
# Give a graphical representation of the results.


from datetime import datetime
import random
from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt


def addPointFromEntry(event):
    try:
        x = float(pointXEntry.get())
        y = float(pointYEntry.get())
        addPoint(x, y)
    except:
        try:
            x = float(pointXEntry.get())
        except:
            pointXEntry.delete(0, END)
            pointXEntry.insert(END, "Error")
        try:
            y = float(pointYEntry.get())
        except:
            pointYEntry.delete(0, END)
            pointYEntry.insert(END, "Error")

def addPoint(x, y):
    global countOperations
    global answer
    temp = [x, y]
    if temp not in Points:
        PointsX.append(x)
        PointsY.append(y)
        Points.append(temp)
        countOperations += 1
        countOperationsEntry.delete(0, END)
        countOperationsEntry.insert(END, "{:}".format(countOperations))

        graph = plt.subplot()
        graph.plot(PointsX, PointsY, 'ro', label="graph")
        plt.title("Quadrangle Graph")
        # graph.legend()
        plt.grid()
        plt.xlabel('Value X')
        plt.ylabel('Value Y')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')

        n = len(Points)
        answer = 0
        for i in range(0, n, 1):
            x1 = PointsX[i % n]
            y1 = PointsY[i % n]
            for j in range(0, n, 1):
                x2 = PointsX[j % n]
                y2 = PointsY[j % n]
                for k in range(0, n, 1):
                    x3 = PointsX[k % n]
                    y3 = PointsY[k % n]
                    for l in range(0, n, 1):
                        x4 = PointsX[l % n]
                        y4 = PointsY[l % n]
                        if i != j and i != k and i != l and j != k and j != l and k != l:
                            # D = (x3 - x1) * (y2 - y1) - (y3 - y1) * (x2 - x1)
                            # 4 1 2
                            bottomX = x4
                            bottomY = y4
                            middleX = x1
                            middleY = y1
                            topX = x2
                            topY = y2
                            D1 = (topX - bottomX) * (middleY - bottomY) - (topY - bottomY) * (middleX - bottomX)
                            # 1 2 3
                            bottomX = x1
                            bottomY = y1
                            middleX = x2
                            middleY = y2
                            topX = x3
                            topY = y3
                            D2 = (topX - bottomX) * (middleY - bottomY) - (topY - bottomY) * (middleX - bottomX)
                            # 2 3 4
                            bottomX = x2
                            bottomY = y2
                            middleX = x3
                            middleY = y3
                            topX = x4
                            topY = y4
                            D3 = (topX - bottomX) * (middleY - bottomY) - (topY - bottomY) * (middleX - bottomX)
                            # 3 4 1
                            bottomX = x3
                            bottomY = y3
                            middleX = x4
                            middleY = y4
                            topX = x1
                            topY = y1
                            D4 = (topX - bottomX) * (middleY - bottomY) - (topY - bottomY) * (middleX - bottomX)
                            if (D1 > 0 and D2 > 0 and D3 > 0 and D4 > 0) or (D1 < 0 and D2 < 0 and D3 < 0 and D4 < 0):
                                answer += 1
                                color = random.choice(colors)
                                graph.plot([x1, x2, x3, x4, x1], [y1, y2, y3, y4, y1], label="graph", color='{:}'.format(color))
        countEntry.delete(0, END)
        countEntry.insert(END, "{:}".format(int(answer / 8)))
        plt.show()


def addRandomPoints(event):
    for i in range(5):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        addPoint(x, y)

# Create window
root = Tk()
root.title("@LGleba Convex Quadrangles")

countOperations = 0
Points = []
PointsX = []
PointsY = []
colors = ['black', 'silver', 'firebrick', 'sandybrown', 'gold', 'olivedrab',
          'chartreuse', 'green', 'cyan', 'darkblue', 'coral', 'orange',
          'yellow', 'red', 'greenyellow', 'steelblue']
answer = 0

# Root geometry
LabelForFirstTask = Label(bg='white', fg='black', width=64, text="@LGleba ~~~~~~~~~~~~~~~~~~~~~~~~~1~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", font="Arial 20")
LabelForFirstTask.grid(row=0, column=0, columnspan=2, sticky="s")

pointXLabel = Label(bg='white', fg='black', width=6, text="Write X:", font="Arial 20")
pointXLabel.grid(row=1, column=0, sticky="e")
pointXEntry = Entry(bg='white', fg='black', width=40)
pointXEntry.grid(row=1, column=1, sticky="w")

pointYLabel = Label(bg='white', fg='black', width=6, text="Write Y:", font="Arial 20")
pointYLabel.grid(row=2, column=0, sticky="e")
pointYEntry = Entry(bg='white', fg='black', width=40)
pointYEntry.grid(row=2, column=1, sticky="w")

countOperationsLabel = Label(bg='white', fg='black', width=13, text="Amount of points:", font="Arial 20")
countOperationsLabel.grid(row=3, column=0, sticky="e")
countOperationsEntry = Entry(bg='white', fg='black', width=40)
countOperationsEntry.grid(row=3, column=1, sticky="w")

addPointButton = Button(text="Add point", width=98, height=2, font="Arial")
addPointButton.grid(row=4, column=0, columnspan=2, sticky="w")


countLabel = Label(bg='white', fg='black', width=21, text="The number of quadrangles:", font="Arial 20")
countLabel.grid(row=5, column=0, sticky="e")
countEntry = Entry(bg='white', fg='black', width=40)
countEntry.grid(row=5, column=1, sticky="w")


addRandomPointsButton = Button(text="Add 5 random points", width=98, height=2, font="Arial")
addRandomPointsButton.grid(row=6, column=0, columnspan=2, sticky="w")


addPointButton.bind('<Button-1>', addPointFromEntry)
addRandomPointsButton.bind('<Button-1>', addRandomPoints)


root.mainloop()
