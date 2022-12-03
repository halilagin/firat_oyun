from flask import Flask
#import views
from ornek import *
from views import *


app = Flask(__name__)

@app.route("/")
def root():
	return "hello!"


if __name__ == '__main__':
	app.run(debug=True)
