from tkinter import *
root = Tk()
root.geometry('550x300')
root.resizable(0,0)
root.title('Geekedu Address Book')
contactList = [
    ['John Doe',  '0176738493'],
    ['Rahul Sharma',  '2684430000'],
    ['Seth Kabrial',   '4338354432'],
    ['Sean Porchevski','6834552341'],
    ['Chris Brown',   '1234852689'],
    ['Amina Armin' , '2119876543'],
    ]
Name = StringVar()
Number = StringVar()
frame = Frame(root)
frame.pack(side = RIGHT)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)
def Selected():
    return int(select.curselection()[0])

def addContact():
    contactList.append([Name.get(), Number.get()])
    selectSet()


def DELETE():
    del contactList[Selected()]
    selectSet()

def VIEW():
    NAME, PHONE = contactList[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

def EXIT():
    root.destroy()

def selectSet() :
    contactList.sort()
    select.delete(0,END)
    for name,phone in contactList :
        select.insert (END, name)
selectSet()
Label(root, text = 'NAME').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 130, y=20)
Label(root, text = 'PHONE #').place(x= 30, y=70)
Entry(root, textvariable = Number).place(x= 130, y=70)
Button(root,text=" ADD", command = addContact).place(x= 50, y=110)
Button(root,text="DELETE",command = DELETE).place(x= 50, y=210)
Button(root,text="VIEW", command = VIEW).place(x= 50, y=160)
Button(root,text="EXIT",bg='red', command = EXIT).place(x= 50, y=260)

root.mainloop()
