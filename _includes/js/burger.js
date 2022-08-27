if(window.addEventListener)
{
    window.addEventListener('load', burger);
}
else
{
    window.attachEvent('onload', burger);
}

function burger()
{
    let stateful_elements = document.getElementsByClassName("stateful");

    for (let i = 0; i < stateful_elements.length; i++)
    {
        let el = stateful_elements[i];
        button = document.getElementById(el.getAttribute("for"));

        button.addEventListener('click', function (e)
        {
            el.classList.toggle('active');
            button.classList.toggle('active');
        });
    }
};