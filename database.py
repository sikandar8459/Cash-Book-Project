import sqlite3

conn = sqlite3.connect("CashBook.db")
cur = conn.cursor()

def create_table():
	cur.execute("create table cash_book (date text, time text, day text, amount text, remarks text, type text)")
	conn.commit()

	print("Table created successfully...")

# create_table()

def fetch():
	cur.execute("select * from cash_book")
	result = cur.fetchall()
	print(result)

fetch()