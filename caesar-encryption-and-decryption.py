import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.minsize(width=460, height=270)
root.title("Verschlüsselungs-Software")

selected_operation = tk.StringVar()

def encrypt(text, s):
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

def decrypt(text, s):
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

def start_operation():
    if selected_operation.get() == "verschlüsseln":
        encrypted_input = encrypt(message_entry_field.get(), int(key_entry_field.get()))
        result_label2.delete(0, tk.END)
        result_label2.insert(0, encrypted_input)
    elif selected_operation.get() == "entschlüsseln":
        decrypted_input = decrypt(message_entry_field.get(), int(key_entry_field.get()))
        result_label2.delete(0, tk.END)
        result_label2.insert(0, decrypted_input)
    else:
        print("Bitte Operation auswählen")


input_frame = ttk.Frame(root, padding=10)
input_frame.grid(column=0, row=0)
separator = ttk.Separator(root)
separator.grid(column=0, row=1, columnspan=4, sticky="ew", pady=5)
output_frame = ttk.Frame(root, padding=10)
output_frame.grid(column=0, row=2)

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

message_label = ttk.Label(input_frame, text="Nachricht:", font=("Roboto", 15))
message_label.grid(column=0, row=0)

message_entry_field = ttk.Entry(input_frame, width=30, font=("Roboto", 15))
message_entry_field.grid(column=1, row=0)

message_entry_field_scrollbar = ttk.Scrollbar(input_frame, orient="horizontal", command=message_entry_field.xview)
message_entry_field_scrollbar.grid(column=1, row=1, pady=1, sticky="ew")
message_entry_field.configure(xscrollcommand=message_entry_field_scrollbar.set)

key_label = ttk.Label(input_frame, text="Key:", font=("Roboto", 15))
key_label.grid(column=0, row=2)

key_entry_field = ttk.Entry(input_frame, width=3, font=("Roboto", 15))
key_entry_field.grid(column=1, row=2, pady=5, sticky="w")

operation_label = ttk.Label(input_frame, text="Operation:", font=("Roboto", 15))
operation_label.grid(column=0, row=3)

encrypt_radiobutton = ttk.Radiobutton(input_frame, text="Verschlüsseln", variable=selected_operation, value="verschlüsseln")
encrypt_radiobutton.grid(column=1, row=3, sticky="w")
decrypt_radiobutton = ttk.Radiobutton(input_frame, text="Entschlüsseln", variable=selected_operation, value="entschlüsseln")
decrypt_radiobutton.grid(column=1, row=4, sticky="w")

start_operation_button = ttk.Button(input_frame, text="Operation ausführen", command=start_operation)
start_operation_button.grid(column=0, row=5, columnspan=2, sticky="ew")

result_label = ttk.Label(output_frame, text="Ergebnis:", font=("Roboto", 15))
result_label.grid(column=0, row=0, sticky="w")

result_label2 = ttk.Entry(output_frame, width=30, font=("Roboto", 15))
result_label2.grid(column=1, row=0)

result_label2_scrollbar = ttk.Scrollbar(output_frame, orient="horizontal", command=result_label2.xview)
result_label2_scrollbar.grid(column=1, row=1, sticky="ew")
result_label2.configure(xscrollcommand=result_label2_scrollbar.set)


root.mainloop()