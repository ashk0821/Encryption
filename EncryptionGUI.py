from tkinter import *

from EncryptionGUI.Encryptor import Encryptor


class Application(Frame):
    def __init__(self, master):
        self.encryptor = Encryptor("cipher1.txt")
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        msg = Label(self, text="Enter the message:")
        msg.grid(row=0, column=1, columnspan=2, sticky=W)

        self.message_entry = Entry(self, width=40)
        self.message_entry.grid(row=1, column=1, columnspan=2, sticky=W)

        e = Button(self, text="Encrypt", command=self.encrypt)
        e.grid(row=2, column=1, sticky=E)

        d = Button(self, text="Decrypt", command=self.decrypt)
        d.grid(row=2, column=2, sticky=W)

        Label(self, text="Encryption/Decryption:").grid(row=3, column=1, sticky=W)
        self.output = Text(self, width=52, height=15, wrap=WORD)
        self.output.grid(row=4, column=1, columnspan=3, sticky=W)

    def encrypt(self):
        message = self.message_entry.get()
        character = self.encryptor.encrypt_message(message)
        self.output.delete(0.0, END)
        self.output.insert(0.0, character)

    def decrypt(self):
        message = self.message_entry.get()
        character = self.encryptor.decrypt_message(message)
        self.output.delete(0.0, END)
        self.output.insert(0.0, character)


root = Tk()
root.title("Encryption/Decryption")
app = Application(root)
root.mainloop()