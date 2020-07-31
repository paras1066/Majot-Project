import tkinter as tk
from tkinter import *
from tkinter import ttk

import mysql.connector
from PIL import ImageTk, Image
def main():
    global bb

    frame = Frame(root, height=700, width=180,bg = '#353839')
    frame.place(x=0, y=0)
    frame2 = Frame(root, height=700, width=1090)
    frame2.place(x=170, y=0)
    img6 = Image.open("main3.jpg")
    img6 = img6.resize((1090, 700), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)
    label300 = Label(frame2, image=img6)
    label300.image = img6
    label300.place(x=0, y=0)

    menu = Menu(root)
    menu.add_command(label="Back", command=destroy)
    root.config(menu=menu)
    bb = Button(frame,text = "Add Subject", width=17, height=2,command = add_sub ,bg = '#555555', fg = 'white',font=("DejaVu Sans Mono", 12))
    bb.place(x = 0 , y = 0)
    Button(frame, text="Add Teacher", width=17, height=2, command=add_teacher, font=("DejaVu Sans Mono", 12),fg = 'white',bg = '#555555').place(x=0, y=50)
    Button(frame, text="Create TT", width=17, height=2 , command = create_tt, font=("DejaVu Sans Mono", 12),fg = 'white',bg = '#555555').place(x=0, y=100)
    Button(frame, text="View TT", width=17, height=2, font=("DejaVu Sans Mono", 12),fg = 'white',bg = '#555555', command = view_tt).place(x=0, y=150)
def add_sub():
    global sub_name,sub_code,deptt2,sem, sub_type, combov, tree_sub
    sub_name = StringVar()
    sub_code = StringVar()
    deptt2 = StringVar()
    sem = StringVar()
    combov = StringVar()
    sub_type = StringVar()
    frame2 = Frame(root, height=700, width=1090)
    frame2.place(x=170, y=0)
    img6 = Image.open("main3.jpg")
    img6 = img6.resize((1090, 700), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)
    label300 = Label(frame2, image=img6)
    label300.image = img6
    label300.place(x=0, y=0)

    lst1 = ["AUTO", "CSE", "CIVIL", "ECE", "ELECTRICAL", "MECHANICAL"]
    Label(frame2, text="Subject Name", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=30)
    Entry(frame2,textvariable = sub_name, font=("DejaVu Sans Mono", 12)).place(x=200, y=30)
    Label(frame2, text="Subject Code", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=60)
    Entry(frame2,textvariable = sub_code, font=("DejaVu Sans Mono", 12)).place(x=200, y=60)
    Label(frame2, text="Type", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=90)
    Label(frame2, text="(Enter 'P' or 'T' only)", font=("DejaVu Sans Mono", 10),bg = '#353839', fg = 'white').place(x=420, y=90)
    Entry(frame2, textvariable=sub_type, font=("DejaVu Sans Mono", 12)).place(x=200, y=90)

    Label(frame2, text="Department", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=120)
    Entry(frame2,textvariable = deptt2, font=("DejaVu Sans Mono", 12)).place(x=200, y=120)
    Label(frame2, text="Semester", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=150)
    Entry(frame2,textvariable = sem, font=("DejaVu Sans Mono", 12)).place(x=200, y=150)
    Button(frame2, text="Add", command = sub_db, width = 15,font=("DejaVu Sans Mono", 14)).place(x=230, y=200)
    ttk.Combobox(frame2, values =lst1,textvariable = combov).place(x = 300, y = 300)
    Button(frame2, text = "Show", command = show_sub, font=("DejaVu Sans Mono", 13), width = 12).place(x = 500, y = 300)

    tree_sub = ttk.Treeview(frame2, column=("one", "two", "three", "four", "five"))
    tree_sub['show'] = 'headings'

    tree_sub.column("one", width=150, anchor='center')
    tree_sub.column("two", width=150, anchor='center')
    tree_sub.column("three", width=150, anchor='center')
    tree_sub.column("four", width=150, anchor='center')
    tree_sub.column("five", width=150, anchor='center')
    tree_sub.heading("one", text="Subject Name")
    tree_sub.heading("two", text="Subject code")
    tree_sub.heading("three", text="Department")
    tree_sub.heading("four", text="Type")
    tree_sub.heading("five", text="Semester")
    tree_sub.place(x =150, y = 340)
def show_sub():
    tree_sub.delete(*tree_sub.get_children())
    combovx = combov.get()
    lst = [combovx]
    sql = ("SELECT * FROM subjects WHERE deptt = %s")
    mycursor.execute(sql, lst)
    rows = mycursor.fetchall()
    c = 0
    for row in rows:
        tree_sub.insert("", tk.END, text=str(c),
                         values=(row[0], row[1], row[2], row[3], row[4]))
        c = c + 1
    mydb.commit()





def add_teacher():
    global name, idx, deptt4, short, combov2, tree_teach
    name = StringVar()
    idx = StringVar()
    deptt4 = StringVar()
    short = StringVar()
    combov2 = StringVar()
    frame2 = Frame(root, height=700, width=1090)
    frame2.place(x=170, y=0)
    img6 = Image.open("main3.jpg")
    img6 = img6.resize((1090, 700), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)
    label300 = Label(frame2, image=img6)
    label300.image = img6
    label300.place(x=0, y=0)
    lst1 = ["AUTO", "CSE", "CIVIL", "ECE", "ELECTRICAL", "MECHANICAL"]
    Label(frame2, text="Teacher name", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=30)
    Entry(frame2,textvariable = name, font=("DejaVu Sans Mono", 12)).place(x=200, y=30)
    Label(frame2, text="Teacher ID", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=60)
    Entry(frame2,textvariable = idx, font=("DejaVu Sans Mono", 12)).place(x=200, y=60)

    Label(frame2, text="Department", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=90)
    Entry(frame2,textvariable = deptt4, font=("DejaVu Sans Mono", 12)).place(x=200, y=90)
    Label(frame2, text="Short name", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=50, y=120)
    Entry(frame2,textvariable =short, font=("DejaVu Sans Mono", 12)).place(x=200, y=120)
    Button(frame2, text="Add", command = teacher_db, font=("DejaVu Sans Mono", 14), width = 15).place(x=230, y=160)
    ttk.Combobox(frame2, values=lst1, textvariable=combov2).place(x=300, y=260)
    Button(frame2, text="Show", command=show_teach, font=("DejaVu Sans Mono", 13), width = 11).place(x=500, y=260)
    tree_teach = ttk.Treeview(frame2, column=("one", "two", "three", "four"))
    tree_teach['show'] = 'headings'
    tree_teach.column("one", width=150, anchor='center')
    tree_teach.column("two", width=150, anchor='center')
    tree_teach.column("three", width=150, anchor='center')
    tree_teach.column("four", width=150, anchor='center')
    tree_teach.heading("one", text="Teacher Name")
    tree_teach.heading("two", text="Teacher ID")
    tree_teach.heading("three", text="Department")
    tree_teach.heading("four", text="Short Name")
    tree_teach.place(x=200, y=300)
