from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/dashboard/<name>')
def dashboard(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      print("If")
      return redirect(url_for('dashboard',name = user))
   else:
      user = request.args.get('name')
      print("Else")
      return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)