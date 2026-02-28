from flask import Flask, render_template
from queries import get_all_todos

app = Flask(__name__)

#http://127.0.0.1:5000/ 
@app.route('/') 
def index():
    todos = get_all_todos()
    return render_template('index.html', todos=todos)

app.run(debug=True)