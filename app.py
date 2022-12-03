from flask import Flask
from .views import *


app = Flask(__name__)

@app.route("/")
def root():
	return "hello!"


if __name__ == '__main__':
	app.run(debug=True)
