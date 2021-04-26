from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def searchpage():
    return render_template('search.html')

@app.route('/result', methods = ['POST'])
def searchresult():
    result = request.form
    name_result=result['contact_name']
    return render_template('result.html', n=name_result)

@app.route('/save')
def save():
    return render_template('save.html')

@app.route('/save_confirm', methods = ['POST'])
def save_confirmation():
    result = request.form
    name_result = result['contact_name']
    phone_result = result['phone_number']
    return render_template('save_confirm.html', phone=phone_result, name=name_result)

app.run(debug=True)