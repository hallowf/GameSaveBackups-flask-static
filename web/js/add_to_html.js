eel.search_all_disks()().then(games => {
  renderGames(games)
});

const gameTemplate = _.template(`
  <div class="card" style="width: 80%; margin:1em auto">
    <img class="card-img-top" src="/img/gameimgs/<%=name%>.jpg" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title"><%=name%></h5>
      <p class="card-text"><%=path%></p>
      <label class="btn btn-secondary active">
        <input class ="checkbox" type="checkbox" autocomplete="off"> Backup
        <input class ="checkbox" type="checkbox" autocomplete="off"> Steam Cloud
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

renderButton()
