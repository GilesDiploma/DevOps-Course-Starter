from flask import Flask, render_template, redirect, url_for, request

from todo_app.flask_config import Config
from todo_app.data.session_items import get_items, add_item

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET'])
def index():
    items = get_items()
    return render_template('index.html',items=items)

@app.route('/new', methods=['GET','POST'])
def new():    
    title = request.form.get('name')
    add_item(title)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run()
