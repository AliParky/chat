from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_will_never_guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
socketio = SocketIO(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    message = Message(content=data['message'])
    db.session.add(message)
    db.session.commit()
    emit('new_message', data, broadcast=True)

if __name__ == '__main__':
    app.run(debug=True)