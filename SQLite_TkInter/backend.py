import sqlite3

class Database:

    # initializing the database
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("create table if not exists people (id integer primary key, name text, hobbies text, job text, discussions text)")
        self.conn.commit()

    # inserting new people and info
    def insert(self,name,hobbies,job,discussions):
        self.cur.execute("insert into people VALUES (null,?,?,?,?)", (name,hobbies,job,discussions))
        self.conn.commit()

    # allowing a view all, from time of entry (due to being sorted by id)
    def view(self):
        self.cur.execute("select * from people")
        rows=self.cur.fetchall()
        return rows

    # search by single parameter
    def search(self,name="",hobbies="",job="",discussions=""):
        self.cur.execute("select * from people where name=? OR hobbies=? OR job=? OR discussions=?", (name,hobbies,job,discussions))
        rows=self.cur.fetchall()
        return rows

    #
    def update(self,id,name,hobbies,job,discussions):
        self.cur.execute("UPDATE people set name=?, hobbies=?, job=?, discussions=? where id=?",(name,hobbies,job,discussions,id))
        self.conn.commit()

    # deleting person based on ID (which is linked to selecting it via mouse click or touch)
    def delete(self,id):
        self.cur.execute("delete from people where id=?",(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
