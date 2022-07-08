from ast import Num
from flask import Flask , render_template 

app = Flask(__name__)   

@app.route('/')          
def home():
    return "hi"



@app.route('/play')          
def play():
    return render_template('play.html')

@app.route('/play/<int:num1>')
def play1(num1):
    return render_template('play2.html', num1 = num1 )

@app.route('/play/<int:num2>/<color>')
def play2(num2 , color):
    return render_template('play3.html', num2 = num2 , color = color )


if __name__=="__main__":   
    app.run(debug=True)   





