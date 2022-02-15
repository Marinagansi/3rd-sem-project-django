let navbar = document.querySelector('.header .navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
  if(window.innerWidth < 1200){
    menu.classList.remove('fa-times');
    header.classList.remove('active');
    document.body.classList.remove('active');
  };
};

let shoePreviewContainer = document.querySelector('.shoes-preview-container');
let shoePreview = shoePreviewContainer.querySelectorAll('.shoe-preview');

document.querySelectorAll('.shoes .slide .btn').forEach(detailBtn =>{
  detailBtn.onclick = () =>{
    shoePreviewContainer.style.display = 'block';
    let name = detailBtn.getAttribute('data-shoe');
    shoePreview.forEach(preview =>{
      let target = preview.getAttribute('data-target');
      if(name == target){
       preview.style.display = 'flex';
      };
    });
  };
});

document.querySelectorAll('.shoes-preview-container .shoe-preview .fa-times').forEach(close =>{
  close.onclick = () =>{
    shoePreviewContainer.style.display = 'none';
    shoePreview.forEach(closePreview =>{
      closePreview.style.display = 'none';
    });
  };
});

var swiper = new Swiper(".shoes-slider", {
  loop:true,
  spaceBetween: 25,
  grabCursor:true,
  centeredSlides: true,
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    991: {
      slidesPerView: 3,
    },
  },
});

let jacketPreviewContainer = document.querySelector('.jackets-preview-container');
let jacketPreview = jacketPreviewContainer.querySelectorAll('.jacket-preview');

document.querySelectorAll('.jackets .slide .btn').forEach(detailBtn =>{
  detailBtn.onclick = () =>{
    jacketPreviewContainer.style.display = 'block';
    let name = detailBtn.getAttribute('data-jacket');
    jacketPreview.forEach(preview =>{
      let target = preview.getAttribute('data-target');
      if(name == target){
       preview.style.display = 'flex';
      };
    });
  };
});

document.querySelectorAll('.jackets-preview-container .jacket-preview .fa-times').forEach(close =>{
  close.onclick = () =>{
    jacketPreviewContainer.style.display = 'none';
    jacketPreview.forEach(closePreview =>{
      closePreview.style.display = 'none';
    });
  };
});

var swiper = new Swiper(".jackets-slider", {
  loop:true,
  spaceBetween: 25,
  grabCursor:true,
  centeredSlides: true,
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    991: {
      slidesPerView: 3,
    },
  },
});