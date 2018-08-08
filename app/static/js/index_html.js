// Template for creating game cards
const cardTemplate = _.template(`
  <div class="card bg-secondary game_cards" style="width:85%; background-color:#eae8ea; margin:1em auto">
    <img class="card-img-top" src="/img/gameimgs/<%=name%>.jpg" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title"><%=name%></h5>
      <p class="card-text"><%=path%></p>
      <p class="card-text"><%=sync_path%></p>
      <label class="btn btn-secondary active">
        <input class ="checkbox" style="margin:1em auto" type="checkbox" autocomplete="off"> Backup
      </label>
      <label class="btn btn-secondary active">
        <input class ="steamCloud" style="margin:1em auto" type="checkbox" autocomplete="off"> Steam Cloud
      </label>
    </div>
  </div>
`)

// Websocket connection
const socket = io.connect("http://" + document.domain + ":" + location.port + "/websocket")


function renderGames(games) {
  const the_row = document.getElementById("the_row")
  the_row.innerHTML = ""
  games.forEach(game => {
    var element = $('<div></div>').addClass('col-sm-3')
    element.html(cardTemplate({ "name": JSON.stringify(game.name), "path": JSON.stringify(game.path), "sync_path": JSON.stringify(game.sync_path)}))
    the_row.append(element)
  })
}




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
    renderGames(msg.dict)
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
    syncedGameList.forEach(function(object) {
      console.log("Received: " + JSON.stringify(object))
    })
    renderGames(msg.dict)
  })
}

searchUnsynced()
searchSynced()
