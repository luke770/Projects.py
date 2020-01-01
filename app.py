# 'Luke Reed'

# 'importing the Flask class'
from flask import Flask, render_template
# 'the first argument we pass is the name of the applications module or package which is (__name__)'

app = Flask(__name__)

# 'here we call the decorator app.rout() to trigger our function'
# 'the functions name ('/') is also used as the URL'


@app.route('/')
def index():
    return render_template('index.html')

# 'just like ('/workout') will trigger a different URL with different embedded functions'
# 'so app.rout calls the function index which returns'
# 'index.html which is a file saved in the same directory as our app.py'
# 'and the browser will then interpret the Html and print the information to the screen'
# 'also remembered to keep all of your Html Templates, Static CSS files, and Python code in the same directory'


@app.route('/workout')
def workout():
    return render_template('pg2index.html')

# 'As for the third app.route you have probably noticed it takes an argument'
# 'so how this works you will type /hello/Luke and <name> is the variable being passed to the hello function'
# 'so whatever you type after hello/ is set equal to <name>'
# 'and then it gets passed to page.html which then prints it to the screen'


@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)

# 'and the debug true displays debugging insights during development'
# 'and host='0.0.0.0' means make this web app accessible to anyone on the same network'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
