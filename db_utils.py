import sqlite3
print("hello")
def init_db():
    conn = sqlite3.connect("sales_data.db")
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS sales(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                title TEXT,
                category TEXT,
                price REAL,
                quantity INTEGER,
                revenue REAL,
                sale_time TEXT)''')
    conn.commit()
    conn.close()

def insert_sale(sale):
    conn=sqlite3.connect("sales_data.db")
    cursor=conn.cursor()
    cursor.execute('''
                   INSERT INTO sales (product_id, title, category, price, quantity, 
                   revenue, sale_time) VALUES (?,?,?,?,?,?,?)''',
                     (sale['product_id'],
                      sale['title'],
                      sale['category'],
                      sale['price'],
                      sale['quantity'],
                      sale['revenue'],
                      sale['sale_time']
                                                                    ))
    
    conn.commit()
    conn.close()
    