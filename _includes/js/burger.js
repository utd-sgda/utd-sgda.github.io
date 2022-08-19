window.onload = function ()
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