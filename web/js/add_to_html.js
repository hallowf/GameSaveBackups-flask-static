eel.get_games()().then(games => {
  renderGames(games)
});

const gameTemplate = _.template(`
  <div class="card" style="width: 80%; margin:1em auto">
    <img class="card-img-top" src="/img/<%=name%>.jpg" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title"><%=name%></h5>
      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
      <div class="btn-group-toogle" data-toggle="buttons">
        <label class="btn btn-secondary active">
          <input type="checkbox" checked autocomplete="off"> Backup
        </label>
      </div>
    </div>
  </div>
`)

const root = $('#list')
function renderGames(games) {
  games.forEach(game => {
    var element = $('<div></div>').addClass("col-sm-6")
    element.html(gameTemplate(game))
    root.append(element)
  })
}
