from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from forms import *

app = Flask(__name__)

# ------- Connect to Tasks DB -------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = "secretsecret"
db = SQLAlchemy(app)
Bootstrap(app)


# Define the Tasks model
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)


# Create database tables
with app.app_context():
 db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    form = DateForm()
    tasks=[]
    if request.method == 'POST':
        date = form.date.data
        tasks = Tasks.query.filter_by(date=date).all()

    return render_template('index.html', form=form, tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = TaskForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        description = form.description.data
        new_task = Tasks(date=date, description=description)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('add.html', form=form)


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Tasks.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
