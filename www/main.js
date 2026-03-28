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
                setTimeout(typeLoop, 1000); // pause before deleting
                return;
            }
        } else {
            index--;
            if(index === 0){
                isDeleting = false;
            }
        }

        setTimeout(typeLoop, isDeleting ? 40 : 80);
    }

    typeLoop();

});