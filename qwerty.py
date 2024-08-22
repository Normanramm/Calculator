from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    a = float(request.form['a'])
    b = float(request.form['b'])
    result = a + b
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
