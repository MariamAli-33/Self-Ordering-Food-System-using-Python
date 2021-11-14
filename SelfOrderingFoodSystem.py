from tkinter import *
import os
#import pyautogui

data_file = 'projectbazam.txt'
x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0
x7 = 0

x9 = 0
x10 = 0
x11 = 0
x12 = 0
x13 = 0
x14 = 0
#defining signup func
def Signup():
    global password
    global name
    global image5
    global window
    window = Tk()
    window.title('SIGNUP') 
    window.geometry('1500x800')
    #window.iconbitmap(r'D://icon.ico')
    window.configure(background="brown")
    #image5=PhotoImage(file="D:\\food-animated-gif-18.gif")
    #global pic5
    #pic5 = Label(window, image=image5)
    #pic5.place(x=0, y=0)
    
    instructions = Label(window,font=("Comic Sans MS",33),width=30, text='Please Enter new Credidentials\n',bg="OrangeRed4",fg='yellow')
    instructions.pack()
    new_name = Label(window,font=("Comic Sans MS",33),width=30, text='New Username(without spaces):',bg="OrangeRed4",fg='yellow')
    new_name.pack()
    name = Entry(window,font=("Comic Sans MS",33),width=30,bg="OrangeRed4",fg='yellow' )
    name.pack()
    new_password = Label(window,font=("Comic Sans MS",33),width=30, text='New Password: ',bg="OrangeRed4",fg='yellow')
    new_password.pack()
    password = Entry(window,width=30 ,font=("Comic Sans MS",33)  ,bg="OrangeRed4",fg='yellow',show='*')
    password.pack()
    save_button = Button(window,text="SAVE", font=("Comic Sans MS",33),width=30,bg="OrangeRed4",fg='yellow'  ,command=doc_write)
    save_button.pack()
    
    window.mainloop()
    login_window.destroy()
#save function (writing name and password in a file)   
def doc_write():
    with open(data_file, 'a') as f:
        f.write(name.get())
        f.write(password.get())
        f.write("\n")
        
        f.close()
    window.destroy()
    Login()

#defining login function
def Login():
    global old_name
    global old_password
    global login_window
    global image1
    login_window = Tk()
    login_window.title('Login')
    #image9=PhotoImage(file="D:\\image.gif")
    #global pic9
    #pic9=Label(login_window,image=image9)
    #pic9.place(x=0,y=0)
    login_window.geometry('1500x800')
    #login_window.iconbitmap(r'D://icon.ico')
    login_window.configure(background="OrangeRed4")
    instruction = Label(login_window,font=("Comic Sans MS",33),width=45,bg="OrangeRed4",fg='yellow'  ,text='Please Login\n')
    instruction.pack()
    label_name = Label(login_window,font=("Comic Sans MS",33),width=30, bg="OrangeRed4",fg='yellow'  ,text='Username: ')
    label_name.pack()
    old_name = Entry(login_window, font=("Comic Sans MS",33),  width=30,bg="OrangeRed4",fg='yellow' )
    old_name.pack()
    label_password = Label(login_window,font=("Comic Sans MS",33),width=30,bg="OrangeRed4",fg='yellow'  ,text='Password: ')
    label_password.pack()
    old_password = Entry(login_window,width=30,  font=("Comic Sans MS",33),  bg="OrangeRed4",fg='yellow', show='*')
    old_password.pack()
    loginB = Button(login_window,font=("Comic Sans MS",33),width=30,text='LOGIN', bg="OrangeRed4",fg='yellow' ,command=CheckLogin)
    loginB.pack()
    signup_2 = Button(login_window,font=("Comic Sans MS",33),width=30,  text='SIGN UP', fg='red', command=Signup)
    signup_2.pack()
    login_window.mainloop()
