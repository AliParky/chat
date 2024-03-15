// Establish Socket.IO Connection
const socket = io();

const messagesList = document.getElementById('messages');

messageForm.addEventListener('submit', (event) => {
    const message = messageInput.value;
    messageInput.value = ''; // Clear the input field

    // Send message to the server
    socket.emit('message', { message: message });
});

// Receive New Messages
socket.on('new_message', (data) => {
    const newMessage = document.createElement('li');
    newMessage.textContent = data.message;
    messagesList.prepend(newMessage); // Add new messages to the top
});