$(document).ready(function(){

    // 🔥 ASK BUTTON TYPING ANIMATION
    let text = "ASK ME ANYTHING...";
    let index = 0;
    let isDeleting = false;

    function typeLoop(){

        let currentText = text.substring(0, index);
        $(".ask-btn").html(currentText + "|");

        if(!isDeleting){
            index++;
            if(index > text.length){
                isDeleting = true;
                setTimeout(typeLoop, 1500);
                return;
            }
        } else {
            index--;
            if(index === 0){
                isDeleting = false;
            }
        }

        setTimeout(typeLoop, isDeleting ? 100 : 180);
    }

    typeLoop();


    // 🔥 SIRI TEXT ANIMATION (only if you used .tlt)
    if ($('.tlt').length) {
        $('.tlt').textillate({
            loop: true,
            in: { effect: 'fadeInUp' },
            out: { effect: 'fadeOutDown' }
        });
    }


    // 🔥 SIRI WAVE (FIRST SCREEN)
    window.siriWave = new SiriWave({
        container: document.getElementById('siri-wave'),
        width: 300,
        height: 100,
        style: "ios9",
        speed: 0.2,
        amplitude: 1,
        autostart: true
    });


    // 🔥 STARTUP FLOW (VERY IMPORTANT)
    setTimeout(function(){

        // hide siri screen
        $("#siri-start").fadeOut(800, function(){

            // show main UI after siri disappears
            $("#main-ui").fadeIn(800);

        });

    }, 3000); // delay (3 sec)

    //mic button click event
 $("#MicBtn").click(function () {

    
    // 🔥 hide main UI
    $("#main-ui").fadeOut(300);
     
    // 🔥 show siri screen
    $("#siri-start").fadeIn(300);
    
    eel.allCommands()()
    

    // 🔥 increase wave energy (cool effect)
    if(window.siriWave){
        window.siriWave.setAmplitude(2);
    }

});

});
