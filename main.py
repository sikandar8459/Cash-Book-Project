from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
from PIL import Image, ImageTk
import random as rd
import sqlite3

from Cash_In import CashInClass
from Cash_Out import CashOutClass
from SaveDataExcel import DataToExcel

conn = sqlite3.connect("CashBook.db")
cur = conn.cursor()

class CashBookClass:
	def __init__(self, root):
		self.root = root
		self.root.title("Cash Book | Developed by Sikandar Singh")
		self.root.geometry("900x600+100+10")
		self.root.resizable(0,0)
		self.root.config(bg = "white")
		self.root.grab_set()

		# self.root.overrideredirect(1)
		# self.root.bind("<Enter>", self.ShowData)

		p1 = PhotoImage(file = 'Icons/1.png')   
		self.root.iconphoto(False, p1)

		self.main_img = Image.open("Icons/4.png")
		self.main_img = self.main_img.resize((60, 60), Image.LANCZOS)
		self.main_img = ImageTk.PhotoImage(self.main_img)

		Label(self.root, text = "Cash Book", anchor = "w", image = self.main_img, compound = LEFT, padx = 20, bg = "white", fg = "darkblue", bd = 0, font = ("goudy old style", 45, "bold")).place(x = 0, y = 0, relwidth = 1, height = 60)

		self.download_ico = Image.open("Icons/download.png")
		self.download_ico = self.download_ico.resize((25, 25), Image.LANCZOS)
		self.download_ico = ImageTk.PhotoImage(self.download_ico)
		Button(self.root, image = self.download_ico, compound = LEFT, padx = 10, cursor = "hand2", text = "Download", command = self.DownloadFile, font = ("goudy old style", 15, "bold"), fg = "white", bg = "blue", bd = 2, relief = RAISED).place(x = 715, y = 20, height = 40)

		self.main_frame = LabelFrame(self.root, bg = "white", bd = 0, relief = GROOVE)
		self.main_frame.place(x = 20, y = 70, width = 860, height = 100)

		#--CASH IN--#
		cur.execute("select amount from cash_book where type = ?",("Cash In",))
		result = cur.fetchall()
		self.cashin_total = 0
		for i in result:
			self.cashin_total += int(i[0])

		self.plus = Image.open("Icons/plus.png")
		self.plus = self.plus.resize((60, 60), Image.LANCZOS)
		self.plus = ImageTk.PhotoImage(self.plus)
		self.cashin_val = rd.randint(1111, 9999)
		Label(self.main_frame, text = f"Cash In\n{self.cashin_total}", image = self.plus, compound = LEFT, padx = 10, fg = "green", bg = "white", font = ("times new roman", 20), bd = 1, relief = GROOVE).place(x = 10, y = 7, width = 270, height = 80)

		#--CASH OUT--#
		cur.execute("select amount from cash_book where type = ?",("Cash Out",))
		result = cur.fetchall()
		self.cashout_total = 0
		for i in result:
			self.cashout_total += int(i[0])

		self.minus = Image.open("Icons/minus_.png")
		self.minus = self.minus.resize((60, 60), Image.LANCZOS)
		self.minus = ImageTk.PhotoImage(self.minus)
		self.cashout_val = rd.randint(1111, 9999)
		Label(self.main_frame, text = f"Cash Out\n{self.cashout_total}", image = self.minus, compound = LEFT, padx = 10, fg = "red", bg = "white", font = ("times new roman", 20), bd = 1, relief = GROOVE).place(x = 290, y = 7, width = 270, height = 80)

		self.equal = Image.open("Icons/equal.png")
		self.equal = self.equal.resize((60, 60), Image.LANCZOS)
		self.equal = ImageTk.PhotoImage(self.equal)
		Label(self.main_frame, text = f"Total Balance\n{self.cashin_total - self.cashout_total}", image = self.equal, compound = LEFT, padx = 10, fg = "orange", bg = "white", font = ("times new roman", 20), bd = 1, relief = GROOVE).place(x = 572, y = 7, width = 270, height = 80)

		self.search_fields = LabelFrame(self.root, bg = "white", bd = 2, relief = GROOVE)
		self.search_fields.place(x = 20, y = 180, width = 860)

		self.search_val = StringVar()
		Label(self.search_fields, text = "Search", font = ("goudy old style", 18, "bold"), fg = "darkblue", bg = "white").grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
		Entry(self.search_fields, textvariable = self.search_val, font = ("goudy old style", 16), bg = "white", bd = 2, relief = GROOVE, width = 21).grid(row = 0, column = 1, padx = 10, pady = 10, sticky = "w")

		self.search_ico = Image.open("Icons/search.png")
		self.search_ico = self.search_ico.resize((35, 35), Image.LANCZOS)
		self.search_ico = ImageTk.PhotoImage(self.search_ico)		
		Button(self.search_fields, image = self.search_ico, command = self.SearchData, compound = LEFT, padx = 10, cursor = "hand2", width = 120, text = "Search", font = ("goudy old style", 18, "bold"), fg = "white", bg = "orange", bd = 2, relief = RAISED).grid(row = 0, column = 3, padx = 10, pady = 10, sticky = "w")

		self.cashIn_ico = Image.open("Icons/plus.png")
		self.cashIn_ico = self.cashIn_ico.resize((35, 35), Image.LANCZOS)
		self.cashIn_ico = ImageTk.PhotoImage(self.cashIn_ico)		
		Button(self.search_fields, image = self.cashIn_ico, compound = LEFT, padx = 10, cursor = "hand2", width = 120, text = "Cash In ", command = self.CashInData, font = ("goudy old style", 18, "bold"), fg = "white", bg = "green", bd = 2, relief = RAISED).grid(row = 0, column = 4, padx = 10, pady = 10, sticky = "w")

		self.cashOut_ico = Image.open("Icons/minus.png")
		self.cashOut_ico = self.cashOut_ico.resize((35, 35), Image.LANCZOS)
		self.cashOut_ico = ImageTk.PhotoImage(self.cashOut_ico)		
		Button(self.search_fields, command = self.CashOutData, image = self.cashOut_ico, compound = LEFT, padx = 10, cursor = "hand2", width = 130, text = "Cash Out", font = ("goudy old style", 18, "bold"), fg = "white", bg = "red", bd = 2, relief = RAISED).grid(row = 0, column = 5, padx = 10, pady = 10, sticky = "w")

		self.EntryFrame = LabelFrame(self.root, bd = 2, relief = GROOVE, bg = "white")
		self.EntryFrame.place(x = 20, y = 270, width = 860, height = 250)

		self.scroll_x = Scrollbar(self.EntryFrame, orient = HORIZONTAL)
		self.scroll_y = Scrollbar(self.EntryFrame, orient = VERTICAL)

		self.EntryTable = ttk.Treeview(self.EntryFrame, columns = ("date","time","day","amount","remarks","type"), xscrollcommand = self.scroll_x.set, yscrollcommand = self.scroll_y.set)
		self.scroll_x.pack(fill = X, side = BOTTOM) 
		self.scroll_y.pack(fill = Y, side = RIGHT)
		self.scroll_x.config(command = self.EntryTable.xview)
		self.scroll_y.config(command = self.EntryTable.yview)
		self.EntryTable.pack(fill = BOTH, expand = 1)

		self.EntryTable.column("date", width = 100, minwidth = 100, anchor = "n")
		self.EntryTable.column("time", width = 100, minwidth = 100, anchor = "n")
		self.EntryTable.column("day", width = 100, minwidth = 60, anchor = "n")
		self.EntryTable.column("amount", width = 200, minwidth = 80, anchor = "n")
		self.EntryTable.column("remarks", width = 100, minwidth = 250, anchor = "n")
		self.EntryTable.column("type", width = 300, minwidth = 100, anchor = "n")

		self.EntryTable["show"] = "headings"

		self.EntryTable.heading("date", text = "Date")
		self.EntryTable.heading("time", text = "Time")
		self.EntryTable.heading("day", text = "Day")
		self.EntryTable.heading("amount", text = "Amount")
		self.EntryTable.heading("remarks", text = "Remarks")
		self.EntryTable.heading("type", text = "Type")
		self.ShowData()

		self.EntryTable.bind("<ButtonRelease-1>", self.UpdateWindow)

		Label(self.root, font = ("times new roman", 12), text = "* || Developed by Sikandar Singh || sikandarsingh.official.22@gmail.com || KAALI GROUPS || *", bg = "darkred", fg = "white", bd = 2, relief = RAISED).place(x = 20, y = 540, width = 700, height = 40)

		self.exit_ico = Image.open("Icons/minus_.png")
		self.exit_ico = self.exit_ico.resize((35, 35), Image.LANCZOS)
		self.exit_ico = ImageTk.PhotoImage(self.exit_ico)		
		Button(self.root, image = self.exit_ico, compound = LEFT, padx = 10, cursor = "hand2", text = "Clear", font = ("goudy old style", 18, "bold"), fg = "white", bg = "darkred", bd = 2, relief = RAISED).place(x = 730, y = 540, width = 150, height = 40)

	def ShowData(self):
		try:
			cur.execute("select * from cash_book")
			result = cur.fetchall()
			self.EntryTable.delete(*self.EntryTable.get_children())
			for row in result:
				self.EntryTable.insert("", END, values = row)
		except Exception as ex:
			print(ex)

	def ExitApp(self):
		exit = msg.askyesno("Exit Application","Do you really want to Exit ??", parent = self.root)
		if exit == True:
			self.root.destroy()

	def CashInData(self):
		self.window = Toplevel(self.root)
		self.obj = CashInClass(self.window)

	def CashOutData(self):
		self.window = Toplevel(self.root)
		self.obj = CashOutClass(self.window)

	def GetData(self):
		r = self.EntryTable.focus()
		content = self.EntryTable.item(r)
		i = content["values"]

		self.date_val.set(i[0])
		self.time_val.set(i[1])
		self.day_val.set(i[2])
		self.amount_val.set(i[3])
		self.remarks_val.set(i[4])
		self.type_val.set(i[5])
		
	def UpdateWindow(self, event):
		self.window = Toplevel(self.root)
		self.window.title("Cash Book | Developed by Sikandar Singh")
		self.window.geometry("400x600+600+10")
		self.window.resizable(0,0)
		self.window.config(bg = "white")
		self.window.focus_force()

		p1 = PhotoImage(file = 'Icons/1.png')   
		self.window.iconphoto(False, p1)

		self.cashin_img = Image.open("Icons/2.png")
		self.cashin_img = self.cashin_img.resize((60, 60), Image.LANCZOS)
		self.cashin_img = ImageTk.PhotoImage(self.cashin_img)

		Label(self.window, text = "Modify your data here", image = self.cashin_img, compound = LEFT, padx = 20, bg = "white", fg = "darkblue", bd = 0, font = ("goudy old style", 18, "bold")).place(x = 0, y = 0, relwidth = 1, height = 60)

		self.main_frame = LabelFrame(self.window, bd = 0, relief = GROOVE, bg = "white")
		self.main_frame.place(x = 10, y = 70, width = 380)

		Label(self.main_frame, text = "Date", font = ("goudy old style", 18, "bold"), bg = "white").grid(row = 0, column = 0, sticky = "w", pady = 10, padx = 10)
		Label(self.main_frame, text = "Time", font = ("goudy old style", 18, "bold"), bg = "white").grid(row = 1, column = 0, sticky = "w", pady = 10, padx = 10)
		Label(self.main_frame, text = "Day", font = ("goudy old style", 18, "bold"), bg = "white").grid(row = 2, column = 0, sticky = "w", pady = 10, padx = 10)
		Label(self.main_frame, text = "Amount", font = ("goudy old style", 18, "bold"), bg = "white").grid(row = 3, column = 0, sticky = "w", pady = 10, padx = 10)
		Label(self.main_frame, text = "Remarks", font = ("goudy old style", 18, "bold"), bg = "white").grid(row = 4, column = 0, sticky = "w", pady = 10, padx = 10)
		Label(self.main_frame, text = "Type", font = ("goudy old style", 18, "bold"), bg = "white").grid(row = 5, column = 0, sticky = "w", pady = 10, padx = 10)

		self.date_val = StringVar()
		self.time_val = StringVar()
		self.day_val = StringVar()
		self.amount_val = StringVar()
		self.remarks_val = StringVar()
		self.type_val = StringVar()

		Entry(self.main_frame, textvariable = self.date_val, bd = 2, relief = SUNKEN, font = ("goudy old style", 18), bg = "lightgreen", width = 18).grid(row = 0, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, textvariable = self.time_val, state = "readonly", bd = 2, relief = SUNKEN, font = ("goudy old style", 18), bg = "lightgreen", width = 18).grid(row = 1, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, textvariable = self.day_val, bd = 2, relief = SUNKEN, font = ("goudy old style", 18), bg = "lightgreen", width = 18).grid(row = 2, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, textvariable = self.amount_val, bd = 2, relief = SUNKEN, font = ("goudy old style", 18), bg = "lightgreen", width = 18).grid(row = 3, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, textvariable = self.remarks_val, bd = 2, relief = SUNKEN, font = ("goudy old style", 18), bg = "lightgreen", width = 18).grid(row = 4, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, textvariable = self.type_val, bd = 2, relief = SUNKEN, font = ("goudy old style", 18), bg = "lightgreen", width = 18).grid(row = 5, column = 1, sticky = "w", pady = 10, padx = 10)

		Button(self.main_frame, command = self.UpdateTreeviewData, cursor = "hand2", width = 8, text = "Update", font = ("goudy old style", 16, "bold"), fg = "white", bg = "green", bd = 2, relief = RAISED).grid(row = 6, column = 0, sticky = "e", pady = 10, padx = 10)
		Button(self.main_frame, cursor = "hand2", width = 8, text = "Delete", font = ("goudy old style", 16, "bold"), fg = "white", bg = "red", bd = 2, relief = RAISED).grid(row = 6, column = 1, sticky = "w", pady = 10, padx = 10)

		Label(self.main_frame, text = "\n\nModify your data means you will able to\nUpdate & Delete your data", font = ("goudy old style", 12, "bold"), bg = "white").grid(row = 7, columnspan = 5, sticky = "n")

		self.GetData()

	def UpdateTreeviewData(self):
		try:
			if self.date_val.get() == "" or self.time_val.get() == "" or self.day_val.get() == "" or self.amount_val.get() == "" or self.remarks_val.get() == "" or self.type_val.get() == "":
				msg.showerror("Error","All fields are required...", parent = self.window)
			else:
				update = msg.showinfo("Success", "Do you really want to Update Details", parent = self.window)
				if update == True:
					cur.execute("update cash_book set date=?, time=?, day=?, amount=?, remarks=?, type=? where remarks=?",(self.date_val.get(), self.time_val.get(), self.day_val.get(), self.amount_val.get(), self.remarks_val.get(), self.type_val.get()))
					conn.commit()
					msg.showinfo("Update Success","Your Details has been Updated Successfully..", parent = self.window)
					self.ShowData()
				else:
					msg.showerror("Update Error", "Data not Updated..", parent = self.window)
		except Exception as ex:
			msg.showerror("Error",f"Error due to {ex}", parent = self.window)

	def SearchData(self):
		try:
			if self.search_val.get() == "":
				msg.showerror("Fields Error","All fields are required..", parent = self.root)
			else:
				cur.execute("select * from cash_book where remarks=?",(self.search_val.get(),))
				result = cur.fetchall()
				self.EntryTable.delete(*self.EntryTable.get_children())
				for row in result:
					self.EntryTable.insert("", END, values = row)
		except Exception as ex:
			msg,showerror("Exception Error",f"Error due to {ex}", parent = self.root)

	def DownloadFile(self):
		obj = DataToExcel()

if __name__ == '__main__':
	root = Tk()
	obj = CashBookClass(root)
	root.mainloop()
