// Establish Socket.IO Connection
const socket = io();

messageForm.addEventListener('submit', (event) => {
    // Send message to the server
    socket.emit('message', { message: message });
});