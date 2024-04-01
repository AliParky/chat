document.addEventListener('DOMContentLoaded', (event) => {
    // Establish Socket.IO Connection
    const socket = io();

    // Get references to the form and the input fields
    const messageForm = document.getElementById('message_form');
    const usernameInput = document.getElementById('username_input');
    const messageInput = document.getElementById('message_input');

    // Get reference to the messages list element
    const messagesList = document.getElementById('messages');

    messageForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent page reload on form submission

        const message = messageInput.value;
        messageInput.value = ''; // Clear the message input field

        // Send message to the server
        socket.emit('message', { username: usernameInput.value, message: message });
    });

    // Receive New Messages
    socket.on('new_message', (data) => {
        const newMessage = document.createElement('li');
        newMessage.textContent = `${data.username}: ${data.message}`;
        messagesList.appendChild(newMessage); // Add new messages to the end
    });
});