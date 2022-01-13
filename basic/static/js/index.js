$(document).ready(function () {
  $("#a").on("click", function () {
    $.ajax({
      type: "POST",
      url: "/test",
      success: function (res) {
        console.log(res);
      },
    });
  });
});
