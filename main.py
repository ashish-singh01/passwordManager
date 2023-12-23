import tkinter
from functools import partial
import saving
import encryption
import sys, os 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

resource_path('icon.ico')
red=(255,0,0)
grey=(125,125,125)


loginPage = tkinter.Tk()
entryPage = tkinter.Tk()
savePage = tkinter.Tk()
loginPage.withdraw()

def doThings(username, password):
    USERNAME = username.get()
    PASSWORD = password.get()
    
    uname = encryption.encrypt(USERNAME)
    word = encryption.encrypt(PASSWORD)

    saving.writing(uname,word)

    u = 20
    p = 20
    c = 0
    while True:
        xuname = saving.showing(c)
        UNAME = encryption.decrypt(xuname)
        tkinter.Label(entryPage, text=UNAME,
                      bg = 'black',
                      fg = 'white', height = 1).place(x=10, y=170+u)
        u+=20
        c+=1

        xpword = saving.showing(c)
        PASS = encryption.decrypt(xpword)
        tkinter.Label(entryPage, text=PASS,
                      bg = 'black',
                      fg = 'white',height = 1).place(x=150, y=170+p)
        p+=20
        c+=1
        print ('u = ')
        print (u)
        print ('p = ' )
        print(p)
        if xuname == '':
            break
    
    
    

    

def read(loginPass):
    login = loginPass.get()
    f = open("login.txt", "r")
    f1 = f.readlines()
    print(f1)
    for x in f1:
        if x==login:
            print(x)
            entrypage()
            f.close()
        else:
            tkinter.Label(loginPage, text = 'WRONG PASSWORD', height = 1).place(x=100, y=20)

def loginpage():

    #loginPage.update()
    loginPage.deiconify()
    entryPage.withdraw()
    savePage.withdraw()
    
    loginPage.geometry('400x150')
    
    loginPage.title('PASSWORD MANAGER')
    loginPage.configure(bg='black')
    
    tkinter.Label(loginPage, text='PASSWORD', 
                      bg = 'black',
                      fg = 'white', height = 1).place(x=10, y=33)
    loginPass = tkinter.Entry(loginPage, width = 50,
                              bd = 5, bg = 'white')
    loginPass.place(x = 80, y = 30 )

    

    r = partial(read, loginPass)
    
    loginButton = tkinter.Button(loginPage, text='LOGIN', bg='#808080',
                                 command = r,
                                 activeforeground='red',
                                 height=1, width=5).place(x=220, y=100)

    setPass = tkinter.Button(loginPage, text='SET PASSWORD', bg='#808080',
                             command=savingpage,
                             activeforeground='red',
                             height=1, width=15).place(x=80, y=100)

    
    
     
def entrypage():

    loginPage.withdraw()
    #entryPage.upadate()
    entryPage.deiconify()
    
    entryPage.geometry('400x350')
    entryPage.title('PASSWORD MANAGER')
    entryPage.configure(bg='black')
    
    tkinter.Label(entryPage, text='USERNAME', 
                      bg = 'black',
                      fg = 'white', height = 1).place(x=10, y=43)
    username = tkinter.Entry(entryPage, width = 50,
                              bd = 5, bg = 'white')
    username.place(x = 80, y = 40 )
    
    tkinter.Label(entryPage, text='PASSWORD', 
                      bg = 'black',
                      fg = 'white', height = 1).place(x=10, y=83)
    password = tkinter.Entry(entryPage, width = 50,
                              bd = 5, bg = 'white')
    password.place(x = 80, y = 80 )

    s = partial(doThings, username, password)
    saveButton = tkinter.Button(entryPage, text='SAVE', bg='#808080',
                                 activeforeground='red',
                                 command=s,
                                 height=1, width=5).place(x=150, y=130)

        
    tkinter.Label(entryPage, text='USERNAME',
                      bg = 'black',
                      fg = 'white', height = 1).place(x=10, y=170)
    
    tkinter.Label(entryPage, text='PASSWORD', 
                      bg = 'black',
                      fg = 'white', height = 1).place(x=150, y=170)


    u = 20
    p = 20
    c = 0
    while True:
        uname = saving.showing(c)
        UNAME = encryption.decrypt(uname)
        tkinter.Label(entryPage, text=UNAME,
                      bg = 'black',
                      fg = 'white', height = 1).place(x=10, y=170+u)
        u+=20
        c+=1

        pword = saving.showing(c)
        PASS = encryption.decrypt(pword)
        tkinter.Label(entryPage, text=PASS,
                      bg = 'black',
                      fg = 'white',height = 1).place(x=150, y=170+p)
        p+=20
        c+=1
        
        if uname == '':
            break

def savingpage():

    loginPage.withdraw()
    savePage.update()
    savePage.deiconify()

    savePage.geometry('400x150')
    savePage.title('PASWORD MANAGER')
    savePage.configure(bg='black')

    
    

    def save():
        f = open('login.txt', "w")
        p = newPass.get()
        print(p)
        f.write(p)
        loginpage()
        f.close()

    
    tkinter.Label(savePage, text='ENTER NEW PASSWORD', height=1).place(x=120, y=10)
    newPass = tkinter.Entry(savePage, width = 50,
                            bd = 5, bg = 'white')
    newPass.place(x=30, y=50)

    saveButton = tkinter.Button(savePage, text='SAVE', bg='#808080',
                                 activeforeground='red',
                                command=save, 
                                 height=1, width=5).place(x=160, y=100)

    
    

loginpage()
#entrypage()

    



