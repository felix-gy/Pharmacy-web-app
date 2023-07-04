from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html', the_title='Login')

@app.route('/empleado')
def empleado():
    return render_template('empleado.html',the_title='Farmacia')

if __name__ == '__main__':
    app.run(debug=True)
    