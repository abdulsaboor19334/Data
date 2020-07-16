import sqlite3
from datetime import datetime
import os



conn = sqlite3.connect('garment.db')
c = conn

# c.execute(
#     "CREATE TABLE garment(barcode INT PRIMARY KEY, name VARCHAR, sale_price REAL,cost_price REAL,discount_price REAL, discount DECIMAL(3,2) DEFAULT '0.00' , gender VARCHAR, size VARCHAR, status VARCHAR, day INT,month INT, year INT )"
# )

# c.execute(
#     "CREATE TABLE trans(detail VARCHAR(2000),trans_id VARCHAR(13) PRIMARY KEY )"
#     )


# c.execute('DROP TABLE garment')

# da = c.fetchall()
# print(da)

# c.execute("ALTER TABLE trans DROP trans_id")

# c.execute("UPDATE garment SET status='inventroy' where barcode = 123")

# c.execute("CREATE TABLE auth(username VARCHAR PRIMARY KEY, password VARCHAR)")

c.execute("INSERT INTO  auth VALUES('Shahid','anabiya')")

# obj = c.execute('SELECT * FROM garment')
# for x in obj:
#     print(x)

# num = 1

# print(num +10.0)


# c.execute("INSERT INTO sold SELECT * FROM garment WHERE barcode='123'")

# c.execute("DELETE FROM garment WHERE barcode = 123")

# p = c.execute('SELECT * FROM garment')
# for x in p:
#     print(x)

# c.execute("INSERT into garment(barcode, name, sale_price, cost_price) VALUES(123, 'hello', 1100, 1000 )")

p = c.execute("SELECT * from auth")
for x in p:
    print(x)

conn.commit()