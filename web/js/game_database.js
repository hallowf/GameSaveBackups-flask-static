

const databaseTemplate = _.template(`
  <div class="card bg-secondary game_sliders" style="width:85%; background-color:#eae8ea; margin:1em auto">
    <div class="card_sliders"></div>
    <div class="card-body">
      <h5 class="card-title"><%=name%></h5>
      <p class="card-text font-weight-bold">Common save path</p>
        <p class="card-text"><%=path%></p>
      <p class="card-text font-weight-bold">Steam Sync path</p>
        <p class="card-text"><%=sync_path%></p>
    </div>
  </div>
`)

const carouselTemplate = _.template(`
  <div class="carousel slide" data-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img class="d-block w-100" src="../img/gameimgs/<%=name%>/1.jpg" alt="First slide">
      </div>
      <div class="carousel-item">
        <img class="d-block w-100" src="../img/gameimgs/<%=name%>/2.jpg" alt="Second slide">
      </div>
      <div class="carousel-item">
        <img class="d-block w-100" src="../img/gameimgs/<%=name%>/3.jpg" alt="Third slide">
      </div>
    </div>
  </div>
`)


const games_row = $('#game_database')
const card_images = $('.card_sliders')


function renderSliders(sliders) {
  sliders.forEach(slider => {
    slider_templates = $('<div></div>')
    slider_templates.html(carouselTemplate(slider))
    card_images.append(slider_templates)
  })
}

function renderGames(games) {
  $('#game_database').find('.game_sliders').remove()
  games.forEach(game => {
    var element = $('<div></div>').addClass('col-sm-3')
    element.html(databaseTemplate(game))
    games_row.append(element)
    })
  }



function get_whole_database() {
  eel.get_database()().then(games => {
    renderGames(games)
  })
}

function gameSliders() {
  $('.game_sliders').hover(
    function() {
      $(this).carousel({pause:false})
      $(this).carousel({interval:1500})
      console.log("Mouse entered game card")
    },
    function() {
      $(this).carousel('pause')
      console.log("Mouse left game card")
    })
}


gameSliders()

get_whole_database()

renderSliders()
