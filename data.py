import sqlite3

class database:

    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute(''' CREATE TABLE IF NOT EXISTS
        Contact (id INTEGER PRIMARY KEY,fname TEXT,lname TEXT,password TEXT,cname TEXT)''')
        self.con.commit()

    def select_record(self):
        self.cur.execute("SELECT * FROM Contact")
        records = self.cur.fetchall()
        return records

    def insert_record(self, fname, lname, password, cname):
        self.cur.execute(
        "INSERT INTO Contact (fname,lname, password, cname) VALUES (?, ?, ?, ?)",(fname, lname, password,cname))
        self.con.commit()

    def remove_item(self,id):
        self.cur.execute("DELETE FROM Contact WHERE id = ?",(id,))
        self.con.commit()

    def search(self,password):   
        self.cur.execute('''SELECT * FROM Contact WHERE password = ?''',(password,))
        recs = self.cur.fetchall()
        return recs