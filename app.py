import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_will_never_guess'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    messages = Message.query.order_by(Message.id).all()  # Fetch recent messages
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(data):
    message = Message(username=data['username'], content=data['message'])
    db.session.add(message)
    db.session.commit()
    emit('new_message', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)