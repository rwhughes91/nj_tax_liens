$(document).ready(function($) {
    $(".table_row_subs").click(function() {
        window.document.location = $(this).data("href");
    });
});

$(document).ready(
  $('#clear').click(function() {
    $('#lien_form')[0].reset();
    $("div input[type='text']").removeAttr("style");
    $("#id_county").removeAttr("style");
  })
);

$(document).ready(function($) {
  let sub_tab = $("#sub_tab");
  let sub_content = $("#sub_form");

    sub_tab.click(function() {
      sub_content[0].style.display = 'block';
    });
    $('#home').click(function() {
      sub_content[0].style.display = 'none';
    });
});

$(document).ready(function($) {
  let home = $("#home");
  let sub_tab = $("#sub_tab");

  sub_tab.click(function() {
    $('#subs_table_list')[0].style.display = 'block';
  });

  home.click(function() {
    $('#subs_table_list')[0].style.display = 'block';
  });
});

$(document).ready(function() {
  $("#redemption_tab").click(function() {
    $("#text_field_notes")[0].style.display = 'none';
    $(".red_form").show();
    $("#red_content").addClass("form-inline")
  });

  $("#notes_tab").click(function() {
    $("#text_field_notes")[0].style.display = 'flex';
    $(".red_form").hide();
    $("#red_content").removeClass("form-inline")
  })
});
