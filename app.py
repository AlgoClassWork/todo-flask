from flask import Flask, render_template, request, redirect, url_for
from queries import get_all_todos, add_todo, delete_todo

app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/') 
def index():
    todos = get_all_todos()
    return render_template('index.html', todos=todos)

#http://127.0.0.1:5000/add/
@app.route('/add', methods=['POST']) 
def add():
    title = request.form['title']
    if title:
        add_todo(title)
    return redirect( url_for('index') )

#http://127.0.0.1:5000/delete/int
@app.route('/delete/<int:id>') 
def delete(id):
    delete_todo( id )
    return redirect( url_for('index') )
    
app.run(debug=True)
