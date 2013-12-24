var msgs;
var textBox;
var ws;


var appendMsg = function(msg) {
    msgs.insertAdjacentHTML('beforeend', msg + "<br/>");
};


var onOpen = function(evt) {
    appendMsg("CONNECTED TO CHAT");
};


var onMessage = function(evt) {
    appendMsg(evt.data);
};


var onClose = function(evt) {
    appendMsg("DISCONNECTED FROM CHAT");
};


var joinChat = function() {
    msgs = document.getElementById("messages");
    textBox = document.getElementById("msgtxt");
    ws = new WebSocket("ws://127.0.0.1:8000/chatsocket");
    ws.onopen = onOpen;
    ws.onmessage = onMessage;
    ws.onclose = onClose;
};


var leaveChat = function() {
    ws.close();
};


var sendMsg = function() {
    ws.send(textBox.value);
    textBox.value = "";
};
