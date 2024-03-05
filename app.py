from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_will_never_guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

messages = []

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    messages.append(data)
    emit('new_message', data, broadcast=True)

if __name__ == '__main__':
    app.run(debug=True)