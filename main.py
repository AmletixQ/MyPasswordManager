from databaseSettings import registration, autorisation, addAccount
import tkinter
import json

class MyGUI:
    def __init__(self):
        # create and change settings for main window
        self.window = tkinter.Tk()
        self.window.title("Password manager")
        self.window.geometry("500x250")

        # Create Frames

        self.main_frame = tkinter.Frame(self.window)

        self.frame_NameApplication = tkinter.Frame(self.main_frame)
        self.frame_login = tkinter.Frame(self.main_frame)
        self.frame_password = tkinter.Frame(self.main_frame)
        self.frame_button = tkinter.Frame(self.main_frame)

        self.mainLogIn_frame = tkinter.Frame(self.window)

        # create widgets --> :
        # first step create labels

        self.logInButton = tkinter.Button(self.frame_button, text="Авторизоваться", command=self.log_in)

        self.label_login = tkinter.Label(self.frame_login, text="Логин:")
        self.label_password = tkinter.Label(self.frame_password, text="Пароль:")
        self.hey_label = tkinter.Label(self.frame_NameApplication, text="Процесс создания аккаунта:")

        self.button_LogIn = tkinter.Button(self.frame_button, text="Зарегистрироваться", command=self.SignInMethod)

        # second step: create entry
        self.entry_login = tkinter.Entry(self.frame_login)
        self.entry_password = tkinter.Entry(self.frame_password)

        # Pack frames and they choose position:

        self.hey_label.pack()
        self.button_LogIn.pack()
        self.logInButton.pack()

        self.label_login.pack(side="left", padx=7)
        self.label_password.pack(side="left")
        self.entry_login.pack()
        self.entry_password.pack()

        self.frame_NameApplication.pack()
        self.frame_login.pack(pady=(30, 20))
        self.frame_password.pack()
        self.frame_button.pack(pady=(20, 0))

        self.main_frame.pack()

        tkinter.mainloop()

    def SignInMethod(self):
        self.login = self.entry_login.get()
        self.password = self.entry_password.get()

        
        check = registration(self.login, self.password)

        if check[0]:
            self.hey_label.config(text="Поздравляю. Регистрация прошла успешно!")
            self.main_frame.pack_forget()
            self.mainPage()
        else:
            self.hey_label.config(text=check[1])

        return self.login

    def LogInMethod(self):
        self.login = self.entry_login.get()
        self.password = self.entry_password.get()

        check = autorisation(self.login, self.password)
        if check:
            self.hey_label.config(text="Авторизация прошла успешно!")
            self.mainPage()
        else:
            self.hey_label.config(text="Неверен либо логин, либо пароль!")
        
    def NeedMethod(self):

        with open("database/AccountData.json", "r") as jsonFile:
            data = json.load(jsonFile)
        
        if len(data[self.login]) > 1:
            for item in data[self.login]["accounts"]:
                self.ListBox.insert(tkinter.END, f"{item}")
                for values in data[self.login]["accounts"][item]:
                    self.ListBox.insert(tkinter.END, f"    {values}: {data[self.login]['accounts'][item][values]}")
                self.ListBox.insert(tkinter.END, "-"*20+"\n")         

    def mainPage(self):
        self.mainLogIn_frame.pack_forget()
        self.main_frame.pack_forget()

        self.window.geometry("700x400")

        self.mainPage_frame = tkinter.Frame(self.window)
        self.frameLabel = tkinter.Frame(self.mainPage_frame)
        self.frameButton = tkinter.Frame(self.mainPage_frame)

        self.menu = tkinter.Label(self.frameLabel, text=f"Пользователь: {self.login}")
        self.addAnyAccount = tkinter.Button(self.frameButton, 
                                            text="Добавить аккаунт", 
                                            command=self.CreateAccount)

        self.scroll = tkinter.Scrollbar(self.window)
        self.scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)


        self.ListBox = tkinter.Listbox(self.mainPage_frame, width=50, yscrollcommand=self.scroll.set)
        # self.ListBox.insert(tkinter.END, "Hello World!")

        self.NeedMethod()

        self.menu.pack(side="left")
        self.addAnyAccount.pack()

        self.frameLabel.pack(side="top", pady=(0, 20))
        self.frameButton.pack(pady=(0, 20))
        self.mainPage_frame.pack()

        self.ListBox.pack()
        self.scroll.config(command=self.ListBox.yview)

    def CreateAccount(self):
        self.mainPage_frame.pack_forget()

        # Frames
        self.main_frame = tkinter.Frame(self.window)
        
        self.frame_name = tkinter.Frame(self.main_frame)
        self.frame_site = tkinter.Frame(self.main_frame)
        self.frameLogin = tkinter.Frame(self.main_frame)
        self.framePassword = tkinter.Frame(self.main_frame)
        self.frameButton = tkinter.Frame(self.main_frame)

        # Labels
        self.label_ = tkinter.Label(self.main_frame, text="Добавляем аккаунт:")

        self.label_name = tkinter.Label(self.frame_name, text="Name: ")
        self.label_site = tkinter.Label(self.frame_site, text="Site: ")
        self.labelLogin = tkinter.Label(self.frameLogin, text="Login: ")
        self.labelPassword = tkinter.Label(self.framePassword, text="Password: ")

        # Entry's
        self.entry_name = tkinter.Entry(self.frame_name)
        self.entry_site = tkinter.Entry(self.frame_site)
        self.entry_login = tkinter.Entry(self.frameLogin)
        self.entryPassword = tkinter.Entry(self.framePassword)

        # Buttons
        self.submitButton = tkinter.Button(
            self.frameButton,
            text="Принять",
            command=self.submitAccountInfo
        )

        # Packing
        self.label_.pack(pady=(0, 20))

        self.label_name.pack(side="left")
        self.label_site.pack(side="left", pady=(0,10))
        self.labelLogin.pack(side="left")
        self.labelPassword.pack(side="left")
        
        self.entry_name.pack(padx=(31, 0))
        self.entry_site.pack(padx=(47, 0))
        self.entry_login.pack(padx=(34, 0))
        self.entryPassword.pack()

        self.submitButton.pack()

        self.frame_name.pack(pady=(0, 14))
        self.frame_site.pack(pady=(0, 5))
        self.frameLogin.pack(pady=(0, 13))
        self.framePassword.pack(pady=(0, 15))
        self.frameButton.pack()

        self.main_frame.pack()

    def submitAccountInfo(self):
        self.name = self.entry_name.get()
        self.site = self.entry_site.get()
        self.account_login = self.entry_login.get()
        self.account_password = self.entryPassword.get()

        addAccount(self.login, self.name, self.site, self.account_login, self.account_password)

        self.mainPage()

    def log_in(self):
        self.main_frame.pack_forget()

        self.mainLogIn_frame = tkinter.Frame(self.window)
        self.NameFrame = tkinter.Frame(self.mainLogIn_frame)
        self.frame_login = tkinter.Frame(self.mainLogIn_frame)
        self.frame_password = tkinter.Frame(self.mainLogIn_frame)
        self.frame_button = tkinter.Frame(self.mainLogIn_frame)

        self.hey_label = tkinter.Label(self.NameFrame, text="Зайдите в свой аккаунт <3:")

        self.label_login = tkinter.Label(self.frame_login, text="Логин:")
        self.label_password = tkinter.Label(self.frame_password, text="Пароль:")

        self.entry_login = tkinter.Entry(self.frame_login)
        self.entry_password = tkinter.Entry(self.frame_password)

        self.LogInButton = tkinter.Button(self.frame_button, 
                                        text="Авторизоваться", 
                                        command=self.LogInMethod)

        self.hey_label.pack()
        self.label_login.pack(side="left", padx=7)
        self.label_password.pack(side="left")
        self.entry_login.pack()
        self.entry_password.pack()
        self.LogInButton.pack()

        self.NameFrame.pack()
        self.frame_login.pack(pady=(30, 20))
        self.frame_password.pack()
        self.frame_button.pack(pady=(20, 0))

        self.mainLogIn_frame.pack()


if __name__ == "__main__":
    application = MyGUI()