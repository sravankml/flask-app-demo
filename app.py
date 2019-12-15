from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html')

@app.route('/register')
def register():
   return render_template('register.html')

@app.route('/register/home')
def home():
   return_value = "<h1> You have been successfully registerd </h2>"
   return return_value

if __name__ == '__main__':
   app.run(debug = True)
