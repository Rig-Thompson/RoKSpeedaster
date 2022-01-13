from tkinter import *
#totalhours1 = 0
#main settings of window
root = Tk()

#peremen
totalhours = 0
totaldays = 0

def totaldef():
    totalhours = int(all1mint.get()) + int(all5mint.get())
    totaldays = totalhours // 24
    print(totalhours)
    totalhourstext.config(text=f'ЧАСЫ: {totalhours}')
    totaldaystext.config(text=f'ДНИ: {totaldays}')

    #totalhourstext = Label(canvas, text=f'ЧАСЫ: {totalhours}', font=('Comic Sans MS', 25), justify=LEFT)
    #totalhourstext.config(bg='#ff0000')
    #  totalhourstext.place(x=36, y=637, width=200, height=70)
    #   totaldaystext = Label(canvas, text=f'ДНЕЙ: {totaldays}', font=('Comic Sans MS', 25), justify=LEFT)
    #  totaldaystext.config(bg='#ff0000')
    #  totaldaystext.place(x=540, y=637, width=200, height=70)
    #totalhours = totalhours1

root['bg'] = '#ff9966'
root.title('Rise of Kingdoms: Speedaster')
root.geometry('1280x720')
root.resizable(width=False, height=False)

#root.wm_attributes('-alpha', 0.65)

#canvas block
canvas = Canvas(root, height=720, width=1280, bg='#ff9966')
canvas.pack()

#frame
frame = Frame(root, bg='#b22222')
frame.place(x=36, y=700, width=657, height=10)

#ALL TEXT PLACE
alltext = Label(canvas, text='Общие ускорения', font=('Comic Sans MS', 17, 'bold')) #allest
alltext.config(bg='#ff9966')# speedast
alltext.place(x=10, y=8)
context = Label(canvas, text='Специальные ускорения', font=('Comic Sans MS', 17, 'bold')) #specia
context.config(bg='#ff9966')# l speedast
context.place(x=10, y=317)
    #speddast name's 1st line
text1 = Label(canvas, text='1-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text1.config(bg='#ff9966')
text1.place(x=36, y=44, width=150, height=65)
text2 = Label(canvas, text='5-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text2.config(bg='#ff9966')
text2.place(x=290, y=44, width=150, height=65)
text3 = Label(canvas, text='10-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text3.config(bg='#ff9966')
text3.place(x=544, y=44, width=150, height=65)
text4 = Label(canvas, text='15-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text4.config(bg='#ff9966')
text4.place(x=797, y=44, width=150, height=65)
text5 = Label(canvas, text='30-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text5.config(bg='#ff9966')
text5.place(x=1049, y=44, width=150, height=65)
    #speddast name's 2st line
text6 = Label(canvas, text='60-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text6.config(bg='#ff9966')
text6.place(x=36, y=186, width=150, height=65)
text7 = Label(canvas, text='3-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text7.config(bg='#ff9966')
text7.place(x=290, y=186, width=150, height=65)
text8 = Label(canvas, text='8-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text8.config(bg='#ff9966')
text8.place(x=544, y=186, width=150, height=65)
text9 = Label(canvas, text='15-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text9.config(bg='#ff9966')
text9.place(x=797, y=186, width=150, height=65)
text10 = Label(canvas, text='7-дневное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text10.config(bg='#ff9966')
text10.place(x=1049, y=186, width=150, height=65)
    #speddast name's 3st line
text11 = Label(canvas, text='1-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text11.config(bg='#ff9966')
text11.place(x=36, y=361, width=150, height=65)
text12 = Label(canvas, text='5-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text12.config(bg='#ff9966')
text12.place(x=290, y=361, width=150, height=65)
text13 = Label(canvas, text='10-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text13.config(bg='#ff9966')
text13.place(x=544, y=361, width=150, height=65)
text14 = Label(canvas, text='5-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text14.config(bg='#ff9966')
text14.place(x=797, y=361, width=150, height=65)
text15 = Label(canvas, text='30-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text15.config(bg='#ff9966')
text15.place(x=1049, y=361, width=150, height=65)
    #speddast name's 4st line
text16 = Label(canvas, text='60-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text16.config(bg='#ff9966')
text16.place(x=36, y=514, width=150, height=65)
text17 = Label(canvas, text='3-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text17.config(bg='#ff9966')
text17.place(x=290, y=514, width=150, height=65)
text18 = Label(canvas, text='8-часовое \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text18.config(bg='#ff9966')
text18.place(x=544, y=514, width=150, height=65)
text19 = Label(canvas, text='15-часовое \nускорение', font=('Comic Sans MS', 17 ))
text19.config(bg='#ff9966')
text19.place(x=797, y=514, width=150, height=65)
text20 = Label(canvas, text='7-дневное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text20.config(bg='#ff9966')
text20.place(x=1049, y=514, width=150, height=65)

    #TOTAL TEXT


#ALL ENTER TEXT
    #speddast enter_text's 1st line
all1mint = Entry(canvas, font=('Comic Sans MS', 17,), bg='#ff7518')
all1mint.place(x=36, y=115, width=150, height=40)
all5mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all5mint.place(x=290, y=115, width=150, height=40)
all10mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all10mint.place(x=544, y=115, width=150, height=40)
all15mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all15mint.place(x=797, y=115, width=150, height=40)
all30mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all30mint.place(x=1049, y=115, width=150, height=40)
    #speddast enter_text's 2st line
all60mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all60mint.place(x=36, y=255, width=150, height=40)
all3hourt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all3hourt.place(x=290, y=255, width=150, height=40)
all8hourt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all8hourt.place(x=544, y=255, width=150, height=40)
all15hourt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all15hourt.place(x=797, y=255, width=150, height=40)
all7dayt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
all7dayt.place(x=1049, y=255, width=150, height=40)
    #speddast enter_text's 3st line
spec1mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec1mint.place(x=36, y=432, width=150, height=40)
spec5mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec5mint.place(x=290, y=432, width=150, height=40)
spec10mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec10mint.place(x=544, y=432, width=150, height=40)
spec15mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec15mint.place(x=797, y=432, width=150, height=40)
spec30mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec30mint.place(x=1049, y=432, width=150, height=40)
    #speddast enter_text's 4st line
spec60mint = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec60mint.place(x=36, y=585, width=150, height=40)
spec3hourt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec3hourt.place(x=290, y=585, width=150, height=40)
spec8hourt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec8hourt.place(x=544, y=585, width=150, height=40)
spec15hourt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec15hourt.place(x=797, y=585, width=150, height=40)
spec7dayt = Entry(canvas, font=('Comic Sans MS', 17), bg='#ff7518')
spec7dayt.place(x=1049, y=585, width=150, height=40)


#BUTTON PLACE
total_btn = Button(canvas, text='Результат', font=('Comic Sans MS', 24, 'bold'), command=totaldef)
total_btn.config(bg='#b22222', fg='#ff7518')
total_btn.place(x=962, y=637, width=236, height=70)

    #text of total_hours
totalhourstext = Label(canvas, text=f'ЧАСЫ: {totalhours}', font=('Comic Sans MS', 25))
totalhourstext.config(bg='#b22222', anchor=W, fg='#ff7518')
totalhourstext.place(x=36, y=637, width=329, height=70)

totaldaystext = Label(canvas, text=f'ДНИ: {totaldays}', font=('Comic Sans MS', 25))
totaldaystext.config(bg='#b22222', anchor=W,fg='#ff7518')
totaldaystext.place(x=365, y=637, width=328, height=70)

root.mainloop()