const icon = document.querySelector('.icon')
        const menu = document.querySelector('.menu-navegacion')


        icon.addEventListener('click', ()=>{
            menu.classList.toggle("spread")
        })

     



        const user= document.querySelector(".btnUser")
        const prod= document.querySelector(".btnProducto")
        const us = document.querySelector(".us")
        const us1 = document.querySelector(".us1")
        const us2 = document.querySelector(".us2")
        const pro = document.querySelector(".pro")
        const pro1 = document.querySelector(".pro1")
        const pro2 = document.querySelector(".pro2")

        user.addEventListener('click', ()=>{
            us.classList.toggle("br")
            us1.classList.toggle("br")
            us2.classList.toggle("br")
            
        })
        prod.addEventListener('click', ()=>{
            pro.classList.toggle("br")
            pro1.classList.toggle("br")
            pro2.classList.toggle("br")
        })
        