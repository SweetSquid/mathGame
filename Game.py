from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from random import randint
from tkinter import messagebox

class Game:


    def money_cl(self, choise, mon):
        print("Я сработал(money_cl)")
        print("choise:",choise)
        print("self.mon_all:",self.mon_all)
        for i in range(len(self.mon_all)):
            if self.mon_all[i]==[]:
                self.mon_all[i] = [None for i in range(self.count)]
                x = self.mon_all[i-1]
                gaz_count = choise.count("Газпром")
                nano_count = choise.count("НАНО")
                print("gaz", gaz_count)
                print("nano", nano_count)
                cryz = randint(1, 6)
                cryz = True if cryz in (3, 6) else False
                print("Кризис: ", cryz)
                print("OK",i)
                for j in range(self.count):
                    if choise[j]=="Банк":
                        self.mon_all[i][j]=self.mon_all[i-1][j]*1.1 if cryz==False else self.mon_all[i-1][j]*0.7
                    elif choise[j]=="Газпром":
                        self.mon_all[i][j]=self.mon_all[i-1][j]*4*gaz_count/self.count
                    elif choise[j]=="НАНО":
                        self.mon_all[i][j]=self.mon_all[i-1][j]*3/nano_count
                    elif choise[j]=="StartUP":
                        self.mon_all[i][j]=self.mon_all[i-1][j]*3 if cryz==False else self.mon_all[i-1][j]*0.8
                    onl = i
                break
        print("Ход:",self.mon_all,"\n\n\n")
        print(self.zn)
        for i in range(1, self.count+1):
            print(self.mon_all[onl][i-1])
            self.table[2][i] = Label(text=int(self.mon_all[onl][i-1]))
            self.table[2][i].place(width=100, height=30, x=110 * 2 + (self.wd - 760) / 2, y=40 * i + 120)



    schelk = 3
    def toexit(self):
        self.root.destroy()
        self.root.quit()
    def start_click(self):
        wd = self.root.winfo_screenwidth()
        hg = self.root.winfo_screenheight()
        self.wd = wd
        self.hg = hg
        self.hod.place(width=70, height=30, x=0.6 * wd, y=(self.count + 1) * 40 + 150)
        for j in range(self.count + 1):
            if j != 0:
                self.table[self.schelk][j] = ttk.Combobox(self.root, values=[u"Газпром", u"Банк", u"StartUP", u"НАНО"], height=4, state='readonly')
                self.table[self.schelk][j].current(1)
            self.table[self.schelk][j].place(width=100, height=30, x=110 * self.schelk + (wd - 760) / 2, y=40 * j + 120)
        self.schelk += 1
        for i in range(len(self.zn)):
            for j in range(len(self.zn[i])):
                self.zn[i][j] = self.zn[i][j].get()
        for i in range(self.count + 1):
            if i != 0:
                self.table[1][i].destroy()
                self.table[1][i] = Label(text=self.zn[0][i - 1])
                self.table[1][i].place(width=100, height=30, x=110 * 1 + (wd - 760) / 2, y=40 * i + 120)
        self.st.destroy()
    def stop(self):
        pass

    def run_click(self):
        wd = self.root.winfo_screenwidth()
        hg = self.root.winfo_screenheight()
        if self.schelk != 7:
            for i in range(self.count + 1):
                self.table[self.schelk][i].place(width=100, height=30, x=110 * self.schelk + (wd - 760) / 2,
                                                 y=40 * i + 120)
                #print(self.zn)
                if i != 0:
                    self.zn[self.schelk - 3][i - 1] = self.table[self.schelk - 1][i].get()
                    self.table[self.schelk][i] = ttk.Combobox(self.root, values=[u"Газпром", u"Банк", u"StartUP", u"НАНО"], height=4, state='readonly')
                    self.table[self.schelk][i].current(1)
                    self.table[self.schelk - 1][i] = Label(text=self.zn[self.schelk - 3][i - 1])#вывод выбора и капитала
                    self.table[self.schelk - 1][i].place(width=100, height=30,
                                                         x=110 * (self.schelk - 1) + (wd - 760) / 2, y=40 * i + 120)
                    self.table[self.schelk][i].place(width=100, height=30, x=110 * (self.schelk) + (wd - 760) / 2,
                                                     y=40 * i + 120)
            #print(self.zn)чч
            self.money_cl(self.zn[self.schelk - 3], 333)
            self.schelk += 1
        else:

            for i in range(self.count + 1):
                if i != 0:
                    self.zn[self.schelk - 3][i - 1] = self.table[self.schelk - 1][i].get()
                    self.table[self.schelk - 1][i] = Label(text=self.zn[self.schelk - 3][i - 1])
                    self.table[self.schelk - 1][i].place(width=100, height=30,
                                                         x=110 * (self.schelk - 1) + (wd - 760) / 2, y=40 * i + 120)
            self.money_cl(self.zn[self.schelk - 3], 333)
            self.hod.destroy()
            self.root.destroy()#где-то тут вызывать след окно


    def window(self, start_count, start_money):
        def send_mes_b():
            root_bank = Toplevel()
            root_bank.title("Банк")
            root_bank.resizable(width=False, height=False)
            root_bank.geometry("650x540")
            def bank_show_message():
                root_bank.destroy()
            mi = PhotoImage(file='img/bank.gif')
            b1 = ttk.Button(root_bank, command=bank_show_message, image=mi)
            b1.grid()
            b2 =ttk.Label(root_bank,text="При вкладі грошей до банку ви можете збільшити свій капітал(на 10%), або навпаки, втратити частину(30%) якщо криза(шанс кризи 18%).")
            b2.place(heigh='20', width='150', x=250, y=520)
            root_bank.mainloop()
        def send_mes_n():
            root_nano = Toplevel()
            root_nano.title("Нанотехнології")
            root_nano.resizable(width=False, height=False)
            root_nano.geometry("778x500")
            def nano_show_message():
                root_nano.destroy()
            mi = PhotoImage(file='img/nano.gif')
            b1 = ttk.Button(root_nano, command=nano_show_message, image=mi)
            b1.grid()
            b2 = ttk.Label(root_nano, text="Бюджет розраховується за формулою x*3/n. Де x - бюджет гравця до вкладу, n - кількість гравців, що вклалися в нанотехнології")
            b2.place(x=50, y=453)
            root_nano.mainloop()

        def send_mes_g():
           root_gaz = Toplevel()
           root_gaz.title('Газпром')
           root_gaz.resizable(width=False, height=False)
           root_gaz.geometry("810x603")
           def gaz_show_message():
                root_gaz.destroy()
           mi = PhotoImage(file='img/gaz.gif')
           b1 = ttk.Button(root_gaz, command=gaz_show_message, image=mi)
           b1.grid()
           b2 = ttk.Label(root_gaz, text="Бюджет разраховується за формулою: (0.4 * к-сть гравців, що вклалися в газпром)/загальну кількість гравців")
           b2.place(x=80, y=583)
           root_gaz.mainloop()

        def send_mes_s():
            root_startup = Toplevel()
            root_startup.title("Start up")
            root_startup.resizable(width=False, height=False)
            root_startup.geometry("884x620+300+70")
            def startup_show_message():
                root_startup.destroy()
            mi = PhotoImage(file='img/startup.gif')
            b1 = ttk.Button(root_startup, command=startup_show_message, image=mi)
            b1.grid()
            b2 = ttk.Label(root_startup,text="(1) При вкладі грошей ви можете збільшити свій капітал в три рази, або навпаки, втратити частину(20%), якщо криза (шанс кризи 40%).")
            b2.place(x=80, y=600)
            root_startup.mainloop()


        self.count = start_count
        self.root = Tk()
        self.root.overrideredirect(1)
        wd = self.root.winfo_screenwidth()
        hg = self.root.winfo_screenheight()
        self.root.geometry("%sx%s" % (wd, hg))  # окно
        #self.root.geometry("%sx%s" % (500, 500))  # окно
        self.mon_all = [[] for i in range(5)]
        self.mon_all[0] = [start_money for i in range(start_count)]



        img = PhotoImage(file='img/bg.gif')
        bg = Label(self.root, image=img)
        bg.place(x=0, y=0, width=wd, height=hg)  # фон

        self.table = []
        self.zn = []
        for i in range(7):
            self.table.append([])
            for j in range(start_count + 1):
                self.table[i].append(None)
        zni, znj = -1, 0
        klap = ""
        for i in range(7):
            for j in range(start_count + 1):
                if i == 2:
                    self.table[i][j] = Label(text=start_money)
                elif (i != 0) & (j != 0) & (i != 2):
                    if klap != i:
                        self.zn.append([])
                        zni += 1
                        znj = 0
                        klap = i
                    self.zn[zni].append(StringVar())
                    self.table[i][j] = Entry(textvariable=self.zn[zni][znj])
                    znj += 1
                elif i == 0:
                    self.table[i][j] = Label(text=j)
                elif j == 0:
                    self.table[0][0] = Label(text="№")
                    self.table[1][0] = Label(text="Ім'я")
                    self.table[2][0] = Label(text="Капітал")
                    self.table[3][0] = Label(text="1")
                    self.table[4][0] = Label(text="2")
                    self.table[5][0] = Label(text="3")
                    self.table[6][0] = Label(text="4")

        for i in range(3):
            for j in range(start_count + 1):
                self.table[i][j].place(width=100, height=30, x=110 * i + (wd - 760) / 2, y=40 * j + 120)
        btn = [Button(text="Газпром", font="Arial 15", command=send_mes_g),
               Button(text="Банк", font="Arial 15", command=send_mes_b),
               Button(text="КПІ", font="Arial 15", command=send_mes_s),
               Button(text="НАНО", font="Arial 15", command=send_mes_n)]
        btn[0].place(width=0.15 * wd, height=100, x=0.35 * wd, y=0.7 * hg)
        btn[1].place(width=0.15 * wd, height=100, x=0.5 * wd, y=0.7 * hg)
        btn[2].place(width=0.15 * wd, height=100, x=0.35 * wd, y=0.7 * hg + 100)
        btn[3].place(width=0.15 * wd, height=100, x=0.5 * wd, y=0.7 * hg + 100)


        exxit = Button(text="X", font="Arial 15", command=self.toexit)
        exxit.place(x=wd-40, y=10, width=30, height=30)

        self.st = Button(text="Почати", font="Arial 13", command=self.start_click)
        self.st.place(width=70, height=30, x=0.3 * wd + 70, y=(start_count + 1) * 40 + 150)
        self.hod = Button(text="Хід", font="Arial 13", command=self.run_click)
        self.end = Button(text="Хід", font="Arial 13", command=lambda x: self.root.destroy())

        self.root.mainloop()
#a = Game()
#a.window(4, 10000)
#print(a.zn)
#print(a.mon_all)
#
