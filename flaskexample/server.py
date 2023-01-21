from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
        return render_template('login.html')


@app.route('/')
def student():
   return render_template('student.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)



if __name__ == '__main__':
   app.run(debug = True)