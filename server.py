from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "this is a secret key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    # var = request.form['nameValue']
    # session['nameValue] = var
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/results')

@app.route('/results')
def result():
    name = session['name']
    location = session['location']
    language = session['language']
    comment = session['comment']
    print(name)
    return render_template('results.html', name=name, location=location, language=language, comment=comment)

if __name__ == '__main__':
    app.run(debug = True)