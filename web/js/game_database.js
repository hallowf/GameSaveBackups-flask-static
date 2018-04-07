

const databaseTemplate = _.template(`
  <div class="card bg-secondary" style="width:85%; background-color:#eae8ea; margin:1em auto">
    <img class="card-img-top" src="/img/gameimgs/<%=name%>.jpg" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title"><%=name%></h5>
      <p class="card-text font-weight-bold">Common save path</p>
        <p class="card-text"><%=path%></p>
      <p class="card-text font-weight-bold">Steam Sync path</p>
        <p class="card-text"><%=sync_path%></p>
    </div>
  </div>
`)


const game_fetch = $('#game_database')
function renderGames(games) {
  games.forEach(game => {
    var element = $('<div></div>').addClass('col-sm-3')
    element.html(databaseTemplate(game))
    game_fetch.append(element)
    })
  }



function get_whole_database() {
  eel.get_database()().then(games => {
    renderGames(games)
  })
}

function gameSliders() {
  $('#innerslider').hover(
    function() {
      $(this).carousel({pause:false})
      $(this).carousel({interval:1500})
    },
    function() {
      $(this).carousel('pause')
    })
}

gameSliders()

get_whole_database()
