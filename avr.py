from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def avr():
        return render_template('avr.html')

if __name__ == '__main__':
    app.run()