#check fun
def CheckLogin():
    global found
    with open(data_file) as f:
        data = f.read()
        if old_name.get() in data and old_password.get() in data:
            found = True
        else:
            found = False

    if found == True:
      win2()
      
      

    else:
        global login_window
        login_window.destroy
        welcome = Tk()
        welcome.title('invalid')
        welcome.configure(background="OrangeRed4")
        #global image6
        #image6 = PhotoImage(file="D:\\food1.gif")
        #global pic6
        #pic6 = Label(window, image=image6)
        #pic6.place(x=0, y=0)
        welcome.geometry('1366x768')
        #window.iconbitmap(r'icon.ico')
        welcome.configure(background="OrangeRed4")
        welcome_label = Label(welcome, text=(' INVALID LOGIN HAI \n {} jee \n DOBARA TRY KREN PL'.format(old_name.get())),font=("Comic Sans MS",56),width=56, bg="OrangeRed4",fg='yellow'  )
        welcome_label.pack()
        log=Button(welcome, text=' LOGIN',font=("Comic Sans MS",56),width=56, bg="OrangeRed4",fg='yellow',command=Login)
        log.pack()
        welcome.mainloop()
        
    
        

    
#welcome window    
def win2():
        global window2
        window2=Tk()
        window2.title("KHANA SHANA ")
        window2.configure(background="OrangeRed4")
        global image1
        #image1 = PhotoImage(file="D:\\food.gif")
        #global pic1
        #pic1 = Label(window, image=image1)
        #pic1.place(x=0, y=0)
        window2.geometry('1366x768')
        #window.iconbitmap(r'icon.ico')
        window2.configure(background="OrangeRed4")
       

        heading = Label(window2, text="KHANA SHANA\n", bg="OrangeRed4")
        heading.config(font=("Ariel", 36, "bold", "underline"),fg='yellow')
        heading.pack()

        label1 = Label(window2, text=(" arayyy aap {}  \n WELCOME JEEE!!!!!\n Kia khaogay".format(old_name.get())), bg="OrangeRed4",fg='yellow')
        label1.config(font=("Comic Sans MS", 56))
        label1.pack()
        button_khana=Button(window2,text="mains",font=("Comic Sans MS",40),width=45,bg="OrangeRed4",fg='yellow',command=khana)
        button_khana.pack()

        button_desserts=Button(window2,text="desserts",font=("Comic Sans MS",40),width=45,bg="OrangeRed4",fg='yellow',command=desserts)
        button_desserts.pack()
