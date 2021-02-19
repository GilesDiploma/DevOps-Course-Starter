from flask import Flask

from todo_app.flask_config import Config, render_template

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('index.hmtl')


if __name__ == '__main__':
    app.run()
