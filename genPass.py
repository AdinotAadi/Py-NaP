from tkinter import Button, Entry, Frame, Label, LabelFrame, Tk
import secrets
from tkinter.constants import END
import string


class PassGen:
    def __init__(self):
        self.window = Tk()
        self.window.title("Generate Password")
        self.window.geometry("500x300")

        # Label Frame
        self.labelFrame = LabelFrame(
            self.window, text="Enter the number of characters")
        self.labelFrame.pack(pady=20)

        # Entry box for number of characters
        self.lengthEntryBox = Entry(self.labelFrame, width=20)
        self.lengthEntryBox.pack(padx=20, pady=20)

        # Declaring feedback if no length is found
        self.feedback = Label(self.window)

        # Entry box for password
        self.passwordEntryBox = Entry(
            self.window, text="", width=50)
        self.passwordEntryBox.pack(pady=20)

        # Frame for buttons
        self.buttonFrame = Frame(self.window)
        self.buttonFrame.pack(pady=20)

        # Generate Password Button
        generatebtn = Button(
            self.buttonFrame, text="Generate Password", command=self.randstr)
        generatebtn.grid(row=0, column=0, padx=10)

        # Copy Password Button
        copybtn = Button(self.buttonFrame,
                          text="Copy Password", command=self.copypassword)
        copybtn.grid(row=0, column=1, padx=10)

    def randstr(self):
        self.passwordEntryBox.delete(0, END)
        try:
            n = int(self.lengthEntryBox.get())
            self.feedback.destroy()  # Destroy feedback if length is there
            characters = string.ascii_letters + string.digits + string.punctuation
            output = "".join(secrets.choice(characters) for i in range(n))
            self.passwordEntryBox.insert(0, output)
        except ValueError:
            self.feedback = Label(self.window, fg="red",
                                  text="Please enter number of characters")
            self.feedback.place(x=130, y=100)

    def copypassword(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.passwordEntryBox.get())


if __name__ == "__main__":
    PassGen().window.mainloop()