#menu funct
#khana function
def khana():
        global windowx
        windowx = Tk()
        windowx.title("KHANA SHANA")
        windowx.configure(background="OrangeRed4")
        #global image2
        #image2 = PhotoImage(file="D:\\basil-delicious-food-459469.jpg")
        #global pic2
        #pic2 = Label(window, image=image2)
        #pic2.place(x=0, y=0)
        windowx.geometry('1366x768')
        #window.iconbitmap(r'icon.ico')
        windowx.configure(background="OrangeRed4")
       

        heading = Label(windowx, text="KHANA KHAALO JEE\n", bg="OrangeRed4")
        heading.config(font=("Ariel", 36, "bold", "underline"),fg='yellow')
        heading.pack()

        label1 = Label(windowx, text="Come ON order JEE!\n SADA MOOD WADA CHANGA SEE\n", bg="OrangeRed4",fg='yellow')
        label1.config(font=("Comic Sans MS", 26))
        label1.pack()

    # MAIN FRAME
        main = Frame(windowx, width=900, height=650, bd=0, relief='raise')
        main.configure(bg="OrangeRed4")
        main.pack()

    # UPPER AND LOWER SUB FRAMES
        upper = Frame(main, width=900, height=330, bd=1, relief='raise')
        upper.configure(bg="OrangeRed4")
        upper.pack(side=TOP)
        lower = Frame(main, width=1366, height=320, bd=1, relief='raise')
        lower.configure(bg="OrangeRed4")
        lower.pack(side=BOTTOM)

    # LEFT AND RIGHT SUB-SUB FRAMES
        left = Frame(upper, width=700, height=430, bd=0, relief='raise')
        left.configure(bg="OrangeRed4")
        left.pack(side=LEFT)
        rightend = Frame(upper, width=100, height=430, bd=0, relief='raise')
        rightend.pack(side=RIGHT)
        right = Frame(upper, width=200, height=430, bd=0, relief='raise')
        right.configure(bg="OrangeRed4")
        right.pack(side=RIGHT)

    # MENU LIST FRAMES IN LEFT SUB-SUB FRAME
        item1 = Frame(left, width=700, height=40, bd=0)
        item1.configure(bg="OrangeRed4")
        item1.pack(side=TOP)
        item2 = Frame(left, width=700, height=40, bd=0)
        item2.configure(bg="OrangeRed4")
        item2.pack(side=TOP)
        item3 = Frame(left, width=700, height=40, bd=0)
        item3.configure(bg="OrangeRed4")
        item3.pack(side=TOP)
        item4 = Frame(left, width=700, height=40, bd=0)
        item4.configure(bg="OrangeRed4")
        item4.pack(side=TOP)
        item5 = Frame(left, width=700, height=40, bd=0)
        item5.configure(bg="OrangeRed4")
        item5.pack(side=TOP)
        item6 = Frame(left, width=700, height=40, bd=0)
        item6.configure(bg="OrangeRed4")
        item6.pack(side=TOP)
        item7 = Frame(left, width=700, height=40, bd=0)
        item7.configure(bg="OrangeRed4")
        item7.pack(side=TOP)

    # MENU LIST LABELS IN LEFT SUB-SUB FRAME
        item_1 = Label(item1, text="Rice and Spice                      |  Rs. 499         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_1.pack()
        item_2 = Label(item2, text=" Pizza Pocket                         |  Rs. 250          ", font=("Comic Sans MS", 20), bg="OrangeRed4",fg='yellow')
        item_2.pack()
        item_3 = Label(item3, text="Value Roll                             |  Rs. 300         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_3.pack()
        item_4 = Label(item4, text="Chicken and Rice                  |  Rs. 450         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_4.pack()
        item_5 = Label(item5, text="Chocolicious Brownie            |  Rs. 799         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_5.pack()
        item_6 = Label(item6, text="Hershey's cookie                 |  Rs. 495         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_6.pack()
        item_7 = Label(item7, text="Hot n Sour Soup                  |  Rs. 375         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_7.pack()

    # SPINBUTTONS IN RIGHT SUB-SUB FRAME
        spin1 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin1.pack(side=TOP)
        spin2 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin2.pack(side=TOP)
        spin3 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin3.pack(side=TOP)
        spin4 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin4.pack(side=TOP)
        spin5 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin5.pack(side=TOP)
        spin6 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin6.pack(side=TOP)
        spin7 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin7.pack(side=TOP)

    # SPINBUTTONS CONFIGURATION
    # 1. Defining function for button command
        def no_of_items():
          global x1
          global x2
          global x3
          global x4
          global x5
          global x6
          global x7
          x1 = int(spin1.get())
          x2 = int(spin2.get())
          x3 = int(spin3.get())
          x4 = int(spin4.get())
          x5 = int(spin5.get())
          x6 = int(spin6.get())
          x7 = int(spin7.get())

    # 2. Creating button widgets
        button1 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items)
        button1.config(bg="yellow")
        button1.pack()
        button2 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items)
        button2.config(bg="yellow")
        button2.pack()
        button3 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items)
        button3.config(bg="yellow")
        button3.pack()
        button4 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items)
        button4.config(bg="yellow")
        button4.pack()
        button5 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items)
        button5.config(bg="yellow")
        button5.pack()
        button6 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items)
        button6.config(bg="yellow")
        button6.pack()
        button7 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items)
        button7.config(bg="yellow")
        button7.pack()
        returnbutton=Button(lower,text="desserts", font=("Comic Sans MS", 13), width=12, command=desserts)
        returnbutton.config(bg="yellow")
        returnbutton.pack()
        mainbutton = Button(lower, text="Checkout", font=("Comic Sans MS", 13), width=12, command=checkout)
        mainbutton.config(bg="yellow")
        mainbutton.pack()

        windowx.mainloop()  
             

