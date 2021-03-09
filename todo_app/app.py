from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    items3 = get_items()
    return render_template('index.html',items=items3)

@app.route('/add-todo', methods=['GET','POST'])
def add_todo():    
    title = request.form.get('todo-title')
    add_item(title)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run()
