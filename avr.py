from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def avr():
        return render_template('index.html')
  
  @app.route('/avr1')
def avr1():
        return render_template('avr1.html')
  
  @app.route('/avr2')
def avr2():
        return render_template('avr2.html')
  
  @app.route('/avr3')
def avr3():
        return render_template('avr3.html')

if __name__ == '__main__':
    app.run()