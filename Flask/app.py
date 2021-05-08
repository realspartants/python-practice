from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return render_template('index.html')

@app.route('/products')
def hehe():
    return 'this is the products page of this web app'

if __name__  == '__main__':
    app.run(debug=True,port=8000)

