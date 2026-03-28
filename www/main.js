$(document).ready(function(){

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
                setTimeout(typeLoop, 1500); // slower pause
                return;
            }
        } else {
            index--;
            if(index === 0){
                isDeleting = false;
            }
        }

        setTimeout(typeLoop, isDeleting ? 100 : 180); // slower typing
    }

    typeLoop();

});