from flask import Flask, render_template, redirect, url_for, request,make_response
from itsdangerous import signer


#app = Flask(__name__)





def AdminMainPage():
    return "admin main page"
    #return render_template("hello_admin.html")


