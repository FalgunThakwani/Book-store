import sqlite3


class Database:

    def __init__(self):
        global conn , cursor
        conn=sqlite3.connect("books.db")
        cursor=conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title TEXT , author TEXT , year INTEGER , isbn INTEGER ) ")
        conn.commit()


    def view(self):
            cursor.execute("SELECT * FROM book ")
            rows=cursor.fetchall()
            conn.commit()
            return rows

    def insert(self,title,author,year,isbn):
            cursor.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,isbn))
            conn.commit()

    def update(self,id,title,author,year,isbn):
            cursor.execute("UPDATE book SET title=? , author=? , year=? , isbn=? WHERE id = ?",(title,author,year,isbn,id))
            conn.commit()


    def delete(self,id):
        cursor.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()


    def search(self,title="",author="",year="",isbn=""):
        cursor.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=? ",(title,author,year,isbn))
        rows=cursor.fetchall()
        conn.commit()
        return rows


    def __del__(self):
        conn.close()
