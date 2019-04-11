from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import functions

app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for('home'))


@app.route('/list.html')
def home():
    t_list = []
    for t in functions.showTasks():
        t_list.append(t)
    return render_template("main.html", list=t_list)


@app.route('/add_elem', methods=['GET', 'POST'])
def add():
    todo = request.form['task']
    functions.newTask(todo)
    return redirect(url_for('home'))


@app.route('/delete/<int:id_task>')
def delete(id_task):
    functions.removeTask(id_task)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run()
