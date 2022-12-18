import hashlib
from tkinter.constants import BOTH, CENTER, END, LEFT, RIGHT, VERTICAL, Y
from genPass import PassGen
from database import init_database
from tkinter import Button, Canvas, Entry, Frame, Label, Scrollbar, Tk
from functools import partial
from vault import VaultMethods


class PasswordManager:

    def __init__(self):
        self.db, self.cursor = init_database()
        self.window = Tk()
        self.window.update()
        self.window.title("Password Manager")
        self.window.geometry("450x350")

    def welcome_new_user(self):
        self.window.geometry("450x200")

        label1 = Label(self.window, text="Create New Master Password")
        label1.config(anchor=CENTER)
        label1.pack(pady=10)

        mp_entry_box = Entry(self.window, width=20, show="*")
        mp_entry_box.pack()
        mp_entry_box.focus()

        label2 = Label(self.window, text="Enter the password again")
        label2.config(anchor=CENTER)
        label2.pack(pady=10)

        rmp_entry_box = Entry(self.window, width=20, show="*")
        rmp_entry_box.pack()

        self.feedback = Label(self.window)
        self.feedback.pack()

        savebtn = Button(self.window, text="Create Password",
                         command=partial(self.saveMasterPassword, mp_entry_box, rmp_entry_box))
        savebtn.pack(pady=5)

    def loginuser(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.geometry("450x200")

        label1 = Label(self.window, text="Enter your master password")
        label1.config(anchor=CENTER)
        label1.place(x=150, y=50)

        self.passwordEntryBox = Entry(self.window, width=20, show="*")
        self.passwordEntryBox.place(x=160, y=80)
        self.passwordEntryBox.focus()

        self.feedback = Label(self.window)
        self.feedback.place(x=170, y=105)

        login_btn = Button(self.window, text="Log In", command=partial(
            self.checkMasterPass, self.passwordEntryBox))
        login_btn.place(x=200, y=130)

    def saveMasterPassword(self, eb1, eb2):
        password1 = eb1.get()
        password2 = eb2.get()
        if password1 == password2:
            hashed_password = self.encryptPassword(password1)
            insert_command = """INSERT INTO master(password)
            VALUES(?) """
            self.cursor.execute(insert_command, [hashed_password])
            self.db.commit()
            self.loginuser()
        else:
            self.feedback.config(text="Passwords do not match", fg="red")

    def exit(self):
        for window in self.window:
            window.destory()

    def checkMasterPass(self, eb):
        hashed_password = self.encryptPassword(eb.get())
        self.cursor.execute(
            "SELECT * FROM master WHERE id = 1 AND password = ?", [hashed_password])
        if self.cursor.fetchall():
            self.passwordVaultScreen()
        else:
            self.passwordEntryBox.delete(0, END)
            self.feedback.config(text="Incorrect password", fg="red")

    def passwordVaultScreen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        vault_methods = VaultMethods()

        self.window.geometry("720x350")
        mainframe = Frame(self.window)
        mainframe.pack(fill=BOTH, expand=1)

        maincanvas = Canvas(mainframe)
        maincanvas.pack(side=LEFT, fill=BOTH, expand=1)

        mainscrollbar = Scrollbar(
            mainframe, orient=VERTICAL, command=maincanvas.yview)
        mainscrollbar.pack(side=RIGHT, fill=Y)

        maincanvas.configure(yscrollcommand=mainscrollbar.set)
        maincanvas.bind('<Configure>', lambda e: maincanvas.configure(
            scrollregion=maincanvas.bbox("all")))

        secondframe = Frame(maincanvas)
        maincanvas.create_window((0, 0), window=secondframe, anchor="nw")

        exitbtn = Button(secondframe, text="Exit",
                         command=exit)
        exitbtn.grid(row=1, column=0, pady=10)

        generatepasswordbtn = Button(secondframe, text="Generate Password",
                                     command=PassGen)
        generatepasswordbtn.grid(row=1, column=2, pady=10)

        addpasswordbtn = Button(
            secondframe, text="Add New Password", command=partial(vault_methods.add_password, self.passwordVaultScreen))
        addpasswordbtn.grid(row=1, column=3, pady=10)

        lbl = Label(secondframe, text="Platform")
        lbl.grid(row=2, column=0, padx=40, pady=10)
        lbl = Label(secondframe, text="Email/Username")
        lbl.grid(row=2, column=1, padx=40, pady=10)

        self.cursor.execute("SELECT * FROM vault")

        if self.cursor.fetchall():
            i = 0
            while True:
                self.cursor.execute("SELECT * FROM vault")
                array = self.cursor.fetchall()

                platformlabel = Label(secondframe, text=(array[i][1]))
                platformlabel.grid(column=0, row=i + 3)

                accountlabel = Label(secondframe, text=(array[i][2]))
                accountlabel.grid(column=1, row=i + 3)

                copybtn = Button(secondframe, text="Copy Password",
                                 command=partial(self.copy_text, array[i][3]))
                copybtn.grid(column=2, row=i + 3, pady=10, padx=10)
                updatebtn = Button(secondframe, text="Update Password",
                                   command=partial(vault_methods.updatepassword, array[i][0],
                                                   self.passwordVaultScreen))
                updatebtn.grid(column=3, row=i + 3, pady=10, padx=10)
                removebtn = Button(secondframe, text="Delete Password",
                                   command=partial(vault_methods.removepassword, array[i][0],
                                                   self.passwordVaultScreen))
                removebtn.grid(column=4, row=i + 3, pady=10, padx=10)

                i += 1

                self.cursor.execute("SELECT * FROM vault")
                if len(self.cursor.fetchall()) <= i:
                    break

    def encryptPassword(self, password):
        password = password.encode("utf-8")
        encoded_text = hashlib.md5(password).hexdigest()
        return encoded_text

    def copy_text(self, text):
        self.window.clipboard_clear()
        self.window.clipboard_append(text)


def main():
    db, cursor = init_database()
    cursor.execute("SELECT * FROM master")
    manager = PasswordManager()
    if cursor.fetchall():
        manager.loginuser()
    else:
        manager.welcome_new_user()
    manager.window.mainloop()


if __name__ == '__main__':
    main()
