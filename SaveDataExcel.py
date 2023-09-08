import sqlite3
import pandas.io.sql as sql
import xlwt
from time import gmtime, strftime

class DataToExcel:
	def __init__(self):
		self.date = strftime("%d %b %Y")
		self.time_ = strftime("%H :%M :%S")
		print(strftime("%d%Y-%H%M%S"))

		conn = sqlite3.connect("CashBook.db")
		cur = conn.cursor()

		df = sql.read_sql("select * from cash_book", conn)

		# print(df)
		# print("\n")
		# print(f"All Excel File/CashBook Details {strftime('%Y%d')} at {strftime('%H%M%S')}.xls")

		df.to_excel(f"All Excel File/CashBook Details {strftime('%Y%d')} at {strftime('%H%M%S')}.xls")

if __name__ == '__main__':
	obj = DataToExcel()