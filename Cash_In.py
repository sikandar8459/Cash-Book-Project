from tkinter import *
import tkinter.messagebox as msg
from time import gmtime, strftime
from PIL import Image, ImageTk
import random as rd
import sqlite3

conn = sqlite3.connect("CashBook.db")
cur = conn.cursor()

class CashInClass:
	def __init__(self, root):
		self.root = root
		self.root.title("Cash Book | Developed by Sikandar Singh")
		self.root.geometry("400x600+600+10")
		self.root.resizable(0,0)
		self.root.config(bg = "white")
		self.root.focus_force()
		self.root.grab_set()

		p1 = PhotoImage(file = 'Icons/1.png')   
		self.root.iconphoto(False, p1)

		self.cashin_img = Image.open("Icons/2.png")
		self.cashin_img = self.cashin_img.resize((60, 60), Image.LANCZOS)
		self.cashin_img = ImageTk.PhotoImage(self.cashin_img)

		Label(self.root, text = "CASH IN", image = self.cashin_img, compound = LEFT, padx = 20, bg = "white", fg = "green", bd = 0, font = ("goudy old style", 18, "bold")).place(x = 0, y = 0, relwidth = 1, height = 60)

		self.cash_in = Image.open("Images/Cash_In.png")
		self.cash_in = self.cash_in.resize((120, 60), Image.LANCZOS)
		self.cash_in = ImageTk.PhotoImage(self.cash_in)

		Label(self.root, image = self.cash_in, bg = "white", fg = "darkblue", bd = 0, font = ("goudy old style", 18, "bold")).place(x = 10, y = 70, relwidth = 1)
		# strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

		self.date = strftime("%d %b %Y")
		self.time_ = strftime("%H :%M :%S")
		self.day = strftime("%a")
		self.cashIn_val = StringVar()
		self.amount = StringVar()
		self.remarks = StringVar()

		Label(self.root, text = f"Date : {self.date}", fg = "green", bg = "white", font = ("times new roman", 13)).place(x = 50, y = 135)
		Label(self.root, text = f"Time : {self.time_}", fg = "green", bg = "white", font = ("times new roman", 13)).place(x = 230, y = 135)
		Label(self.root, text = f"Day : {self.day}", fg = "green", bg = "white", font = ("times new roman", 13)).place(x = 5, y = 160, relwidth = 1)

		Label(self.root, text = "Amount", font = ("goudy old style", 17, "bold"), anchor = "w", padx = 10, fg = "green", bg = "white").place(x = 0, y = 200, relwidth = 1, height = 50)
		Entry(self.root, textvariable = self.amount, font = ("goudy old style", 17), bg = "lightgreen").place(x = 10, y = 250, width = 380)

		Label(self.root, text = "Remarks", font = ("goudy old style", 17, "bold"), anchor = "w", padx = 10, fg = "green", bg = "white").place(x = 0, y = 300, relwidth = 1, height = 50)
		Entry(self.root, textvariable = self.remarks, font = ("goudy old style", 17), bg = "lightgreen").place(x = 10, y = 350, width = 380)

		Label(self.root, text = "Type", font = ("goudy old style", 17, "bold"), anchor = "w", padx = 10, fg = "green", bg = "white").place(x = 0, y = 400, relwidth = 1, height = 50)
		Entry(self.root, textvariable = self.cashIn_val, state = "readonly", font = ("goudy old style", 17), bg = "lightgreen", fg = "green").place(x = 10, y = 450, width = 380)
		self.cashIn_val.set("Cash In")
		
		Button(self.root, cursor = "hand2", width = 8, text = "Save", command = self.save, font = ("goudy old style", 18, "bold"), fg = "white", bg = "green", bd = 2, relief = RAISED).place(x = 70, y = 510, width = 100, height = 40)
		Button(self.root, cursor = "hand2", width = 8, text = "Clear", command = self.clear_data, font = ("goudy old style", 18, "bold"), fg = "white", bg = "orange", bd = 2, relief = RAISED).place(x = 210, y = 510, width = 100, height = 40)

	def clear_data(self):
		self.amount.set("")
		self.remarks.set("")
		self.cashIn_val.set("Cash In")

	def save(self):
		if self.amount.get() == "" or self.remarks.get() == "":
			msg.showerror("Error","All fields are required..", parent = self.root)
		else:
			cur.execute("insert into cash_book values (?,?,?,?,?,?)", (self.date, self.time_, self.day, self.amount.get(), self.remarks.get(), self.cashIn_val.get()))
			conn.commit()
			msg.showinfo("Success","Cashed in successfully..", parent = self.root)
			self.clear_data()


if __name__ == '__main__':
	root = Tk()
	obj = CashInClass(root)
	root.mainloop()