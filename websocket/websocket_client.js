let ws_server_url = 'ws://localhost:8090';
let ws = new WebSocket(ws_server_url);

let logElement = document.getElementById('websocket_log');

function clearLog(logElement) {
    logElement.innerText = '';
}

function addToLog(logElement, text) {
    logElement.innerText += `${text}\n`;
}

window.onload = function() {
    addToLog(logElement, `Run a websocket server at ${ws_server_url}\n`);
}

//
// Websocket events
//
ws.onopen = function(event) {
    console.log('WebSocket opened');
    // Automatically send something to the websocket server just for grins
    ws.send('Sending a message to a WebSocket server');
};
ws.onclose = function(event) {
    console.log('WebSocket closed');
};
ws.onerror = function(event) {
    console.log('WebSocket error:', event);
}
ws.onmessage = function(event) {
    console.log('Received message:', event);
    addToLog(logElement, event.data);
}

//
// Button handlers
//
var btn_send = document.getElementById('btn_send');
btn_send.addEventListener('click', function(event) {
    // Sends a 'message' event to the SocketIO server
    data = 'Clicked the Send button.';
    addToLog(logElement, data);
    ws.send(data);
})

var btn_clear = document.getElementById('btn_clear');
btn_clear.addEventListener('click', function(event) {
    clearLog(logElement);
});
