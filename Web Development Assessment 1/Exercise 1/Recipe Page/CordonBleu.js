var audio = document.getElementById('background_audio');

function enableMute() { 
    audio.muted = true;
} 
  
function disableMute() { 
    audio.muted = false;
} 
  
function checkMute() { 
    alert(audio.muted);
}     

let buttontoggle = false;

const button = document.getElementById("button");
button.onclick = () => {
    buttontoggle = !buttontoggle
    console.log("Toggle")
    ButtonWork();
}

const ButtonWork = () => {
    if (buttontoggle == true){
        button.src = 'https://cdn.iconscout.com/icon/free/png-512/free-speaker-mute-icon-download-in-svg-png-gif-file-formats--silent-no-volume-user-interface-pack-icons-2598130.png?f=webp&w=512'
        enableMute();
    }
    else {
        button.src = 'https://cdn.iconscout.com/icon/free/png-512/free-speaker-volume-full-icon-download-in-svg-png-gif-file-formats--sound-voice-user-interface-pack-icons-2598129.png?f=webp&w=512'
        disableMute();
    }
}
