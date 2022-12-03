from flask import Flask
import views
import admin

app = Flask(__name__)

app.add_url_rule('/', view_func=views.index)
app.add_url_rule('/hello_admin', view_func=views.HelloAdmin)
app.add_url_rule('/admin_main', view_func=admin.AdminMainPage)


if __name__ == '__main__':
	app.run(debug=True)
