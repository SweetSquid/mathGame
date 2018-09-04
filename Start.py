from tkinter import *
from tkinter import messagebox
class Start:

    def oneclick(self):#функция, которая срабатывает при нажатии на кнопку, обработка данных, закрытие текущего и открытие самой игры
        if self.start_count.get().isdigit()!=True:
            messagebox.showerror("Помилка!", "Перевірте поле 'Кількість гравців'")
        elif int(self.start_count.get())<1:
            messagebox.showerror("Помилка!", "Кількість гравців не повинна бути менша за 1")
        elif int(self.start_count.get())>10:
            messagebox.showerror("Помилка!", "Кількість гравців не повинна перевищувати число 10")
        elif self.start_money.get().isdigit()!=True:
            messagebox.showerror("Помилка!", "Перевірте поле 'Початковий капітал'")
        else:
            self.start_count = self.start_count.get()
            self.start_money = self.start_money.get()
            self.root.destroy()
            self.root.quit()
            del self.root#удаляем переменную из памяти
        #Тут вызвать функцию где 4 кнопки, если это надо

    def blank(self):#окошко и запоминание всех данных
        self.root = Tk()
        wd = self.root.winfo_screenwidth()
        hg =  self.root.winfo_screenheight()
        r1 = int((wd-220)/2)
        r2 = int((hg-100)/2-100)
        self.root.geometry("220x100+%s+%s"%(r1, r2))
        self.root.maxsize(width=220, height=110)
        self.root.minsize(width=220, height=110)
        txt = Label(text="Кількість гравців:")#Текст
        txt.place(width=140, x=10, y=10)

        self.start_count = StringVar()#Переменная принимает значение которое ввели в поле
        ef = Entry(textvariable=self.start_count)
        ef.place(width=50, x=155, y=10)


        txt = Label(text="Початковий капітал:")
        txt.place(width=140, x=10, y=30)

        self.start_money = StringVar()
        ef = Entry(textvariable=self.start_money)
        ef.place(width=50, x=155, y=30)

        btn = Button(text="Почати!", font="Arial 15", command=self.oneclick)#Кнопка, которая вызивает функцию oneclick
        btn.place(x=60, y=55, height=40)

        self.root.mainloop()
#a = Start()#то что надо ввести для вызова этой функции
#a.blank()  #то что надо ввести для вызова этой функции
#
#print(a.start_count)#к-во игроков
#print(a.start_money)#стартовый капитал
