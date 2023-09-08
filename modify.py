from tkinter import *
from PIL import ImageTk, Image

class ModifyClass:
	def __init__(self, root):
		self.window = root
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

		Entry(self.main_frame, bd = 2, relief = SUNKEN, font = ("goudy old style", 18, "bold"), bg = "lightgreen", width = 18).grid(row = 0, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, bd = 2, relief = SUNKEN, font = ("goudy old style", 18, "bold"), bg = "lightgreen", width = 18).grid(row = 1, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, bd = 2, relief = SUNKEN, font = ("goudy old style", 18, "bold"), bg = "lightgreen", width = 18).grid(row = 2, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, bd = 2, relief = SUNKEN, font = ("goudy old style", 18, "bold"), bg = "lightgreen", width = 18).grid(row = 3, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, bd = 2, relief = SUNKEN, font = ("goudy old style", 18, "bold"), bg = "lightgreen", width = 18).grid(row = 4, column = 1, sticky = "w", pady = 10, padx = 10)
		Entry(self.main_frame, bd = 2, relief = SUNKEN, font = ("goudy old style", 18, "bold"), bg = "lightgreen", width = 18).grid(row = 5, column = 1, sticky = "w", pady = 10, padx = 10)

		Button(self.main_frame, cursor = "hand2", width = 8, text = "Update", font = ("goudy old style", 16, "bold"), fg = "white", bg = "green", bd = 2, relief = RAISED).grid(row = 6, column = 0, sticky = "e", pady = 10, padx = 10)
		Button(self.main_frame, cursor = "hand2", width = 8, text = "Delete", font = ("goudy old style", 16, "bold"), fg = "white", bg = "red", bd = 2, relief = RAISED).grid(row = 6, column = 1, sticky = "w", pady = 10, padx = 10)

		Label(self.main_frame, text = "\n\nModify your data means you will able to\nUpdate & Delete your data", font = ("goudy old style", 12, "bold"), bg = "white").grid(row = 7, columnspan = 5, sticky = "n")


if __name__ == '__main__':
	root = Tk()
	obj = ModifyClass(root)
	root.mainloop()

