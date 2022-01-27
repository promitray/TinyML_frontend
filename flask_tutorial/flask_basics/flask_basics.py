## Talk about flask a little being lightweigh web framework! 

## Render some HTML text on the browser. 

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.

from flask import Flask, render_template
  
# Flask constructor takes the name of 
# current module (__name__) as argument.

app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World in 2 min'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

## Rendering templates and using variables

@app.route('/index')
def hello():
    return render_template('index.html', variable_name = 'promit')

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(word.capitalize())

@app.route('/multiply/<int:n1>/<int:n2>/')
def multiply(n1, n2):
    return '<h1>{}</h1>'.format(n1 * n2)

@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    return '<h2>Hi {}</h2>'.format(users[user_id])



  
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()