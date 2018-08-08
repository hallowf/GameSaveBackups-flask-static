
const socket = io.connect("http://" + document.domain + ":" + location.port + "/websocket")

function searchUnsynced() {
  const unsyncedButton = document.getElementById("no_sync")
  unsyncedButton.onclick = (function() {
    socket.emit("data request", {request: "search_unsynced"})
  })
  socket.on("unsynced_game_list", function(msg) {
    const gameList = msg.dict
    gameList.forEach(function(object){
      console.log("Received: " + JSON.stringify(object))
    })
  })
}

function searchSynced() {
  const syncedButton = document.getElementById("steam_sync")
  syncedButton.onclick = (function() {
    let idInput = document.getElementById("user_id").value
    socket.emit("data request", {request: "search_synced " + idInput})
  })
  socket.on("synced_game_list", function(msg) {
    const syncedGameList = msg.dict
    for (var i = 0; i < syncedGameList.length; i++) {
      console.log("Found: " + JSON.stringify(syncedGameList[i]))
    }
    syncedGameList.forEach(function(object) {
      console.log("Received: " + JSON.stringify(object))
    })
  })
}

searchUnsynced()
searchSynced()
