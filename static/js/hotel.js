let navbarr = document.querySelector('.header .navbarr');

document.querySelector('#menu-btn').onclick = () =>{
    navbarr.classList.toggle('active');
}

window.onscroll = () =>{
    navbarr.classList.remove('active');
}

document.querySelectorAll('.about .video-container .controls .control-btn').forEach(btn =>{
    btn.onclick = () =>{
        let src = btn.getAttribute('data-src');
        document.querySelector('.about .video-container .video').src = src;
    }
})