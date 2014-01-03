var msgs;
var textBox;
var ws;

//
// Helper to add new messages to the bottom of the window.
//
var appendMsg = function(msg) {
    msgs.insertAdjacentHTML('beforeend', msg + "<br/>");
};

//
// Confirm connection
//
var onOpen = function(evt) {
    appendMsg("CONNECTED TO CHAT");
};

//
// All messages to the bottom of the window
//
var onMessage = function(evt) {
    appendMsg(evt.data);
};

//
// Confirm disconnect
//
var onClose = function(evt) {
    appendMsg("DISCONNECTED FROM CHAT");
};

//
// Open the websocket and setup handlers
//
var joinChat = function() {
    msgs = document.getElementById("messages");
    textBox = document.getElementById("msgtxt");
    ws = new WebSocket("ws://127.0.0.1:8000/chatsocket");
    ws.onopen = onOpen;
    ws.onmessage = onMessage;
    ws.onclose = onClose;
};

//
// Close the socket.
//
var leaveChat = function() {
    ws.close();
};

//
// Send messages
//
var sendMsg = function() {
    ws.send(textBox.value);
    textBox.value = "";
};
