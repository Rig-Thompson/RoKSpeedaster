from tkinter import *
#totalhours1 = 0
#main settings of window
root = Tk()

def totaldef():
    print('a')
#    all1min = all1mint.get()
#    all5min = all5mint.get()
#    totalhours1 = (int(all1min) + int(all5min))
#    totalhours = to#talhours1

root['bg'] = '#ff9966'
root.title('Rise of Kingdoms: Speedaster')
root.geometry('1280x720')
#root.wm_attributes('-alpha', 0.65)

#canvas block
canvas = Canvas(root, height=720, width=1280, bg='#ff9966')
canvas.pack()

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
text19 = Label(canvas, text='15-часовое \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text19.config(bg='#ff9966')
text19.place(x=797, y=514, width=150, height=65)
text20 = Label(canvas, text='7-дневное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text20.config(bg='#ff9966')
text20.place(x=1049, y=514, width=150, height=65)

    #TOTAL TEXT
totalhours = 0
totaldays = 0
totalhourstext = Label(canvas, text=totalhours, font=('Comic Sans MS', 25), justify=RIGHT)
totalhourstext.config(bg='#ff0000')
totalhourstext.place(x=36, y=637, width=200, height=70)
totaldaystext = Label(canvas, text=totaldays, font=('Comic Sans MS', 25), justify=RIGHT)
totaldaystext.config(bg='#ff0000')
totaldaystext.place(x=540, y=637, width=200, height=70)
    #just text of hours/days
hourstext = Label(canvas, text='ЧАСОВ', font=('Comic Sans MS', 25), justify=LEFT)
hourstext.config(bg='#ff0000')
hourstext.place(x=195, y=637, width=200, height=70)

daystext = Label(canvas, text='ДНЕЙ', font=('Comic Sans MS', 25), justify=LEFT)
daystext.config(bg='#ff0000')
daystext.place(x=710, y=637, width=200, height=70)

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
total_btn.place(x=962, y=637, width=236, height=65)



#frame
#frame = Frame(root)
#frame.place(relx=0.1, rely=0.1, relwidth=1, relheight=1)

root.mainloop()