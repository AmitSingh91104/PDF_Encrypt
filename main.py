from tkinter import filedialog
import PyPDF2
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("PDF Encryption")
root.geometry("300x400+600+1")
root.resizable(False, False)

def select_file():
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(tk.END, file_path)

def encrypt_pdf():
    input_file = input_entry.get()
    password = password_entry.get()

    if input_file and password:
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf")

        with open(input_file, 'rb') as file:
            pdf = PyPDF2.PdfFileReader(file)
            pdf.encrypt(password)

            with open(output_file, 'wb') as output:
                pdf.write(output)

        messagebox.showinfo("Encryption Complete", "PDF file encrypted successfully.")
    else:
        messagebox.showwarning("Missing Information", "Please select an input file and enter a password.")

def decrypt_pdf():
    input_file = input_entry.get()
    password = password_entry.get()

    if input_file and password:
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf")

        with open(input_file, 'rb') as file:
            pdf = PyPDF2.PdfFileReader(file)

            if pdf.isEncrypted:
                pdf.decrypt(password)

                with open(output_file, 'wb') as output:
                    pdf.write(output)

                tk.messagebox.showinfo("Decryption Complete", "PDF file decrypted successfully.")
            else:
                tk.messagebox.showwarning("Invalid PDF", "The selected PDF file is not encrypted.")
    else:
        tk.messagebox.showwarning("Missing Information", "Please select an input file and enter a password.")

input_label = tk.Label(root, text="Input File:")
input_label.pack()
input_entry = tk.Entry(root, width=50)
input_entry.pack()

cl1 = PhotoImage(file="button_select-file.png")
cl1_image = Button(root,image=cl1,borderwidth=0,cursor="hand2",bd=0,command=select_file)
cl1_image.place(x=100, y=60)

cl2 = PhotoImage(file="button_decrypt-pdf.png")
cl2_image = Button(root,image=cl2,borderwidth=0,cursor="hand2",bd=0,command=decrypt_pdf)
cl2_image.place(x=100,y=260)

cl3 = PhotoImage(file="button_encrypt-pdf.png")
cl3_image = Button(root,image=cl3,borderwidth=0,cursor="hand2",bd=0,command=encrypt_pdf)
cl3_image.place(x=100,y=180)

password_label = tk.Label(root, text="Password:")
password_label.place(x=120,y=130)
password_entry = tk.Entry(root, width=50, show="*")
password_entry.place(x=0,y=150)

root.mainloop()