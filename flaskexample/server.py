from flask import Flask, make_response, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)


@app.route('/enternew')
def new_student():
   return render_template('student.html')




@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         nm = request.form['nm']
         addr = request.form['add']
         city = request.form['city']
         pin = request.form['pin']
         
         with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html", msg =msg)
         con.close()


@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)
if __name__ == '__main__':
  conn = sqlite3.connect('database.db')
  print ("Opened database successfully");
  conn.execute('CREATE TABLE  IF NOT EXISTS students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
  print ("Table created successfully");
  conn.close()
app.run(debug = True)