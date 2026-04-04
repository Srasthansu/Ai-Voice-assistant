$(document).ready(function () {


    //Display Speak message
    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        $(".siri-text").fadeOut(200, function () {
            $(this).text(message).fadeIn(200);
        });
    }

    //Show Hood
    eel.expose(ShowHood);
    function ShowHood() {
        
        $("#siri-start").hide();
        $("#main-ui").show();
        
    }




});