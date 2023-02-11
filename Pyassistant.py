
'''
def A21():


    asd123 = Tk()
    asd123.geometry('500x200')
    asd123.title("Translator")
    Label(asd123, text='Translate From:').pack()
    info = Entry(asd123).insert(END, "").pack()
    Label(asd123, text='Translate To:').pack()
    info1 = Entry(asd123).insert(END, '').pack()
    Label(asd123, text='Translate What:').pack()
    info_Tf = Entry(asd123).insert(END, "").pack()


    def Translate():
        A = info.get()
        B = info1.get()
        C = info_Tf.get()
        translator = Translator(from_lang=A, to_lang=B)
        translation = translator.translate(C)
        Label(ws, text=translation).pack()

    Button(asd123, text="Translate", command=Translate).pack()
    asd123.mainloop()
'''

import Functions
import tkinter
def Initializer():
    def Code_The_Starter(data):
        if "Features" in data:
            Functions.A1()
        if "Say" in data:
            Functions.A2(data)
        if "Calculator" in data:
            from Functions import A3
            A3()
        if 'Take a photo' in data:
            Functions.A6()
        if "Make a new file" in data:
            Functions.A7()
        if "Read a file" in data:
            Functions.A8()
        if data in ('Stop', 'exit', 'bye', "goodbye"):
            Functions.A9()
        if "How are you" in data:
            Functions.A10()
        if "Open my camera" in data:
            Functions.A11()
        if "Month lookup" in data:
            Functions.A12()
        if "Calender" in data:
            Functions.A13()
        if "Open Gmail" in data:
            Functions.A14()
        if "What is the weather" in data:
            Functions.A15()
        if "What time is it" in data:
            Functions.A16()
        if "Where is" in data:
            Functions.A17(data)
        if "Search" in data:
            Functions.A18(data)
        if "Shutdown my computer" in data:
            Functions.A19()
        if "Play snake" in data:
            Functions.A20()
    Functions.A1()
    ws = tkinter.Tk()
    ws.title('Ad_BoT')
    ws.geometry('187x333')

    img = tkinter.PhotoImage(file=r"Aaa.png")
    label = tkinter.Label(
        ws,
        image=img
    )
    label.place(x=0, y=0)

    input = tkinter.Entry(ws)

    def type():
        data1 = input.get()
        Code_The_Starter(data1)

    button = tkinter.Button(text="Enter",
                            bd=10,
                            bg="grey",
                            fg="red",
                            command=type,
                            activeforeground="Orange",
                            activebackground="blue",
                            font="Andalus",
                            height=1,
                            highlightcolor="purple",
                            justify="right",
                            padx=1,
                            pady=1,
                            relief="groove",
                            )
    button1 = tkinter.Button(text="Stop",
                             bd=10,
                             bg="grey",
                             fg="red",
                             command=Functions.A9,
                             activeforeground="Red",
                             activebackground="Black",
                             font="Andalus",
                             height=1,
                             highlightcolor="purple",
                             justify="right",
                             padx=10,
                             pady=10,
                             relief="groove",
                             )
    input.place(x=25, y=166)
    button.place(x=25, y=186)
    button1.place(x=57, y=246)
    ws.mainloop()


Initializer()