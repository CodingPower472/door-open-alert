
var socket = new WebSocket('ws://localhost:8080');

function reverseState(currentState) {
    if (currentState == 'Open') {
        return 'Closed';
    } else if (status == 'Closed') {
        return 'Open';
    } else {
        console.error('Status text was neither open nor closed.');
        return 'Error';
    }
}

function updateTable(sensorIndex) {
    var tableRow = $('tr#sensor-' + sensorIndex);
    var status = tableRow.children('.status');
    var newStatus = reverseState(status.text());
    status.text(newStatus);
}

function getNotificationPermission() {

    return new Promise(function(resolve, reject) {

        if (!('Notification' in window)) {
            reject('This browser doesn\'t support desktop notifications');
        } else if (Notification.permission === 'granted') {
            resolve('Desktop notifications were already granted');
        } else if (Notification.permission !== 'denied') {
            return Notification.requestPermission()
                .then(function(permission) {
                    if (permission === 'granted') {
                        resolve('Desktop notifications were just granted');
                    } else {
                        reject('Desktop notifications were just denied');
                    }
                });
        } else {
            reject('Desktop notifications were already denied');
        }

    });

}

function sendNotification(sensorIndex) {
    console.log('Sending notification');
    var tableRow = $('tr#sensor-' + sensorIndex)
    var title = tableRow.children('.title').text();
    var status = tableRow.children('.status').text();
    new Notification(title + ' is now ' + status.toLowerCase());
}

socket.onmessage = function(event) {

    var sensorIndex = parseInt(event.data);
    console.log('Got message: ' + message);

    updateTable(sensorIndex);
    getNotificationPermission()
        .then(function(data) {
            sendNotification(sensorIndex)
        })
        .catch(console.error);

}
