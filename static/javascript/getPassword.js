$(document).ready(function () {
    $.ajax({
        type: "POST",
        url: "/exe",
        success: function (response) {
            alert(response)
            $("body").load("../../templates/showresult.html");
        }
    });
})

