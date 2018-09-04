from tkinter import *
import matplotlib.pyplot as mpl
import tkinter as Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
class Final:
    def for_money(self, all, num):
        p = []
        for i in range(len(all)):
            p.append(int(all[i][num]))
        print("\n\n\n\n\n\n\n",num)
        return p
    def show_graph(self, num):  # Вывод графика для отдельного игрока, используя его историю
        mpl.ylabel("Гроші")
        mpl.xlabel("Ходи")
        mpl.plot(['0', '1', '2', '3', '4'], self.for_money(self.mnoey, num), "r")
        mpl.title("Бюджет гравця")
        mpl.grid()
        mpl.show()
    def window(self, names, moneyAll, mnoey):
        self.mnoey = mnoey
        root = Tk.Tk()
        table = []
        root.overrideredirect(1)
        wd = root.winfo_screenwidth()
        hg =  root.winfo_screenheight()
        root.geometry("%sx%s"%(wd, hg))#окно

        img = PhotoImage(file='img/bg.gif')
        bg = Label(root, image=img)
        bg.place(x=0, y=0, width=wd, height=hg)

        f = Figure(dpi = 80, figsize = (512 / 80, 384 /80))
        a = f.add_subplot(10, 10, (21, 80))

        x = moneyAll
        a.pie(x, autopct='%.1f%%', radius = 1.1,
        explode = [0.1] + [0 for _ in range(len(x) - 1)], shadow=True)

        a.legend(bbox_to_anchor=(-0.16, 0.45, 0.25, 0.25), loc='lower left', labels=names, shadow=True)

        canvas = FigureCanvasTkAgg(f, master=root)
        canvas.get_tk_widget().place(width=500, height=500, y=140, x=0.5*wd)
        #canvas.print_figure('bg.png')#создает png копию диаграммы

        def _quit():
            root.quit()     # stops mainloop
            root.destroy()  # this is necessary on Windows to prevent
                            # Fatal Python Error: PyEval_RestoreThread: NULL tstate

        button = Tk.Button(master=root, text='Quit', command=_quit)
        button.pack(side=Tk.BOTTOM)


        def but(i):#эта функция создает кнопки для графиков
            table[i].append(Button(text="Графік гравця \n%s"%names[i], bg="aqua", relief=RAISED, font="Arial 10", command=lambda:self.show_graph(i)))
            table[i][2].place(width=100, height=45, x=0.2*wd+197, y=142+i*50)



        for i in range(len(names)):
            table.append([])
            table[i].append(Label(text=(i+1), bg="white", bd=4, relief=GROOVE, font="Arial, 15"))
            table[i][0].place(width=50, height=50, x=100, y=140+i*50)

            table[i].append(Label(text=names[i]+"("+str(int(moneyAll[i]))+")", bg="white", bd=4, relief=GROOVE, font="Arial, 15"))
            table[i][1].place(width=0.2*wd, height=50, x=147, y=140+i*50)

            but(i)

        pob = Label(text="Переможець: %s"%names[0], font="Arial 50", fg="blue", bg="yellow", bd=8, relief=RIDGE)
        pob.place(width=0.5*wd, height=100, x=0.25*wd, y=hg-200)
        root.mainloop()


#a = Final()
#name = ["Вася", "Петя", "Макар"]
#x = (1000, 500, 700)
#a.window(name, x)
