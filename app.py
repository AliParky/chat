from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_will_never_guess'
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