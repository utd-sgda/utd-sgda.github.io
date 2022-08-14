window.onload = function ()
{
    burger = document.getElementById('nav-burger');
    tuckedMenu = document.getElementById('tuckedMenu');

    burger.addEventListener('click', function (e)
    {
        tuckedMenu.classList.toggle('nav-tucked');
        burger.classList.toggle('x');
    });
};