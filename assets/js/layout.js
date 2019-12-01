$(document).ready(function() {
  $(".close").click(function() {
    $(this).parent().hide();
  })
});

$(document).ready(function() {
  setTimeout(function() {
    $('#message').fadeOut('slow')
  }, 6000)
});