def show_teach():
    tree_teach.delete(*tree_teach.get_children())
    combov2x = combov2.get()
    lst = [combov2x]
    sql = ("SELECT * FROM teachers WHERE deptt = %s")
    mycursor.execute(sql, lst)
    rows = mycursor.fetchall()
    c = 0
    for row in rows:
        tree_teach.insert("", tk.END, text=str(c),
                        values=(row[0], row[1], row[2], row[3]))
        c = c + 1
    mydb.commit()

def destroy():
    main()
def sub_db():
    subxx = sub_name.get()
    codexx = sub_code.get()
    deptxx = deptt2.get()
    semxx = sem.get()
    typexx = sub_type.get()
    lst = [subxx,codexx,typexx,deptxx,semxx]
    sql = ("INSERT INTO subjects VALUES(%s,%s,%s,%s,%s)")
    mycursor.execute(sql, lst)
    mydb.commit()

def teacher_db():
    namexx = name.get()
    idxx = idx.get()
    deptt4x = deptt4.get()
    shortxx = short.get()
    lst = [namexx,idxx ,deptt4x, shortxx]
    sql = ("INSERT INTO teachers VALUES(%s,%s,%s,%s)")
    mycursor.execute(sql, lst)
    mydb.commit()

def create_tt():
    global dept, semm, var1,var2,frame2y
    dept = StringVar()
    semm = StringVar()
    var1 = StringVar()
    var2 = StringVar()
    frame2y = Frame(root, height=700, width=1090)
    frame2y.place(x=170, y=0)
    img6 = Image.open("main3.jpg")
    img6 = img6.resize((1090, 700), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)
    label300 = Label(frame2y, image=img6)
    label300.image = img6
    label300.place(x=0, y=0)
    var1.set("---SELECT---")
    var2.set("0")
    lst1 = ["AUTO","CSE","CIVIL","ECE","ELECTRICAL","MECHANICAL"]
    lst2 = ["1","2","3","4","5","6"]
    # lst3 = ["Monady","Tuesday","Wednesday" ,"Thursday","Friday"]
    Label(frame2y,text = "Department:", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x = 100, y = 10)
    # ttk.Combobox(frame00, values = lst1, textvariable = dept,font = ("Lucida",16)).place(x = 500, y = 100)
    Label(frame2y, text="Sem:" , font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x=420, y=10)
    # ttk.Combobox(frame00, values =lst2, textvariable = semm,font = ("Lucida",16)).place(x = 500, y =200)
    # Label(frame1, text="Choose Day").place(x=650, y=30)
    # ttk.Combobox(frame1, values =lst3).place(x=650, y=50)
    opt1 = OptionMenu(frame2y,var1,"AUTO","CSE","CIVIL","ECE","ELECTRICAL","MECHANICAL")
    opt1.config(font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white')
    opt1.place(x = 230, y = 10)
    opt2 = OptionMenu(frame2y, var2, "1","2","3","4","5","6")
    opt2.config(font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white')
    opt2.place(x = 480, y =10)
    Button(frame2y, text = "GO", command = go,width = 10,font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x = 600, y = 10)


def go():
    global day
    day = StringVar()
    # frame1 = LabelFrame(frame00, text="Enter details", height=700, width=1150)
    # frame1.place(x=0, y=40)
    # frame2 = LabelFrame(root, text="Tuesday", height=230, width=650, bg='green')
    # frame2.place(x=0, y=230)
    # frame3 = LabelFrame(root, text="Wednesday", height=230, width=650, bg='green')
    # frame3.place(x=0, y=460)
    # frame4 = LabelFrame(root, text="Thursday", height=230, width=650, bg='green')
    # frame4.place(x=660, y=0)
    # frame5 = LabelFrame(root, text="Friday", height=230, width=650, bg='green')
    # frame5.place(x=660, y=230)
    # tabControl = ttk.Notebook(frame1)
    # tab1 = ttk.Frame(tabControl,height = 600, width=1150)
    # tab2 = ttk.Frame(tabControl,height = 600, width=1150)
    # tab3 = ttk.Frame(tabControl,height = 600, width=1150)
    # tab4 = ttk.Frame(tabControl, height= 600, width=1150)
    # tab6 = ttk.Frame(tabControl, height= 600, width=1150)
    # tabControl.add(tab1, text='Monday')
    # tabControl.add(tab2, text="Tuesday")
    # tabControl.add(tab3, text="Wednesday")
    # tabControl.add(tab4, text="Thursday")
    # tabControl.add(tab6, text="Friday")
    Label( frame2y, text = "Select day:", font=("DejaVu Sans Mono", 12),bg = '#353839', fg = 'white').place(x = 170, y = 60)
    Radiobutton( frame2y,text = "Monday", variable = day, value = "Monday", font=("DejaVu Sans Mono", 12), command = mondaytt,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x = 300, y = 60)
    Radiobutton( frame2y, text="Tuesday", variable=day, value="Tuesday", font=("DejaVu Sans Mono", 12), command = tuesdaytt,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=390, y=60)
    Radiobutton( frame2y, text="Wednesday", variable=day, value="Wednesday", font=("DejaVu Sans Mono", 12),bg = '#353839',command = wedtt, fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=490, y=60)
    Radiobutton( frame2y, text="Thursday", variable=day, value="Thursday", font=("DejaVu Sans Mono", 12),bg = '#353839',command = thurstt, fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=610, y=60)
    Radiobutton( frame2y, text="Friday", variable=day, value="Friday", font=("DejaVu Sans Mono", 12),bg = '#353839',command =fritt, fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=720, y=60)
    # Label(tab1, text="Lect 1",font = ("Lucida",10)).place(x=5, y=0)
    # Label(tab1, text="Lect 2",font = ("Lucida",10)).place(x=5, y=30)
    # Label(tab1, text="Lect 3",font = ("Lucida",10)).place(x=5, y=60)
    # Label(tab1, text="Lect 4",font = ("Lucida",10)).place(x=5, y=90)
    # Label(tab1, text="Lect 6",font = ("Lucida",10)).place(x=5, y=120)
    # Label(tab1, text="Lect 7",font = ("Lucida",10)).place(x=5, y=150)
    # Label(tab1, text="Lect 8",font = ("Lucida",10)).place(x=5, y=180)
    #
    # Label(frame1, text="Room",font = ("Lucida",10)).place(x=50, y=0)
    # ttk.Combobox(frame1,font = ("Lucida",10)).place(x=80, y=0)
    # Label(frame1, text="Subject",font = ("Lucida",10)).place(x=30, y=0)
    # ttk.Combobox(frame1,font = ("Lucida",10)).place(x=140, y=0)
    # Label(frame1, text="teacher",font = ("Lucida",10)).place(x=30, y=0)
    # ttk.Combobox(frame1,font = ("Lucida",10)).place(x=140, y=0)
    global res, res2, res3, res4, res5,sec1,sec2,secj
    var1xx = var1.get()
    var2xx = var2.get()
    lst = [var1xx]
    sql = ("SELECT room_no FROM room WHERE deptt = %s")
    mycursor.execute(sql, lst)
    rows = mycursor.fetchall()
    res = []
    for i in rows:
        for x in i:
            res.append(x)
    mydb.commit()

    lst = [var1xx]
    sql = ("SELECT room_no FROM lab WHERE deptt = %s")
    mycursor.execute(sql, lst)
    rows = mycursor.fetchall()
    res5 = []
    for i in rows:
        for x in i:
            res5.append(x)
    mydb.commit()

    var2xx = var2.get()
    xx = "T"
    lst1 = [var1xx, var2xx, xx]
    sql2 = ("SELECT sub_name FROM subjects WHERE deptt = %s AND sem = %s AND type = %s")
    mycursor.execute(sql2, lst1)
    rows2 = mycursor.fetchall()
    res2 = []
    for i in rows2:
        for x in i:
            res2.append(x)
    mydb.commit()

    xx2 = "P"
    lst2 = [var1xx, var2xx, xx2]
    sql3 = ("SELECT sub_name FROM subjects WHERE deptt = %s AND sem = %s AND type = %s")
    mycursor.execute(sql3, lst2)
    rows3 = mycursor.fetchall()
    res3 = []
    for i in rows3:
        for x in i:
            res3.append(x)
    mydb.commit()

    lst3 = [var1xx]
    sql4 = ("SELECT short_name FROM teachers WHERE deptt = %s")
    mycursor.execute(sql4, lst3)
    rows4 = mycursor.fetchall()
    res4 = []
    for i in rows4:
        for x in i:
            res4.append(x)
    mydb.commit()

    lst4 = [var1xx]
    sql5 = ("SELECT sec FROM deptt WHERE deptt = %s")
    mycursor.execute(sql5, lst4)
    rows5 = mycursor.fetchall()
    res6 = []
    for i in rows5:
        for x in i:
            res6.append(x)

    mydb.commit()
    a = res6[0]
    data = a.split(',')
    sec1 = data[0]
    sec2 = data[1]
    secj = sec1 + sec2
    print(sec1)
    print(sec2)
    print(secj)
def mondaytt():
     global frame2z,frame24,frame3,frame4,frame5,frame6, frame7,radio_var,radio_var2,radio_var3,radio_var4,radio_var5,radio_var6,radio_var7,radio_var1
     radio_var = StringVar()
     radio_var1 = StringVar()
     radio_var2 = StringVar()
     radio_var3 = StringVar()
     radio_var4 = StringVar()
     radio_var5 = StringVar()
     radio_var6 = StringVar()
     radio_var7 = StringVar()
     frame2z = LabelFrame(frame2y, text="Lect 1", height=130, width=550,bg = '#353839', fg = 'white')
     frame2z.place(x=5, y=110)
     frame24 = LabelFrame(frame2y, text="Lect 2", height=130, width=550,bg = '#353839', fg = 'white')
     frame24.place(x=5, y=240)
     frame3 = LabelFrame(frame2y, text="Lect 3", height=130, width=550,bg = '#353839', fg = 'white')
     frame3.place(x=5, y=370)
     frame4 = LabelFrame(frame2y, text="Lect 4", height=130, width=550,bg = '#353839', fg = 'white')
     frame4.place(x=5, y=500)
     frame5 = LabelFrame(frame2y, text="Lect 6", height=130, width=550,bg = '#353839', fg = 'white')
     frame5.place(x=560, y=110)
     frame6 = LabelFrame(frame2y, text="Lect 7", height=130, width=550,bg = '#353839', fg = 'white')
     frame6.place(x=560, y=240)
     frame7 = LabelFrame(frame2y, text="Lect 8", height=130, width=550,bg = '#353839', fg = 'white')
     frame7.place(x=560, y=370)
     Label(frame2z, text="Class type: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=5)
     Radiobutton(frame2z, text="Lecture Hall", variable=radio_var, value=1, font=("Lucida", 10),bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black', command=radiox).place(x=80, y=5)
     Radiobutton(frame2z, text="Lab", variable=radio_var, value=10, font=("Lucida", 10), command=radiox1,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=190, y=5)

     Label(frame24, text="Class type: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=5)
     Radiobutton(frame24, text="Lecture Hall", variable=radio_var1, value=2, font=("Lucida", 10),
                           command=radiox,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=80, y=5)
     Radiobutton(frame24, text="Lab", variable=radio_var1, value=20, font=("Lucida", 10), command=radiox1,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=190, y=5)

     Label(frame3, text="Class type: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=5)
     Radiobutton(frame3, text="Lecture Hall", variable=radio_var2, value=3, font=("Lucida", 10),
                           command=radiox,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=80, y=5)
     Radiobutton(frame3, text="Lab", variable=radio_var2, value=30, font=("Lucida", 10), command=radiox1,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=190, y=5)

     Label(frame4, text="Class type: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=5)
     Radiobutton(frame4, text="Lecture Hall", variable=radio_var3, value=4, font=("Lucida", 10),
                           command=radiox,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=80, y=5)
     Radiobutton(frame4, text="Lab", variable=radio_var3, value=40, font=("Lucida", 10), command=radiox1,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=190, y=5)

     Label(frame5, text="Class type: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=5)
     Radiobutton(frame5, text="Lecture Hall", variable=radio_var4, value=6, font=("Lucida", 10),
                           command=radiox,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=80, y=5)
     Radiobutton(frame5, text="Lab", variable=radio_var4, value=60, font=("Lucida", 10), command=radiox1,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=190, y=5)


     Label(frame6, text="Class type: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=5)
     Radiobutton(frame6, text="Lecture Hall", variable=radio_var5, value=7, font=("Lucida", 10),
                          command=radiox,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=80, y=5)
     Radiobutton(frame6, text="Lab", variable=radio_var5, value=70, font=("Lucida", 10), command=radiox1,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=190, y=5)

     Label(frame7, text="Class type: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=5)
     Radiobutton(frame7, text="Lecture Hall", variable=radio_var6, value=8, font=("Lucida", 10),
                           command=radiox,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=80, y=5)
     Radiobutton(frame7, text="Lab", variable=radio_var6, value=80, font=("Lucida", 10), command=radiox1,bg = '#353839', fg = 'white',activebackground = 'black',activeforeground = 'white', selectcolor = 'black').place(x=190, y=5)

def tuesdaytt():
    global frame2z, frame24, frame3, frame4, frame5, frame6, frame7, radio_var, radio_var2, radio_var3, radio_var4, radio_var5, radio_var6, radio_var1
    radio_var = StringVar()
    radio_var2 = StringVar()
    radio_var3 = StringVar()
    radio_var4 = StringVar()
    radio_var5 = StringVar()
    radio_var6 = StringVar()
    radio_var1 = StringVar()
    frame2z = LabelFrame(frame2y, text="Lect 1", height=130, width=550, bg='#353839', fg='white')
    frame2z.place(x=5, y=110)
    frame24 = LabelFrame(frame2y, text="Lect 2", height=130, width=550, bg='#353839', fg='white')
    frame24.place(x=5, y=240)
    frame3 = LabelFrame(frame2y, text="Lect 3", height=130, width=550, bg='#353839', fg='white')
    frame3.place(x=5, y=370)
    frame4 = LabelFrame(frame2y, text="Lect 4", height=130, width=550, bg='#353839', fg='white')
    frame4.place(x=5, y=500)
    frame5 = LabelFrame(frame2y, text="Lect 6", height=130, width=550, bg='#353839', fg='white')
    frame5.place(x=560, y=110)
    frame6 = LabelFrame(frame2y, text="Lect 7", height=130, width=550, bg='#353839', fg='white')
    frame6.place(x=560, y=240)
    frame7 = LabelFrame(frame2y, text="Lect 8", height=130, width=550, bg='#353839', fg='white')
    frame7.place(x=560, y=370)
    Label(frame2z, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame2z, text="Lecture Hall", variable=radio_var, value=1, font=("Lucida", 10), bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black',
                command=radiox).place(x=80, y=5)
    Radiobutton(frame2z, text="Lab", variable=radio_var, value=10, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame24, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame24, text="Lecture Hall", variable=radio_var1, value=2, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame24, text="Lab", variable=radio_var1, value=20, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame3, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame3, text="Lecture Hall", variable=radio_var2, value=3, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame3, text="Lab", variable=radio_var2, value=30, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame4, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame4, text="Lecture Hall", variable=radio_var3, value=4, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame4, text="Lab", variable=radio_var3, value=40, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame5, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame5, text="Lecture Hall", variable=radio_var4, value=6, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame5, text="Lab", variable=radio_var4, value=60, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame6, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame6, text="Lecture Hall", variable=radio_var5, value=7, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame6, text="Lab", variable=radio_var5, value=70, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame7, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame7, text="Lecture Hall", variable=radio_var6, value=8, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame7, text="Lab", variable=radio_var6, value=80, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)


def wedtt():
    global frame2z, frame24, frame3, frame4, frame5, frame6, frame7, radio_var, radio_var2, radio_var3, radio_var4, radio_var5, radio_var6, radio_var1
    radio_var = StringVar()
    radio_var2 = StringVar()
    radio_var3 = StringVar()
    radio_var4 = StringVar()
    radio_var5 = StringVar()
    radio_var6 = StringVar()
    radio_var1 = StringVar()
    frame2z = LabelFrame(frame2y, text="Lect 1", height=130, width=550, bg='#353839', fg='white')
    frame2z.place(x=5, y=110)
    frame24 = LabelFrame(frame2y, text="Lect 2", height=130, width=550, bg='#353839', fg='white')
    frame24.place(x=5, y=240)
    frame3 = LabelFrame(frame2y, text="Lect 3", height=130, width=550, bg='#353839', fg='white')
    frame3.place(x=5, y=370)
    frame4 = LabelFrame(frame2y, text="Lect 4", height=130, width=550, bg='#353839', fg='white')
    frame4.place(x=5, y=500)
    frame5 = LabelFrame(frame2y, text="Lect 6", height=130, width=550, bg='#353839', fg='white')
    frame5.place(x=560, y=110)
    frame6 = LabelFrame(frame2y, text="Lect 7", height=130, width=550, bg='#353839', fg='white')
    frame6.place(x=560, y=240)
    frame7 = LabelFrame(frame2y, text="Lect 8", height=130, width=550, bg='#353839', fg='white')
    frame7.place(x=560, y=370)
    Label(frame2z, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame2z, text="Lecture Hall", variable=radio_var, value=1, font=("Lucida", 10), bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black',
                command=radiox).place(x=80, y=5)
    Radiobutton(frame2z, text="Lab", variable=radio_var, value=10, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame24, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame24, text="Lecture Hall", variable=radio_var1, value=2, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame24, text="Lab", variable=radio_var1, value=20, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame3, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame3, text="Lecture Hall", variable=radio_var2, value=3, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame3, text="Lab", variable=radio_var2, value=30, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame4, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame4, text="Lecture Hall", variable=radio_var3, value=4, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame4, text="Lab", variable=radio_var3, value=40, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame5, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame5, text="Lecture Hall", variable=radio_var4, value=6, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame5, text="Lab", variable=radio_var4, value=60, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame6, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame6, text="Lecture Hall", variable=radio_var5, value=7, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame6, text="Lab", variable=radio_var5, value=70, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame7, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame7, text="Lecture Hall", variable=radio_var6, value=8, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame7, text="Lab", variable=radio_var6, value=80, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)



def thurstt():
    global frame2z, frame24, frame3, frame4, frame5, frame6, frame7, radio_var, radio_var2, radio_var3, radio_var4, radio_var5, radio_var6, radio_var1
    radio_var = StringVar()
    radio_var2 = StringVar()
    radio_var3 = StringVar()
    radio_var4 = StringVar()
    radio_var5 = StringVar()
    radio_var6 = StringVar()
    radio_var1 = StringVar()
    frame2z = LabelFrame(frame2y, text="Lect 1", height=130, width=550, bg='#353839', fg='white')
    frame2z.place(x=5, y=110)
    frame24 = LabelFrame(frame2y, text="Lect 2", height=130, width=550, bg='#353839', fg='white')
    frame24.place(x=5, y=240)
    frame3 = LabelFrame(frame2y, text="Lect 3", height=130, width=550, bg='#353839', fg='white')
    frame3.place(x=5, y=370)
    frame4 = LabelFrame(frame2y, text="Lect 4", height=130, width=550, bg='#353839', fg='white')
    frame4.place(x=5, y=500)
    frame5 = LabelFrame(frame2y, text="Lect 6", height=130, width=550, bg='#353839', fg='white')
    frame5.place(x=560, y=110)
    frame6 = LabelFrame(frame2y, text="Lect 7", height=130, width=550, bg='#353839', fg='white')
    frame6.place(x=560, y=240)
    frame7 = LabelFrame(frame2y, text="Lect 8", height=130, width=550, bg='#353839', fg='white')
    frame7.place(x=560, y=370)
    Label(frame2z, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame2z, text="Lecture Hall", variable=radio_var, value=1, font=("Lucida", 10), bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black',
                command=radiox).place(x=80, y=5)
    Radiobutton(frame2z, text="Lab", variable=radio_var, value=10, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame24, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame24, text="Lecture Hall", variable=radio_var1, value=2, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame24, text="Lab", variable=radio_var1, value=20, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame3, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame3, text="Lecture Hall", variable=radio_var2, value=3, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame3, text="Lab", variable=radio_var2, value=30, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame4, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame4, text="Lecture Hall", variable=radio_var3, value=4, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame4, text="Lab", variable=radio_var3, value=40, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame5, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame5, text="Lecture Hall", variable=radio_var4, value=6, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame5, text="Lab", variable=radio_var4, value=60, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame6, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame6, text="Lecture Hall", variable=radio_var5, value=7, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame6, text="Lab", variable=radio_var5, value=70, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame7, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame7, text="Lecture Hall", variable=radio_var6, value=8, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame7, text="Lab", variable=radio_var6, value=80, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)


def fritt():
    global frame2z, frame24, frame3, frame4, frame5, frame6, frame7, radio_var, radio_var2, radio_var3, radio_var4, radio_var5, radio_var6, radio_var1
    radio_var = StringVar()
    radio_var2 = StringVar()
    radio_var3 = StringVar()
    radio_var4 = StringVar()
    radio_var5 = StringVar()
    radio_var6 = StringVar()
    radio_var1 = StringVar()
    frame2z = LabelFrame(frame2y, text="Lect 1", height=130, width=550, bg='#353839', fg='white')
    frame2z.place(x=5, y=110)
    frame24 = LabelFrame(frame2y, text="Lect 2", height=130, width=550, bg='#353839', fg='white')
    frame24.place(x=5, y=240)
    frame3 = LabelFrame(frame2y, text="Lect 3", height=130, width=550, bg='#353839', fg='white')
    frame3.place(x=5, y=370)
    frame4 = LabelFrame(frame2y, text="Lect 4", height=130, width=550, bg='#353839', fg='white')
    frame4.place(x=5, y=500)
    frame5 = LabelFrame(frame2y, text="Lect 6", height=130, width=550, bg='#353839', fg='white')
    frame5.place(x=560, y=110)
    frame6 = LabelFrame(frame2y, text="Lect 7", height=130, width=550, bg='#353839', fg='white')
    frame6.place(x=560, y=240)
    frame7 = LabelFrame(frame2y, text="Lect 8", height=130, width=550, bg='#353839', fg='white')
    frame7.place(x=560, y=370)
    Label(frame2z, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame2z, text="Lecture Hall", variable=radio_var, value=1, font=("Lucida", 10), bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black',
                command=radiox).place(x=80, y=5)
    Radiobutton(frame2z, text="Lab", variable=radio_var, value=10, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame24, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame24, text="Lecture Hall", variable=radio_var1, value=2, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame24, text="Lab", variable=radio_var1, value=20, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame3, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame3, text="Lecture Hall", variable=radio_var2, value=3, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame3, text="Lab", variable=radio_var2, value=30, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame4, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame4, text="Lecture Hall", variable=radio_var3, value=4, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame4, text="Lab", variable=radio_var3, value=40, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame5, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame5, text="Lecture Hall", variable=radio_var4, value=6, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame5, text="Lab", variable=radio_var4, value=60, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame6, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame6, text="Lecture Hall", variable=radio_var5, value=7, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame6, text="Lab", variable=radio_var5, value=70, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)

    Label(frame7, text="Class type: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=5)
    Radiobutton(frame7, text="Lecture Hall", variable=radio_var6, value=8, font=("Lucida", 10),
                command=radiox, bg='#353839', fg='white', activebackground='black', activeforeground='white',
                selectcolor='black').place(x=80, y=5)
    Radiobutton(frame7, text="Lab", variable=radio_var6, value=80, font=("Lucida", 10), command=radiox1, bg='#353839',
                fg='white', activebackground='black', activeforeground='white', selectcolor='black').place(x=190, y=5)


def radiox():
    global e11,e13,e12,sec2, lectt,room1,sub1,teach1,ctype
    room1 = StringVar()
    sub1 = StringVar()
    teach1 = StringVar()
    xradio = radio_var.get()
    xradio1 = radio_var1.get()
    xradio2 = radio_var2.get()
    xradio3 = radio_var3.get()
    xradio4 = radio_var4.get()
    xradio5 = radio_var5.get()
    xradio6 = radio_var6.get()
    ctype = 'T'
    if xradio == '1':
        fx1 = Frame(frame2z, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        lectt = 1

        Label(fx1, text="Room No.: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=0)
        e11 = ttk.Combobox(fx1,values = res, font=("Lucida", 10),textvariable = room1)
        e11.place(x = 80, y = 0)
        Label(fx1, text="Subject: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=20)
        e12 = ttk.Combobox(fx1, values = res2, font=("Lucida", 10),textvariable = sub1)
        e12.place(x=80, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=40)
        e13 = ttk.Combobox(fx1,values = res4, font=("Lucida", 10),textvariable = teach1)
        e13.place(x=80, y=40)
        Button(fx1, text="Save", command = pkdb,bg = 'white',fg = 'black').place(x=250, y=30)

    if xradio1 == '2':
        fx1 = Frame(frame24, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        lectt = 2
        Label(fx1, text="Room No.: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=0)
        e11 = ttk.Combobox(fx1, values=res, font=("Lucida", 10),textvariable = room1)
        e11.place(x=80, y=0)
        Label(fx1, text="Subject: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=20)
        e12 = ttk.Combobox(fx1, values=res2, font=("Lucida", 10),textvariable = sub1)
        e12.place(x=80, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10),bg = '#353839', fg = 'white').place(x=5, y=40)
        e13 = ttk.Combobox(fx1, values=res4, font=("Lucida", 10),textvariable = teach1)
        e13.place(x=80, y=40)
        Button(fx1, text="Save", command = pkdb,bg = 'white',fg = 'black').place(x=250, y=30)
    if xradio2 == '3':
        lectt = 3
        fx1 = Frame(frame3, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        Label(fx1, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        e11 = ttk.Combobox(fx1, values=res, font=("Lucida", 10), textvariable=room1)
        e11.place(x=80, y=0)
        Label(fx1, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        e12 = ttk.Combobox(fx1, values=res2, font=("Lucida", 10), textvariable=sub1)
        e12.place(x=80, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        e13 = ttk.Combobox(fx1, values=res4, font=("Lucida", 10), textvariable=teach1)
        e13.place(x=80, y=40)
        Button(fx1, text="Save", command = pkdb,bg = 'white',fg = 'black').place(x=250, y=30)
    if xradio3 == '4':
        fx1 = Frame(frame4, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        lectt = 4
        Label(fx1, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        e11 = ttk.Combobox(fx1, values=res, font=("Lucida", 10), textvariable=room1)
        e11.place(x=80, y=0)
        Label(fx1, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        e12 = ttk.Combobox(fx1, values=res2, font=("Lucida", 10), textvariable=sub1)
        e12.place(x=80, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        e13 = ttk.Combobox(fx1, values=res4, font=("Lucida", 10), textvariable=teach1)
        e13.place(x=80, y=40)
        Button(fx1, text="Save", command = pkdb,bg = 'white',fg = 'black').place(x=250, y=30)

    if xradio4 == '6':
        fx1 = Frame(frame5, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        lectt = 6
        Label(fx1, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        e11 = ttk.Combobox(fx1, values=res, font=("Lucida", 10), textvariable=room1)
        e11.place(x=80, y=0)
        Label(fx1, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        e12 = ttk.Combobox(fx1, values=res2, font=("Lucida", 10), textvariable=sub1)
        e12.place(x=80, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        e13 = ttk.Combobox(fx1, values=res4, font=("Lucida", 10), textvariable=teach1)
        e13.place(x=80, y=40)
        Button(fx1, text="Save", command=pkdb, bg='white', fg='black').place(x=250, y=30)
    if xradio5 == '7':
        fx1 = Frame(frame6, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        lectt = 7
        Label(fx1, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        e11 = ttk.Combobox(fx1, values=res, font=("Lucida", 10), textvariable=room1)
        e11.place(x=80, y=0)
        Label(fx1, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        e12 = ttk.Combobox(fx1, values=res2, font=("Lucida", 10), textvariable=sub1)
        e12.place(x=80, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        e13 = ttk.Combobox(fx1, values=res4, font=("Lucida", 10), textvariable=teach1)
        e13.place(x=80, y=40)
        Button(fx1, text="Save", command = pkdb,bg = 'white',fg = 'black').place(x=250, y=30)

    if xradio6 == '8':
        fx1 = Frame(frame7, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        lectt = 8
        Label(fx1, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        e11 = ttk.Combobox(fx1, values=res, font=("Lucida", 10), textvariable=room1)
        e11.place(x=80, y=0)
        Label(fx1, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        e12 = ttk.Combobox(fx1, values=res2, font=("Lucida", 10), textvariable=sub1)
        e12.place(x=80, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        e13 = ttk.Combobox(fx1, values=res4, font=("Lucida", 10), textvariable=teach1)
        e13.place(x=80, y=40)
        Button(fx1, text="Save", command=pkdb, bg='white', fg='black').place(x=250, y=30)


def radiox1():
    global roomm,rooml, subl, subm , teachl, teachm,lect2,sem2,sec2,sec2x,sec2y,ctype,lectt
    roomm = StringVar()
    rooml = StringVar()
    subl =  StringVar()
    subm =  StringVar()
    teachl =StringVar()
    teachm =StringVar()
    xradio = radio_var.get()
    xradio1 = radio_var1.get()
    xradio2 = radio_var2.get()
    xradio3 = radio_var3.get()
    xradio4 = radio_var4.get()
    xradio5 = radio_var5.get()
    xradio6 = radio_var6.get()
    ctype = 'P'
    sec2x = sec1
    sec2y = sec2
    if xradio == '10':

        lectt = 1
        fx1 = Frame(frame2z, height=67, width=580, bg='#353839')
        fx1.place(x=0, y=35)
        Label(fx1, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        ttk.Combobox(fx1, font=("Lucida", 10), textvariable=rooml,values=res5).place(x=80, y=0)
        Label(fx1, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=0)
        ttk.Combobox(fx1, font=("Lucida", 10), textvariable=roomm,values=res5).place(x=310, y=0)
        Label(fx1, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=0)
        Label(fx1, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        Label(fx1, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=20)
        ttk.Combobox(fx1, font=("Lucida", 10), textvariable=subl,values=res3).place(x=80, y=20)
        Label(fx1, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=20)
        ttk.Combobox(fx1, font=("Lucida", 10), textvariable=subm,values=res3).place(x=310, y=20)
        Label(fx1, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        Label(fx1, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=40)
        ttk.Combobox(fx1, font=("Lucida", 10), textvariable=teachl,values=res4).place(x=80, y=40)
        Label(fx1, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=40)
        ttk.Combobox(fx1, font=("Lucida", 10), textvariable=teachm,values=res4).place(x=310, y=40)
        Button(fx1,text = "Save", command = pkdb,bg = 'white',fg = 'black').place(x = 480,y=0)
    # if xradio == '2':
    if xradio1 == '20':
        lectt = 2
        fx2 = Frame(frame24, height=67, width=580, bg='#353839')
        fx2.place(x=0, y=35)
        Label(fx2, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        ttk.Combobox(fx2, font=("Lucida", 10), textvariable=rooml, values = res5).place(x=80, y=0)
        Label(fx2, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=0)
        ttk.Combobox(fx2, font=("Lucida", 10), textvariable=roomm, values = res5).place(x=310, y=0)
        Label(fx2, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=0)
        Label(fx2, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        Label(fx2, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=20)
        ttk.Combobox(fx2, font=("Lucida", 10), textvariable=subl, values = res3).place(x=80, y=20)
        Label(fx2, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=20)
        ttk.Combobox(fx2, font=("Lucida", 10), textvariable=subm, values = res3).place(x=310, y=20)
        Label(fx2, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        Label(fx2, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=40)
        ttk.Combobox(fx2, font=("Lucida", 10), textvariable=teachl, values = res4).place(x=80, y=40)
        Label(fx2, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=40)
        ttk.Combobox(fx2, font=("Lucida", 10), textvariable=teachm, values = res4).place(x=310, y=40)
        Button(fx2, text="Save", command=pkdb, bg='white', fg='black').place(x=480, y=0)
    if xradio2 == '30':
        lectt = 3
        fx3 = Frame(frame3, height=67, width=580, bg='#353839')
        fx3.place(x=0, y=35)
        Label(fx3, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        ttk.Combobox(fx3, font=("Lucida", 10), textvariable=rooml, values = res5).place(x=80, y=0)
        Label(fx3, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=0)
        ttk.Combobox(fx3, font=("Lucida", 10), textvariable=roomm, values = res5).place(x=310, y=0)
        Label(fx3, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=0)
        Label(fx3, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        Label(fx3, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=20)
        ttk.Combobox(fx3, font=("Lucida", 10), textvariable=subl, values = res3).place(x=80, y=20)
        Label(fx3, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=20)
        ttk.Combobox(fx3, font=("Lucida", 10), textvariable=subm, values = res3).place(x=310, y=20)
        Label(fx3, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        Label(fx3, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=40)
        ttk.Combobox(fx3, font=("Lucida", 10), textvariable=teachl, values = res4).place(x=80, y=40)
        Label(fx3, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=40)
        ttk.Combobox(fx3, font=("Lucida", 10), textvariable=teachm, values = res4).place(x=310, y=40)
        Button(fx3, text="Save", command=pkdb, bg='white', fg='black').place(x=480, y=0)
    if xradio3 == '40':
        lectt = 4
        fx4 = Frame(frame4, height=67, width=580, bg='#353839')
        fx4.place(x=0, y=35)
        Label(fx4, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        ttk.Combobox(fx4, font=("Lucida", 10), textvariable=rooml, values = res5).place(x=80, y=0)
        Label(fx4, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=0)
        ttk.Combobox(fx4, font=("Lucida", 10), textvariable=roomm, values = res5).place(x=310, y=0)
        Label(fx4, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=0)
        Label(fx4, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        Label(fx4, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=20)
        ttk.Combobox(fx4, font=("Lucida", 10), textvariable=subl, values = res3).place(x=80, y=20)
        Label(fx4, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=20)
        ttk.Combobox(fx4, font=("Lucida", 10), textvariable=subm, values = res3).place(x=310, y=20)
        Label(fx4, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        Label(fx4, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=40)
        ttk.Combobox(fx4, font=("Lucida", 10), textvariable=teachl, values = res4).place(x=80, y=40)
        Label(fx4, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=40)
        ttk.Combobox(fx4, font=("Lucida", 10), textvariable=teachm, values = res4).place(x=310, y=40)
        Button(fx4,text = "Save", command = pkdb,bg = 'white',fg = 'black').place(x = 480,y=0)
    if xradio4 == '60':
        lectt = 6
        fx5 = Frame(frame5, height=67, width=580, bg='#353839')
        fx5.place(x=0, y=35)
        Label(fx5, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        ttk.Combobox(fx5, font=("Lucida", 10), textvariable=rooml, values = res5).place(x=80, y=0)
        Label(fx5, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=0)
        ttk.Combobox(fx5, font=("Lucida", 10), textvariable=roomm, values = res5).place(x=310, y=0)
        Label(fx5, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=0)
        Label(fx5, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        Label(fx5, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=20)
        ttk.Combobox(fx5, font=("Lucida", 10), textvariable=subl, values = res3).place(x=80, y=20)
        Label(fx5, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=20)
        ttk.Combobox(fx5, font=("Lucida", 10), textvariable=subm, values = res3).place(x=310, y=20)
        Label(fx5, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        Label(fx5, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=40)
        ttk.Combobox(fx5, font=("Lucida", 10), textvariable=teachl, values = res4).place(x=80, y=40)
        Label(fx5, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=40)
        ttk.Combobox(fx5, font=("Lucida", 10), textvariable=teachm, values = res4).place(x=310, y=40)
        Button(fx5,text = "Save", command = pkdb,bg = 'white',fg = 'black').place(x = 480,y=0)
    if xradio5 == '70':
        lectt = 7
        fx6 = Frame(frame6, height=67, width=580, bg='#353839')
        fx6.place(x=0, y=35)
        Label(fx6, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        ttk.Combobox(fx6, font=("Lucida", 10), textvariable=rooml, values = res5).place(x=80, y=0)
        Label(fx6, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=0)
        ttk.Combobox(fx6, font=("Lucida", 10), textvariable=roomm, values = res5).place(x=310, y=0)
        Label(fx6, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=0)
        Label(fx6, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        Label(fx6, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=20)
        ttk.Combobox(fx6, font=("Lucida", 10), textvariable=subl, values = res3).place(x=80, y=20)
        Label(fx6, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=20)
        ttk.Combobox(fx6, font=("Lucida", 10), textvariable=subm, values = res3).place(x=310, y=20)
        Label(fx6, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        Label(fx6, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=40)
        ttk.Combobox(fx6, font=("Lucida", 10), textvariable=teachl, values = res4).place(x=80, y=40)
        Label(fx6, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=40)
        ttk.Combobox(fx6, font=("Lucida", 10), textvariable=teachm, values = res4).place(x=310, y=40)
        Button(fx6,text = "Save", command = pkdb,bg = 'white',fg = 'black').place(x = 480,y=0)
    if xradio6 == '80':
        lectt = 8
        fx7 = Frame(frame7, height=67, width=580, bg='#353839')
        fx7.place(x=0, y=35)
        Label(fx7, text="Room No.: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=0)
        ttk.Combobox(fx7, font=("Lucida", 10), textvariable=rooml, values = res5).place(x=80, y=0)
        Label(fx7, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=0)
        ttk.Combobox(fx7, font=("Lucida", 10), textvariable=roomm, values = res5).place(x=310, y=0)
        Label(fx7, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=0)
        Label(fx7, text="Subject: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=20)
        Label(fx7, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=20)
        ttk.Combobox(fx7, font=("Lucida", 10), textvariable=subl, values = res3).place(x=80, y=20)
        Label(fx7, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=20)
        ttk.Combobox(fx7, font=("Lucida", 10), textvariable=subm, values = res3).place(x=310, y=20)
        Label(fx7, text="Teacher: ", font=("Lucida", 10), bg='#353839', fg='white').place(x=5, y=40)
        Label(fx7, text="(L sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=240, y=40)
        ttk.Combobox(fx7, font=("Lucida", 10), textvariable=teachl, values = res4).place(x=80, y=40)
        Label(fx7, text="(M sec)", font=("Lucida", 10), bg='#353839', fg='white').place(x=470, y=40)
        ttk.Combobox(fx7, font=("Lucida", 10), textvariable=teachm, values = res4).place(x=310, y=40)
        Button(fx7, text="Save", command=pkdb, bg='white', fg='black').place(x=480, y=0)

def pkdb():
    ctypex = ctype
    dayx = day.get()
    lecttx = lectt
    var1x = var1.get()
    var2x = var2.get()
    if ctypex == "T":
        room1x = room1.get()
        sub1x = sub1.get()
        teach1x = teach1.get()
        lst = [lecttx,var1x,teach1x,var2x,secj,room1x,sub1x,ctypex,dayx]
        sql = ("INSERT INTO main VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        mycursor.execute(sql, lst)
        mydb.commit()
    if ctypex == "P":
        roommx = roomm.get()
        roomlx = rooml.get()
        sublx = subl.get()
        submx = subm.get()
        teachlx = teachl.get()
        teachmx = teachm.get()
        lst2 = [lecttx,var1x,teachlx,var2x,sec2x ,roomlx,sublx,ctypex,dayx]
        lst3 = [lecttx, var1x,teachmx, var2x, sec2y,roommx, submx, ctypex, dayx]
        sql1 = ("INSERT INTO main VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        sql2 = ("INSERT INTO main VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        mycursor.execute(sql1, lst2)
        mycursor.execute(sql2, lst3)
        mydb.commit()

def view_tt():
    global deptv,semv,dayv, frame02
    deptv = StringVar()
    semv = StringVar()
    dayv = StringVar()
    frame02 = Frame(root, height=700, width=1090)
    frame02.place(x=170, y=0)
    img6 = Image.open("main3.jpg")
    img6 = img6.resize((1090, 700), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)
    label300 = Label(frame02, image=img6)
    label300.image = img6
    label300.place(x=0, y=0)
    lst = ["CSE", "CIVIL", "ECE", "ELECTRICAL", "MECHANICAL", "AUTO"]
    lst1 = [1,2,3,4,5,6]
    lst2 = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
    Label(frame02, text="Deptt. : ", font=("Lucida", 14), bg='#353839', fg='white').place(x=20, y=30)
    ttk.Combobox(frame02, values=lst, font=("Lucida", 14),textvariable = deptv).place(x =100, y = 30)
    Label(frame02, text="Sem. : ", font=("Lucida", 14), bg='#353839', fg='white').place(x=20, y=60)
    ttk.Combobox(frame02, values=lst1, font=("Lucida", 14),textvariable = semv).place(x=100, y=60)
    Label(frame02, text="Day. : ", font=("Lucida", 14), bg='#353839', fg='white').place(x=20, y=90)
    ttk.Combobox(frame02, values=lst2, font=("Lucida", 14),textvariable = dayv).place(x=100, y=90)
    Button(frame02, text="Show", width=17, height=2, command=show_tt, font=("DejaVu Sans Mono", 12),
           fg='white', bg='#555555').place(x=150, y=140)
    Button(frame02, text="Delete this TT", width=17, height=2, command=delete_tt, font=("DejaVu Sans Mono", 12),
           fg='white', bg='#555555').place(x=150, y=340)
    img6 = Image.open("pkk.png")
    img6 = img6.resize((300, 620), Image.ANTIALIAS)
    img6 = ImageTk.PhotoImage(img6)
    label300 = Label(frame02, image=img6)
    label300.image = img6
    label300.place(x=500, y=15)

def delete_tt():
    deptvxx = deptv.get()
    semvxx = semv.get()
    dayvxx = dayv.get()
    lst = [deptvxx,semvxx,dayvxx]
    sql = ("DELETE FROM main WHERE deptt = %s,sem = %s,dayvxx = %s")
    mycursor.execute(sql,lst)
    mydb.commit()

def show_tt():
    global lec, teach, sec, room, sub, types,secc1, secc2
    deptvxx = deptv.get()
    semvxx = semv.get()
    dayvxx = dayv.get()
    lst2 = [deptvxx]
    sql2 = ("SELECT sec FROM deptt WHERE deptt = %s")
    mycursor.execute(sql2, lst2)
    roww = mycursor.fetchall()
    for y in roww:
        m = y[0]
    d = m.split(',')
    secc1 = d[0]
    secc2 = d[1]
    mydb.commit()
    lst = [deptvxx,semvxx,dayvxx]

    sql = ("SELECT lect_no, teacher, section, room, subject, type FROM main WHERE deptt=%s and sem=%s and day=%s ORDER BY lect_no ASC")

    mycursor.execute(sql, lst)

    rows = mycursor.fetchall()
    mydb.commit()
    for x in rows:
        (lec, teach, sec, room, sub, types) = x
        paras()

def paras():
    semvxx = semv.get()
    dayvxx = dayv.get()
    Label(frame02, text=semvxx, fg='white', bg='#353839', font=("Lucida", 21)).place(x=750, y=27)
    Label(frame02, text=dayvxx, fg='yellow', bg='#353839', font=("Lucida", 21),wraplength = '1').place(x=530, y=255)
    Label(frame02, text=secc1, fg='yellow', bg='#353839', font=("Lucida", 16)).place(x=675, y=83)
    Label(frame02, text=secc2, fg='yellow', bg='#353839', font=("Lucida", 16)).place(x=746, y=83)

    if types == 'P' and sec == ('L' or 'A' or 'G' or 'E' or 'C' or 'J'):
        if lec == '1':
            Label(frame02, text=types+" "+sub,  fg='white', bg='#353839', font=("Lucida", 10)).place(x=666, y=130)
            Label(frame02, text=teach,fg='white', bg='#353839', font=("Lucida", 10)).place(x=670, y=158)

        if lec == '2':
            Label(frame02, text=types+" "+sub , fg='white', bg='#353839', font=("Lucida", 10)).place(x=666, y=185)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=670, y=213)

        if lec == '3':
            Label(frame02, text=types+" "+sub , fg='white', bg='#353839', font=("Lucida", 10)).place(x=666, y=242)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=670, y=270)

        if lec == '4':
            Label(frame02, text=types+" "+sub,  fg='white', bg='#353839', font=("Lucida", 10)).place(x=666, y=298)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=670, y=328)
        if lec == '5':
            Label(frame02, text="BREAK", fg='white', bg='#353839', font=("Lucida", 14)).place(x=684, y=367)

        if lec == '6':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=666, y=411)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=670, y=441)
        if lec == '7':
            Label(frame02, text=types+" "+sub , fg='white', bg='#353839', font=("Lucida", 10)).place(x=666, y=467)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=670, y=496)

        if lec == '8':
            Label(frame02, text=types+" "+sub , fg='white', bg='#353839', font=("Lucida", 10)).place(x=666, y=523)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=670, y=551)


    if types == 'P' and sec == ('M' or 'B' or 'H' or 'F' or 'D' or 'K'):
        if lec == '1':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=740, y=130)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=744, y=158)

        if lec == '2':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=740, y=185)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=744, y=213)

        if lec == '3':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=740, y=242)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=744, y=270)

        if lec == '4':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=740, y=298)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=744, y=328)
        if lec == '5':
            Label(frame02, text="BREAK", fg='white', bg='#353839', font=("Lucida", 14)).place(x=684, y=367)

        if lec == '6':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=740, y=411)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=744, y=441)
        if lec == '7':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=740, y=467)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=744, y=496)

        if lec == '8':
            Label(frame02, text=types+" "+sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=740, y=523)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=744, y=551)

    if types == 'T':
        if lec == '1':
            Label(frame02, text=sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=710, y=135)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=660, y=160)
            Label(frame02, text=room, fg='white', bg='#353839', font=("Lucida", 10)).place(x=758, y=160)
        if lec == '2':
            Label(frame02, text=sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=710, y=185)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=660, y=210)
            Label(frame02, text=room, fg='white', bg='#353839', font=("Lucida", 10)).place(x=758, y=210)
        if lec == '3':
            Label(frame02, text=sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=710, y=241)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=660, y=266)
            Label(frame02, text=room, fg='white', bg='#353839', font=("Lucida", 10)).place(x=758, y=266)

        if lec == '4':
            Label(frame02, text=sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=710, y=300)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=660, y=325)
            Label(frame02, text=room, fg='white', bg='#353839', font=("Lucida", 10)).place(x=758, y=325)

        if lec == '5':
            Label(frame02, text="BREAK", fg='white', bg='#353839', font=("Lucida", 14)).place(x=684, y=367)
        if lec == '6':
            Label(frame02, text=sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=710, y=415)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=660, y=440)
            Label(frame02, text=room, fg='white', bg='#353839', font=("Lucida", 10)).place(x=758, y=440)

        if lec == '7':
            Label(frame02, text=sub, fg='white', bg='#353839', font=("Lucida", 10)).place(x=710, y=470)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=660, y=495)
            Label(frame02, text=room, fg='white', bg='#353839', font=("Lucida", 10)).place(x=758, y=495)


        if lec == '8':
            Label(frame02, text=sub,  fg='white', bg='#353839', font=("Lucida", 10)).place(x=710, y=525)
            Label(frame02, text=teach, fg='white', bg='#353839', font=("Lucida", 10)).place(x=660, y=550)
            Label(frame02, text=room, fg='white', bg='#353839', font=("Lucida", 10)).place(x=758, y=550)



mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "timetable"
)
mycursor = mydb.cursor()
mycursor2 = mydb.cursor()
root = Tk()
root.geometry("1260x650")
root.resizable(0,0)
root.title('Timetable Generation System')
style = ttk.Style(root)
style.theme_use('clam')
# lst = ["Automobile","Computer","Civil","Mechanical","ECE","Electronics"]
# lst1 = ["monday","tuesday","wednesday","thursday","friday"]
# lect = StringVar()
# dept = StringVar()
# teach = StringVar()
# sem = StringVar()
# sec = StringVar()
# room = StringVar()
# sub = StringVar()
# day = StringVar()
# Label(root,text = "Lect. No.").pack()
# Entry(root, textvariable = lect).pack()
# Label(root,text = "Department.").pack()
# ttk.Combobox(root, values = lst, textvariable = dept).pack()
# Label(root,text = "Teacher").pack()
# Entry(root, textvariable = teach).pack()
# Label(root,text = "Sem").pack()
# Entry(root, textvariable = sem).pack()
# Label(root,text = "Section").pack()
# Entry(root, textvariable = sec).pack()
# Label(root,text = "Room").pack()
# Entry(root, textvariable = room).pack()
# Label(root,text = "Subject").pack()
# Entry(root, textvariable = sub).pack()
# Label(root,text = "Day").pack()
# ttk.Combobox(root,values = lst1, textvariable = day).pack()
# Button(root,text = "Submit", command = insert).pack()
style.configure("Treeview", background='#555555', fieldbackground='#555555', foreground='white')
img = Image.open("main2.jpg")
img= img.resize((1366, 700), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
label300 = Label(root, image=img)
label300.place(x=0, y=0)
Entry(root, font = ("Courier", 20), width = 15).place(x =700, y = 200)
Entry(root, font = ("Courier", 20), width = 15).place(x = 700, y = 250)
pk = ["pk","op"]
print(pk)
photo4 = Image.open("loginxx.jpg")
photo4 = photo4.resize((200, 48), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(photo4)
butt4 = Button(root,text = "Login", command = main, image = photo4)
butt4.image = photo4
butt4.place(x=720, y=300)
Label(root, text = "Timetable Generation System, GNDP College", font=("DejaVu Sans Mono", 30),bg = '#353839',fg = 'white').place(x = 135, y = 20)
root.mainloop()

