from cgitb import text
from tkinter import ttk, Tk, PhotoImage, RIDGE, GROOVE


class Front:
    def __init__(self, master):
        self.master = master
        self.login()

    def login(self):
        self.master.geometry('640x360+300+100')
        self.master.title('Zeus Bank')
        self.frame_header = ttk.Frame(self.master)
        self.logo = PhotoImage(file='zeus_logo.png').subsample(4, 4)

        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()

        ttk.Label(self.frame_header, image=self.logo).grid(
            row=0, column=0, rowspan=3)
        ttk.Label(self.frame_header, text='Welcome to Zeus Banking!').grid(
            row=0, column=1, rowspan=2)

        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief=GROOVE, padding=(31, 16))
        ttk.Label(self.frame_body, text='User Name:').grid(
            row=0, column=1, padx=10, pady=10, sticky='sw')
        ttk.Label(self.frame_body, text='Password:').grid(
            row=1, column=1, padx=10, pady=10, sticky='sw')
        self.user = ttk.Entry(self.frame_body, width=24, font=('Arial', 10))
        self.psd = ttk.Entry(self.frame_body, width=24, font=('Arial', 10))
        self.user.grid(row=0, column=2)
        self.psd.grid(row=1, column=2)
        self.psd.config(show='*')

        def temp_action():
            password

        ttk.Button(self.frame_body, text="Submit", command=temp_action).grid(
            row=2, column=0, padx=10, pady=10, columnspan=2)
        ttk.Button(self.frame_body, text="Create account", command=self.create).grid(
        row=2, padx=10, pady=10, column=2, stick='se')
        ttk.Button(self.frame_body, text="Forgot Password?", command=self.forgot).grid(
        row=3, column=1, columnspan=2, padx=10, pady=10)
    def create(self):
        self.menu_ini()
    def forgot(self):
        pass
    def menu_ini(self):
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=GROOVE)
        self.homebut = ttk.Button(
            self.frame_menu, text="Home", command=self.home)
        self.homebut.grid(row=0, column=0)
        self.probut = ttk.Button(
            self.frame_menu, text="Profile", command=self.profile)
        self.probut.grid(row=0, column=1)
        self.fribut = ttk.Button(
            self.frame_menu, text="Friends", command=self.friends)
        self.fribut.grid(row=0, column=2)
        self.tranbut = ttk.Button(
            self.frame_menu, text="Transfer amount", command=self.transfer)
        self.tranbut.grid(row=0, column=3)
        self.seabut = ttk.Button(
            self.frame_menu, text="Search", command=self.search)
        self.seabut.grid(row=0, column=4)

root = Tk()
Front(root)
root.mainloop()