def desserts():
        global window_desserts
        
        
        window_desserts = Tk()
        window_desserts.title("KHANA SHANA")
        window_desserts.configure(background="OrangeRed4")
        window_desserts.geometry('1366x768')
        #window.iconbitmap(r'icon.ico')
        window_desserts.configure(background="OrangeRed4")
       

        heading = Label(window_desserts, text="Kuch meetha Hojaye\n", bg="OrangeRed4")
        heading.config(font=("Ariel", 36, "bold", "underline"),fg='yellow')
        heading.pack()

        label1 = Label(window_desserts, text="DESSERTS\n", bg="OrangeRed4",fg='yellow')
        label1.config(font=("Comic Sans MS", 26))
        label1.pack()

    # MAIN FRAME
        main = Frame(window_desserts, width=900, height=650, bd=0, relief='raise')
        main.configure(bg="OrangeRed4")
        main.pack()

    # UPPER AND LOWER SUB FRAMES
        upper = Frame(main, width=900, height=330, bd=1, relief='raise')
        upper.configure(bg="OrangeRed4")
        upper.pack(side=TOP)
        lower = Frame(main, width=1366, height=320, bd=1, relief='raise')
        lower.configure(bg="OrangeRed4")
        lower.pack(side=BOTTOM)

    # LEFT AND RIGHT SUB-SUB FRAMES
        left = Frame(upper, width=700, height=430, bd=0, relief='raise')
        left.configure(bg="OrangeRed4")
        left.pack(side=LEFT)
        rightend = Frame(upper, width=100, height=430, bd=0, relief='raise')
        rightend.pack(side=RIGHT)
        right = Frame(upper, width=200, height=430, bd=0, relief='raise')
        right.configure(bg="OrangeRed4")
        right.pack(side=RIGHT)

    # MENU LIST FRAMES IN LEFT SUB-SUB FRAME
        
        item9 = Frame(left, width=700, height=40, bd=0)
        item9.configure(bg="OrangeRed4")
        item9.pack(side=TOP)
        item10 = Frame(left, width=700, height=40, bd=0)
        item10.configure(bg="OrangeRed4")
        item10.pack(side=TOP)
        item11 = Frame(left, width=700, height=40, bd=0)
        item11.configure(bg="OrangeRed4")
        item11.pack(side=TOP)
        item12 = Frame(left, width=700, height=40, bd=0)
        item12.configure(bg="OrangeRed4")
        item12.pack(side=TOP)
        item13 = Frame(left, width=700, height=40, bd=0)
        item13.configure(bg="OrangeRed4")
        item13.pack(side=TOP)
        item14 = Frame(left, width=700, height=40, bd=0)
        item14.configure(bg="OrangeRed4")
        item14.pack(side=TOP)

    # MENU LIST LABELS IN LEFT SUB-SUB FRAME
        
        item_9 = Label(item9, text="Berry Cake                       |  Rs. 250          ", font=("Comic Sans MS", 20), bg="OrangeRed4",fg='yellow')
        item_9.pack()
        item_10 = Label(item10, text="Choco Fudge                    |  Rs. 300         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_10.pack()
        item_11= Label(item11, text="Tiramisu Cake                     |  Rs. 450         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_11.pack()
        item_12 = Label(item12, text="Chocolicious Brownie            |  Rs. 799         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_12.pack()
        item_13 = Label(item13, text="Hershey's cookie                |  Rs. 495         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_13.pack() 
        item_14 = Label(item14, text="KitKat Cake                      |  Rs. 375         ", font=("Comic Sans MS", 20),bg="OrangeRed4",fg='yellow')
        item_14.pack()

    # SPINBUTTONS IN RIGHT SUB-SUB FRAME
        
        spin9 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin9.pack(side=TOP)
        spin10 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin10.pack(side=TOP)
        spin11 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin11.pack(side=TOP)
        spin12 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin12.pack(side=TOP)
        spin13 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin13.pack(side=TOP)
        spin14 = Spinbox(right, from_=0, to=10, width=5, font=("Comic Sans MS", 20))
        spin14.pack(side=TOP)

    # SPINBUTTONS CONFIGURATION
    # 1. Defining function for button command
        def no_of_items2():
         
          global x9
          global x10
          global x11
          global x12
          global x13
          global x14
         
          x9 = int(spin9.get())
          x10 = int(spin10.get())
          x11 = int(spin11.get())
          x12 = int(spin12.get())
          x13 = int(spin13.get())
          x14 = int(spin14.get())


    # 2. Creating button widgets
       
        button9 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items2)
        button9.config(bg="yellow")
        button9.pack()
        button10 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items2)
        button10.config(bg="yellow")
        button10.pack()
        button11= Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items2)
        button11.config(bg="yellow")
        button11.pack()
        button12 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items2)
        button12.config(bg="yellow")
        button12.pack()
        button13 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items2)
        button13.config(bg="yellow")
        button13.pack()
        button14 = Button(rightend, text="Add", font=("Comic Sans MS", 13), width=12, command=no_of_items2)
        button14.config(bg="yellow")
        button14.pack()

        returnbutton=Button(lower,text="main", font=("Comic Sans MS", 13), width=12, command=khana)
        returnbutton.config(bg="yellow")
        returnbutton.pack() 
        mainbutton1 = Button(lower, text="Checkout", font=("Comic Sans MS", 13), width=12, command=checkout)
        mainbutton1.config(bg="yellow")
        mainbutton1.pack()

    

