from flask import render_template, request, redirect, flash, session, url_for
from app.models import Todo
from app import app,db
from datetime import datetime


@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        db.session.add(Todo(task=content,created=datetime.now().strftime('(%d/%m/%Y) %H:%M')))
        db.session.commit()
        return redirect('/')
    tasks = Todo.query.all()
    return render_template('index.html',tasks=tasks)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    tasks = Todo.query.get_or_404(id)
    if request.method == 'GET':
        if tasks:
            return render_template('update.html',id=tasks.id,content=tasks.task)
        else:
            return '<h1>Accessing Invalid Data, Go <a href="/">Home</a></h1>'

    if request.method == 'POST':
        new_task = request.form['content']
        tasks.task = new_task
        db.session.commit()
        return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    tasks = Todo.query.get_or_404(id)
    db.session.delete(tasks)
    db.session.commit()
    return redirect('/')
