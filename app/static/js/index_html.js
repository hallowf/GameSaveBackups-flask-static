

var socket = io.connect('http://' + document.domain + ':' + location.port + '/websocket')


function searchUnsynced() {
  const unsyncedButton = document.getElementById("no_sync")
  unsyncedButton.onclick = (function() {
    socket.emit('event listener', {data: "search_unsynced"})
  })
  socket.on('my response', function(msg) {
    console.log('Received: ' + msg.data)
  })
}

function searchSynced() {
  console.log("Somebody")
}

searchUnsynced()
