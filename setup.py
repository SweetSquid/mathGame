from Start import *
from Final import *
from Game import *
a = Start()
a.blank()
b = Game()
b.window(int(a.start_count), int(a.start_money))



c = Final()

name = b.zn[0]
money = b.mon_all[4]
x = list(zip(name, money))
x.sort(key=lambda f:f[1])
x.reverse()

name = [i[0] for i in x]#список имен с капиталом по убыванию
money = [i[1] for i in x]#список капиталов по убыванию
c.window(name, money, b.mon_all)
print(c.mnoey)
