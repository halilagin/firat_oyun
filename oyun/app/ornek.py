from flask import Flask
from app import app


@app.route('/test')
def test():
	return 'Test, Hello, World!\n'


@app.route('/loop')
def index():
	k = []
	for x in range(9):
		k.append(x)
	return k
@app.route('/topla/<a>/<b>')
def topla(a,b):
	a_,b_ = int(a), int(b)
	sum_=a_+b_
	return str(sum_)
@app.route('/dict/<dict_value>')
def dict(dict_value):
	print("dict_value", dict_value)
	d=eval(dict_value)
	a=d["a"]
	print("a degeri", a)
	return str(a)

