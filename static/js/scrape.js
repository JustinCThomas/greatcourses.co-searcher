// Code adapted from:
// https://www.bogotobogo.com/python/Flask/Python_Flask_with_AJAX_JQuery.php
$(function(){
  $('button').click(function(){
    var user = $('#pageStart').val();
    var pass = $('#pageEnd').val();
    $.ajax({
      url: '/scrape',
      data: $('form').serialize(),
      type: 'POST',
      success: function(response){
        // console.log(response);
        var container = $('.container')[0];
        container.innerHTML = response;
      },
      error: function(error){
        console.log(error);
      }
    });
  });
});