#PRICE SPECIFICATION
item1_price = 499
item2_price = 250
item3_price = 300
item4_price = 450
item5_price = 799
item6_price = 495
item7_price = 375

item9_price = 250
item10_price = 300
item11_price = 450
item12_price = 799
item13_price = 495
item14_price = 375
#CHECKOUT
def checkout():
          global root
          root=Tk()
          root.geometry('1366x768')
          root.configure(bg="OrangeRed4")
          #global image3
     
          #image3=PhotoImage(file="C:/Users/littl/Downloads/Fruitcones.jpeg")
          #global label_1
          #label_1=Label(root,image=image3)
          #label_1.pack()
          message=Label(root,text="Thankyou for orderinG JEE.\n APKA ORDER PLACE HOGAYA.\n",bg="OrangeRed4")
          message.config(font=("Ariel",24,"bold"),fg='yellow')
          message.grid(row=0,column=1)
          message1=Label(root,text="ORDER DETAILS \n",bg="OrangeRed4")
          message1.config(font=("Ariel",20,'underline',"bold"),fg="yellow")
          message1.grid(row=1,column=1)
          receipt_=Label(root,text="  Item\t\t\t\tPrice\t\tQuantity\t\t\tTotal")
          receipt_.config(font=("Ariel",20,"bold"),fg='yellow',bg='black')
          receipt_.grid(row=2,column=1)
          if x1!=0:
                 x_1=Label(root,text=("Rice and Spice\t\t\t 499\t\t\t{}\t\t\t{}".format(x1,x1*item1_price)),bg="OrangeRed4")
                 x_1.config(font=("Ariel",18,"bold"),fg='yellow')
                 x_1.grid(row=3,column=1)
          if x2!=0:
                x_2=Label(root,text=("Pizza Pocket\t\t\t250\t\t\t{}\t\t\t{}".format(x2,x2*item2_price)),bg="OrangeRed4")
                x_2.config(font=("Ariel",18,"bold"),fg='yellow')
                x_2.grid(row=4,column=1)
          if x3!=0:
                x_3=Label(root,text=("Chicken Roll\t\t\t300\t\t\t{}\t\t\t{}".format(x3,x3*item3_price)),bg="OrangeRed4")
                x_3.config(font=("Ariel",18,"bold"),fg='yellow')
                x_3.grid(row=5,column=1)
          if x4!=0:
                x_4=Label(root,text=("Chicken n Rice\t\t\t450\t\t\t{}\t\t\t{}".format(x4,x4*item4_price)),bg="OrangeRed4")
                x_4.config(font=("Ariel",18,"bold"),fg='yellow')
                x_4.grid(row=6,column=1)
          if x5!=0:
                x_5=Label(root,text=("Choco Brownie\t\t\t799\t\t\t{}\t\t\t{}".format(x5,x5*item5_price)),bg="OrangeRed4")
                x_5.config(font=("Ariel",18,"bold"),fg='yellow')
                x_5.grid(row=7,column=1)
          if x6!=0:
                x_6=Label(root,text=("Hershey's Cookie\t\t\t495\t\t\t{}\t\t\t{}".format(x6,x6*item6_price)),bg="OrangeRed4")
                x_6.config(font=("Ariel",18,"bold"),fg='yellow')
                x_6.grid(row=8,column=1)
          if x7!=0:
                x_7=Label(root,text=("Hot n Sour Soup\t\t\t375\t\t\t{}\t\t\t{}".format(x7,x7*item7_price)),bg="OrangeRed4")
                x_7.config(font=("Ariel",18,"bold"),fg='yellow')
                x_7.grid(row=9,column=1)
          if x9!=0:
                x_9=Label(root,text=("Berry Cake\t\t\t250\t\t\t{}\t\t\t{}".format(x9,x9*item9_price)),bg="OrangeRed4")
                x_9.config(font=("Ariel",18,"bold"),fg='yellow')
                x_9.grid(row=11,column=1)
          if x10!=0:
                x_10=Label(root,text=("Choco fudge\t\t\t300\t\t\t{}\t\t\t{}".format(x10,x10*item10_price)),bg="OrangeRed4")
                x_10.config(font=("Ariel",18,"bold"),fg='yellow')
                x_10.grid(row=12,column=1)
          if x11!=0:
                x_11=Label(root,text=("Tiramisu Cake\t\t\t450\t\t\t{}\t\t\t{}".format(x11,x11*item11_price)),bg="OrangeRed4")
                x_11.config(font=("Ariel",18,"bold"),fg='yellow')
                x_11.grid(row=13,column=1)
          if x12!=0:
                x_12=Label(root,text=("Choco Brownie\t\t\t799\t\t\t{}\t\t\t{}".format(x12,x12*item12_price)),bg="OrangeRed4")
                x_12.config(font=("Ariel",18,"bold"),fg='yellow')
                x_12.grid(row=14,column=1)
          if x13!=0:
                x_13=Label(root,text=("hershey's cookie\t\t\t495\t\t\t{}\t\t\t{}".format(x13,x13*item13_price)),bg="OrangeRed4")
                x_13.config(font=("Ariel",18,"bold"),fg='yellow')
                x_13.grid(row=15,column=1)
          if x14!=0:
                x_14=Label(root,text=("kitkat cake\t\t\t375\t\t\t{}\t\t\t{}\n".format(x14,x14*item14_price)),bg="OrangeRed4")
                x_14.config(font=("Ariel",18,"bold"),fg='yellow')
                x_14.grid(row=16,column=1)                      
          Total_bill = (item1_price*x1)+(item2_price*x2)+(item3_price*x3)+(item4_price*x4)+(item5_price*x5)+(item6_price*x6)+(item7_price*x7)+(item9_price*x9)+(item10_price*x10)+(item11_price*x11)+(item12_price*x12)+(item13_price*x13)+(item14_price*x14)
          output=Label(root,text=("\n\n\nYour total bill is Rs.{}.\n".format(Total_bill)))
          output.config(font=("Ariel",20,"bold"),bg="OrangeRed4",fg='yellow')
          output.grid(row=17,column=1)
          #last window
          def exit_func1():
                global old_name
                name=old_name.get()
                
                #takepic=pyautogui.screenshot()
                #takepic.save("C:/Users/littl/Desktop/orders/{} order.png".format(name))
                #win3()
          exitbutton=Button(root,text="next",command=exit_func1)
          exitbutton.config(font=('Ariel',10,"bold"),width=10,bg="yellow",fg="black")
          exitbutton.grid(row=18,column=2)

          root.mainloop()          

