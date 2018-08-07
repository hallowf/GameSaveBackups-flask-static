
function sendTroughSocket(toSend) {
  var socket = io.connect('http://' + document.domain + ':' + location.port);
  socket.on('connect', function() {
    socket.emit('my event', {data: toSend});
  });
  socket.close()
}


function searchUnsynced() {
  const unsyncedButton = document.getElementById("no_sync").click(function() {
    sendTroughSocket("OOF")
  })
}

function searchSynced() {
  console.log("Somebody")
}

searchUnsynced()
