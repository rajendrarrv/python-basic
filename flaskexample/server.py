from flask import Flask
from flask import render_template
app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
@app.route('/index')
def index():
    users = [ 'Rosalia','Adrianna','Victoria' ]
    return render_template('index.html', title='Welcome', members=users)

@app.route('/hello')
def hello_world():
   return "hello world"
#  with name    
@app.route('/product/<name>')
def get_product(name):
  return "The product is " + str(name)
# flask route multiple arguments
@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
  return 'Hello ' + first_name + ',' + last_name


app.run(host='0.0.0.0')