eel.get_games()().then(games => {
  renderGames(games)
});

const gameTemplate = _.template(`
  <div class="card" style="width: 80%; margin:1em auto">
    <img class="card-img-top" src="/img/<%=name%>.jpg" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title"><%=name%></h5>
      <p class="card-text"><%=path%></p>
      <div class="btn-group-toogle" data-toggle="buttons">
        <label class="btn btn-secondary active">
          <input class ="checkbox" type="checkbox" autocomplete="off"> Backup
        </label>
      </div>
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
    eel.make_zip()
  })
}

renderButton()
