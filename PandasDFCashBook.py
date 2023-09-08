import pandas as pd
import sqlite3

conn = sqlite3.connect("CashBook.db")
cur = conn.cursor()

cur.execute("select * from cash_book")
datas = cur.fetchall()
# print(data)

CashBook_Data = pd.DataFrame(datas)
# print(CashBook_Data)

CashBook_Data.to_excel("CashBook.xlsx", index = False)
print("Data saved to Excel Successfully...")