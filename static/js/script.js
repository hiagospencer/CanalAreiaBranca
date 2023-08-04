const iconMenuMobile = document.querySelector(".icon-menu")
const menuMobile = document.querySelector(".itens-menu")
const closeMenu = document.querySelector(".menu-close")

const copy = document.querySelector(".logos-slide").cloneNode(true);
      document.querySelector(".logos").appendChild(copy);


iconMenuMobile.addEventListener("click", function(){
    if(menuMobile.classList.contains("close")){
        menuMobile.classList.remove("close")
        menuMobile.classList.add("show")
    }
    if(menuMobile.classList.contains("show")){
        closeMenu.addEventListener("click", function(){
            menuMobile.classList.remove("show")
            menuMobile.classList.add("close")
        })
    }
})