#bye window    
def win3():
        global window3
        window3=Tk()
        window3.title("BYE JEE ")
        window3.configure(background="OrangeRed4")
        #global image8
        #image8 = PhotoImage(file="D:\\basil-delicious-food-459469.jpg")
        #global pic1
        #pic8 = Label(window, image=image8)
        #pic8.place(x=0, y=0)
        window3.geometry('1366x768')
        #window.iconbitmap(r'icon.ico')
        window3.configure(background="OrangeRed4")
        heading = Label(window3, text="BYE BYE JEE\n", bg="OrangeRed4")
        heading.config(font=("Ariel", 72, "bold", "underline"),fg='yellow')
        heading.pack()

        label1 = Label(window3, text="JALDEE ANA!!!!!\n", bg="OrangeRed4",fg='yellow')
        label1.config(font=("Comic Sans MS", 56))
        label1.pack()
        button_k=Button(window3,text=" Allah Hafiz",font=("Comic Sans MS",13),width=30,bg="OrangeRed4",fg='yellow',command=exit_func)
        button_k.pack()

def exitwindow():
             window_desserts.destroy()
def exitwindow1():
             windowx.destroy()
def welcome_123():
             welcome.destroy()
                    
def exit_func():
          global root
          global window2
          global window3
          global login_window
          global window_desserts
        
          
          root.destroy()
        
          window2.destroy()
          window3.destroy()
          login_window.destroy()
          window_desserts.destroy()
          
          Login()
          

def DelUser():
    os.remove(data_file)
    login_window.destroy()
    Signup()


if os.path.isfile(data_file):
    Login()
else:
    Signup()




    
