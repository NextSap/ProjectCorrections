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
    success = 0
    name=name_result
    with open('datausers.txt', 'r') as datas:
        for a in datas:
            datas=a.split()
            if name_result == datas[0]:
                success = success+1
                p=datas[1]
        if success==0:
            p="Inconnu"
    return render_template('result.html', name=name_result, phone=p)

@app.route('/save')
def save():
    return render_template('save.html')

@app.route('/save_confirm', methods = ['POST'])
def save_confirmation():
    result = request.form
    name_result = result['contact_name']
    phone_result = result['phone_number']
    with open("datausers.txt", "a") as datas:
        datas.write(name_result+" "+phone_result+"\n")
    return render_template('save_confirm.html', phone=phone_result, name=name_result)


app.run(debug=True)