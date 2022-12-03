from flask import Flask, render_template, redirect, url_for, request,make_response
from itsdangerous import signer

app = Flask(__name__)




@app.route("/hello")
def Hello():
    return render_template("hello.html")\



@app.route("/hello_admin")
def HelloAdmin():
    return render_template("hello_admin.html")


@app.route("/hello-user/<name>")
def HelloUser(name):
    if name.lower() == "admin":
        return redirect(url_for("HelloAdmin"))
    return render_template("hello_user.html", name=name)


@app.route("/login", methods=['POST', 'GET'])
def Login():
    if request.method == 'POST':
        username = request.form["username"]
        return redirect(url_for("HelloUser", name=username))
    else:
        return render_template("login.html")


@app.route("/ort")
def average_calc():
    return render_template("student.html")


@app.route("/ort_sonuc", methods=['POST'])
def average_result():
    if request.method == 'POST':
        if "math" in request.form and "chem" in request.form and "bio" in request.form and "physic" in request.form:
            math = request.form['math']
            physics = request.form['physic']
            chemistry = request.form['chem']
            biology = request.form['bio']
            result = float((int(math) + int(physics) + int(chemistry) + int(biology)) / 4)
    return render_template("student_result.html", result=result)