
idStorage = window.localStorage;

/*eel.search_all_disks()().then(games => {
  renderGames(games)
});*/

const gameTemplate = _.template(`
  <div class="card bg-secondary" style="width:85%; background-color:#eae8ea; margin:1em auto">
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

const root = $('#list')
function renderGames(games) {
  games.forEach(game => {
    var element = $('<div></div>').addClass('col-sm-3')
    element.html(gameTemplate(game))
    root.append(element)
    var button = element.find('.checkbox').click(function() {
      eel.make_backup(game)
    })
  })
}


function renderButton() {
  var zipButton = $('#backup')
  zipButton.click(function() {
    $('#loading').modal()
    eel.make_zip()().then(function(){
      $('#loading').modal('hide')
    })
  })
}

function loginSteam() {
  checkBTN = $('#checkid').click(function() {
    user_id = $('#userid').val()
    idStorage.setItem('userID', user_id)
    steam_id3 = eel.convert_into_ID3(user_id)().then(steam_id3 => {
      console.log(steam_id3)
      eel.get_steam_sync(steam_id3)().then(games => {
        renderGames(games)
      })
    })
  })
}


function cachedSync() {
  $('#cached_id').click(function() {
    cachedID = idStorage.getItem('userID')
    cached_steam_id3 = eel.convert_into_ID3(cachedID)().then(cached_steam_id3 => {
      console.log(cachedID)
      eel.get_steam_sync(cached_steam_id3)().then(games => {
        renderGames(games)
      })
    })
  })
}

function noSteam() {
  nosteam = $('#nosteam').click(function() {
    console.log("getting games")
    eel.search_all_disks()().then(games => {
      renderGames(games)
    });
  })
}

cachedSync()

noSteam()

loginSteam()

renderButton()
