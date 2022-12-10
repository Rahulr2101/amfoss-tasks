

  



function playsound(x) {
  switch(x){
    case 1 : var audio = new Audio('sounds/crash.mp3');
                           audio.play();
                           break;
    case 2 : var audio = new Audio('sounds/kick-bass.mp3');
                           audio.play();
                           break;
    case 3 : var audio = new Audio('sounds/snare.mp3');
                           audio.play();
                           break;
    case 4 : var audio = new Audio('sounds/tom-1.mp3');
                           audio.play();
                           break;
    case 5 : var audio = new Audio('sounds/tom-2.mp3');
                           audio.play();
                           break;
    case 6 : var audio = new Audio('sounds/tom-3.mp3');
                           audio.play();
                           break;
    case 7 : var audio = new Audio('sounds/tom-4.mp3');
                           audio.play();
                           break;
                           
    
  }
  }
  window.addEventListener('keydown',function(e){if(e.code=='KeyW'){
    playsound(1)
  }else if(e.code == 'KeyA'){
    playsound(2)
  }else if (e.code == 'KeyS'){
    playsound(3)
  }else if(e.code == 'KeyD'){
    playsound(4)
  }else if(e.code == 'KeyJ'){
    playsound(5)
  }else if(e.code=='KeyK'){
    playsound(6)
  }else if(e.code =='KeyI'){
    playsound(7)
  }},false)
  