var open = document.querySelector('#play-btn');
var close = document.querySelector('#close');
                    
open.addEventListener('click', function(){
    document.querySelector('#popup-video').style.display="flex";
});
                    
close.addEventListener('click', function(){
    document.querySelector('#popup-video').style.display="none";
     var iframe = document.querySelector('iframe');
        iframe.src = iframe.src;
});