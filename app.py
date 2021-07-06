from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@app.route('/')
def hello_world():
    return 'Hey, we have Flask in a Docker container!'

@app.route('/name/<name>', methods=['GET'])
def name(name):
    return 'Hello ' + name

@app.route('/edit')
def edit()
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

@app.route('/all')
def all():
    todo_list = Todo.query.all()
    return render_template("list.html", todo_list=todo_list)

@app.route('/add', method['POST'])
def add()
    title=request.form.get('title')
    new_todo= Todo(title=title, complete=_False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("edit"))


@app.route('/base')
def base():
    return render_template("base.html")


if __name__ == '__main__':
    app.run(port=5000,debug=True,host='0.0.0.0')
