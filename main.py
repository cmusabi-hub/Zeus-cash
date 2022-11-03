from cgitb import text
from tkinter import ttk, Tk, PhotoImage, RIDGE, GROOVE


class FrontEnd:
    def __init__(self, master):
        self.master = master
        self.login()

    def login(self):
        self.master.geometry('640x360+300+100')
        self.master.title('ZEUS BANK')
        self.frame_header = ttk.Frame(self.master)
        self.logo = PhotoImage(file='zeus_logo.png').subsample(5, 5)

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
        ttk.Button(self.frame_body, text="Submit", command=temp_action ).grid(
            row=2, column=0, padx=10, pady=10, columnspan=2)
        ttk.Button(self.frame_body, text="Create account", command=self.create).grid(
        row=2, padx=10, pady=10, column=2, stick='se')
        ttk.Button(self.frame_body, text=" Password?", command=self.forget).grid(
        row=3, column=1, columnspan=2, padx=10, pady=10)
    def home(self):
        self.frame_body.forget()
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=GROOVE)
        self.homebut = ttk.Button(
            self.frame_menu, text="Home", command=self.forget)
        self.homebut.grid(row=0, column=0)
        self.probut = ttk.Button(
            self.frame_menu, text="Profile", command=self.forget)
        self.probut.grid(row=0, column=1)
        self.buddbut = ttk.Button(
            self.frame_menu, text="Buddies", command=self.forget)
        self.buddbut.grid(row=0, column=2)
        self.sendbut = ttk.Button(
            self.frame_menu, text="Send amount", command=self.forget)
        self.sendbut.grid(row=0, column=3)
        self.seabut = ttk.Button(
            self.frame_menu, text="Search", command=self.forget)
        self.seabut.grid(row=0, column=4)

        self.frame_body = ttk.Frame(self.master)
        self.frame_body.pack()
        self.frame_body.config(relief=GROOVE, padding=(31, 16))

        ttk.Button(self.frame_body, text="Check Account Balance",
                   command=self.forget).grid(row=1, padx=30, pady=5, column=1)
        ttk.Button(self.frame_body, text="View Recent Transactions",
                   command=self.forget).grid(row=2, padx=30, pady=10, column=1)
        ttk.Button(self.frame_body, text="Check Usage Graph",
                   command=self.forget).grid(row=3, padx=30, pady=10, column=1)
        ttk.Button(self.frame_body, text="Log out", command=self.login).grid(
            row=4, padx=30, pady=10, column=1)
        ttk.Label(self.frame_body, wraplength=300, text="Welcome to postinter bank. This is a simple, fast and elegant way of transferring money to anyone swiftly. Explore for more features.").grid(
            row=0, padx=20, pady=30, column=1)
    def forget(self):
        pass

root = Tk()
FrontEnd(root)
root.mainloop()
