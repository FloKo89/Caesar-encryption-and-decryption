import tkinter as tk
from tkinter import ttk

class CaesarEncryptionAndDecryption(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.minsize(width=460, height=270)
        self.title("Verschlüsselungs-Software")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        Gui(self, padding=10).grid(column=0, row=0)

class Gui(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.selected_operation = tk.StringVar()

        message_label = ttk.Label(self, text="Nachricht:", font=("Roboto", 15))
        message_label.grid(column=0, row=0)

        self.message_entry_field = ttk.Entry(self, width=30, font=("Roboto", 15))
        self.message_entry_field.grid(column=1, row=0)

        self.message_entry_field_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.message_entry_field.xview)
        self.message_entry_field_scrollbar.grid(column=1, row=1, pady=1, sticky="ew")
        self.message_entry_field.configure(xscrollcommand=self.message_entry_field_scrollbar.set)

        key_label = ttk.Label(self, text="Key:", font=("Roboto", 15))
        key_label.grid(column=0, row=2)

        self.key_entry_field = ttk.Entry(self, width=3, font=("Roboto", 15))
        self.key_entry_field.grid(column=1, row=2, pady=5, sticky="w")

        operation_label = ttk.Label(self, text="Operation:", font=("Roboto", 15))
        operation_label.grid(column=0, row=3)

        encrypt_radiobutton = ttk.Radiobutton(self, text="Verschlüsseln", variable=self.selected_operation, value="verschlüsseln")
        encrypt_radiobutton.grid(column=1, row=3, sticky="w")
        decrypt_radiobutton = ttk.Radiobutton(self, text="Entschlüsseln", variable=self.selected_operation, value="entschlüsseln")
        decrypt_radiobutton.grid(column=1, row=4, sticky="w")

        start_operation_button = ttk.Button(self, text="Operation ausführen", command=self.start_operation)
        start_operation_button.grid(column=0, row=5, columnspan=2, sticky="ew")

        self.separator = ttk.Separator(self)
        self.separator.grid(column=0, row=6, columnspan=4, sticky="ew", pady=5)

        result_label = ttk.Label(self, text="Ergebnis:", font=("Roboto", 15))
        result_label.grid(column=0, row=7, sticky="w")

        self.result_label2 = ttk.Entry(self, width=30, font=("Roboto", 15))
        self.result_label2.grid(column=1, row=7)

        self.result_label2_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.result_label2.xview)
        self.result_label2_scrollbar.grid(column=1, row=8, sticky="ew")
        self.result_label2.configure(xscrollcommand=self.result_label2_scrollbar.set)

    def encrypt(self, text, s):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char == " " or char == "." or char == "!" or char == "?":
                result += char
            elif char.isnumeric():
                result += chr((ord(char) + s - 48) % 10 + 48)
            elif char.isupper():
                result += chr((ord(char) + s - 65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    def decrypt(self, text, s):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char == " " or char == "." or char == "!" or char == "?":
                result += char
            elif char.isnumeric():
                result += chr((ord(char) - s - 48) % 10 + 48)
            elif char.isupper():
                result += chr((ord(char) - s - 65) % 26 + 65)
            else:
                result += chr((ord(char) - s - 97) % 26 + 97)
        return result

    def start_operation(self):
        if self.selected_operation.get() == "verschlüsseln":
            encrypted_input = self.encrypt(self.message_entry_field.get(), int(self.key_entry_field.get()))
            self.result_label2.delete(0, tk.END)
            self.result_label2.insert(0, encrypted_input)
        elif self.selected_operation.get() == "entschlüsseln":
            decrypted_input = self.decrypt(self.message_entry_field.get(), int(self.key_entry_field.get()))
            self.result_label2.delete(0, tk.END)
            self.result_label2.insert(0, decrypted_input)
        else:
            print("Bitte Operation auswählen")


root = CaesarEncryptionAndDecryption()
root.mainloop()