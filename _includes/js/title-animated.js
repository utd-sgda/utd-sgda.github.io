function clamp(input, min, max)
{
    return input < min ? min : input > max ? max : input;
}

function map(current, in_min, in_max, out_min, out_max)
{
    const mapped = ((current - in_min) * (out_max - out_min)) / (in_max - in_min) + out_min;
    return clamp(mapped, out_min, out_max);
}

window.onload = function ()
{
    // ignore mobile browsers
    if (navigator.userAgent.toLowerCase().match(/mobile/i)) return;
    
    let logos = document.getElementsByClassName('logo-shadow-cascade')

    for (let i = 0; i < logos.length; i++)
    {
        let el = logos[i];
        if (el.tagName != 'H1') continue;

        document.body.addEventListener('mousemove', function (e)
        {
            console.log(e);
            
            let center_x = el.offsetLeft + el.clientWidth / 2;
            let center_y = el.offsetTop + el.clientHeight / 2;
            
            let x = e.clientX;
            let y = e.clientY;

            const xWalk = Math.round(map(x - center_x, -window.innerWidth/2, window.innerWidth/2, -15, 15));
            const yWalk = Math.round(map(y - center_y, -window.innerHeight/2, window.innerHeight/2, -15, 15));

            let shadow = ['--sgda_red', '--sgda_yellow', '--sgda_green', '--sgda_blue']

            for (let i = 0; i < shadow.length; i++)
            {
                shadow[i] = `var(${shadow[i]}) ${xWalk*(i+1)}px ${yWalk*(i+1)}px`;
            }

            window.requestAnimationFrame(function()
            {
                el.style.textShadow = shadow.join(', ');
            });
        });
    }
};