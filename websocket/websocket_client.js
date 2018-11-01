let ws_server_url = 'ws://localhost:8090';
let ws = new WebSocket(ws_server_url);

ws.onopen = function(event) {
    console.log('WebSocket opened');
    // Automatically send something to the websocket server just for grins
    ws.send('Sending a message to an online WebSocket echo server');
};
ws.onclose = function(event) {
    console.log('WebSocket closed');
};
ws.onerror = function(event) {
    console.log('WebSocket error:', event);
}
ws.onmessage = function(event) {
    console.log('Receive message:', event);

    log_element = document.getElementById('websocket_log');
    log_element.innerText = event.data;
}
