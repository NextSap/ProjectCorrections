from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/autre_page')
def autre_page():
    return render_template("autre_page.html")
app.run(debug=True)

def search():
    success = 0
    search = input("Entrez un nom:")
    with open('datauser.txt', 'r') as datas:
        for n in datas:
            datas = n.split()
            if search == datas[0]:
                print (datas[0] + ": " + datas[1])
                success = success + 1
        if success == 0:
            return "Inconnu"


def write():
    else:
        phone_number = input("Téléphone:")
        with open('datauser.txt', 'a') as f:
            f.write(name + " " + phone_number + "\n")