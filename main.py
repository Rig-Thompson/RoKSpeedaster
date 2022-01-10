from tkinter import *

def totaldef():
    totalhours = 'rabotaet chasy'
    return totalhours
    totaldays =  'rabotaet dni'
    return totaldays
#main settings of window
root = Tk()
root['bg'] = '#a7e0d9'
root.title('Let me take a selfie')
root.geometry('1280x720')
root.wm_attributes('-alpha', 0.65)

#canvas block
canvas = Canvas(root, height=720, width=1280, bg='#a7e0d9')
canvas.pack()

#ALL TEXT PLACE
alltext = Label(canvas, text='Общие ускорения', font=('Comic Sans MS', 17, 'bold')) #allest
alltext.config(bg='#a7e0d9')# speedast
alltext.place(x=1, y=8)
context = Label(canvas, text='Специальные ускорения', font=('Comic Sans MS', 17, 'bold')) #specia
context.config(bg='#a7e0d9')# l speedast
context.place(x=1, y=317)
    #speddast name's 1st line
text1 = Label(canvas, text='1-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text1.config(bg='#a7e0d9')
text1.place(x=36, y=44)
text2 = Label(canvas, text='5-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text2.config(bg='#a7e0d9')
text2.place(x=290, y=44)
text3 = Label(canvas, text='10-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text3.config(bg='#a7e0d9')
text3.place(x=544, y=44)
text4 = Label(canvas, text='15-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text4.config(bg='#a7e0d9')
text4.place(x=797, y=44)
text5 = Label(canvas, text='30-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text5.config(bg='#a7e0d9')
text5.place(x=1049, y=44)
    #speddast name's 2st line
text6 = Label(canvas, text='60-минутное \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text6.config(bg='#a7e0d9')
text6.place(x=36, y=186)
text7 = Label(canvas, text='3-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text7.config(bg='#a7e0d9')
text7.place(x=290, y=186)
text8 = Label(canvas, text='8-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text8.config(bg='#a7e0d9')
text8.place(x=544, y=186)
text9 = Label(canvas, text='15-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text9.config(bg='#a7e0d9')
text9.place(x=797, y=186)
text10 = Label(canvas, text='7-дневное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text10.config(bg='#a7e0d9')
text10.place(x=1049, y=186)
    #speddast name's 3st line
text11 = Label(canvas, text='1-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text11.config(bg='#a7e0d9')
text11.place(x=36, y=361)
text12 = Label(canvas, text='5-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text12.config(bg='#a7e0d9')
text12.place(x=290, y=361)
text13 = Label(canvas, text='10-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text13.config(bg='#a7e0d9')
text13.place(x=544, y=361)
text14 = Label(canvas, text='5-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text14.config(bg='#a7e0d9')
text14.place(x=797, y=361)
text15 = Label(canvas, text='30-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text15.config(bg='#a7e0d9')
text15.place(x=1049, y=361)
    #speddast name's 4st line
text16 = Label(canvas, text='60-минутное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text16.config(bg='#a7e0d9')
text16.place(x=36, y=514)
text17 = Label(canvas, text='3-часовое \nускорение', font=('Comic Sans MS', 17), justify=CENTER)
text17.config(bg='#a7e0d9')
text17.place(x=290, y=514)
text18 = Label(canvas, text='8-часовое \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text18.config(bg='#a7e0d9')
text18.place(x=544, y=514)
text19 = Label(canvas, text='15-часовое \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text19.config(bg='#a7e0d9')
text19.place(x=797, y=514)
text20 = Label(canvas, text='7-дневное \nускорение', font=('Comic Sans MS', 17 ), justify=CENTER)
text20.config(bg='#a7e0d9')
text20.place(x=1049, y=514)

    #TOTAL TEXT
totalhours = ' '
totaldays = ' '
totalhourstext = Label(canvas, text=totalhours, font=('Comic Sans MS', 17 ), justify=CENTER)
totalhourstext.config(bg='#a7e0d9')
totalhourstext.place(x=36, y=637)
totaldaystext = Label(canvas, text=totaldays, font=('Comic Sans MS', 17 ), justify=CENTER)
totaldaystext.config(bg='#a7e0d9')
totaldaystext.place(x=540, y=637)
    #just text of hours/days
hourstext = Label(canvas, text='ЧАСОВ', font=('Comic Sans MS', 17 ), justify=CENTER)
hourstext.config(bg='#a7e0d9')
hourstext.place(x=195, y=637)
daystext = Label(canvas, text='ДНЕЙ', font=('Comic Sans MS', 17 ), justify=CENTER)
daystext.config(bg='#a7e0d9')
daystext.place(x=710, y=637)

#ALL ENTER TEXT



#BUTTON PLACE
total_btn = Button(text='Итог', command=totaldef,)
total_btn.place(x=1049, y=637)



#frame
#frame = Frame(root)
#frame.place(relx=0.1, rely=0.1, relwidth=1, relheight=1)

root.mainloop()