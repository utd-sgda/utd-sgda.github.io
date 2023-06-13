if (window.addEventListener)
{
    window.addEventListener('DOMContentLoaded', swapInLowresImages);
}
else
{
    window.attachEvent('DOMContentLoaded', swapInLowresImages);
}

function swapInLowresImages()
{
    const images = document.getElementsByTagName("img");
    for (let image of images)
    {

        let image_split = image.src. split('.');
        image_split = [image_split[0], "blur", image_split[1]];
        blur_image = image_split.join(".");
        let hires_image = image.src;
        image.src = blur_image;

        let image_holder = new Image();
        image_holder.src = hires_image;
        image_holder.addEventListener('load', () =>
        {
            setTimeout(2000, () => {
                console.log("loaded")
            });
            // image.src = hires_image;
        });
    }
}

// function loadHighResImage(elem, highResUrl) {
//     let image = new Image()
//     image.addEventListener('load', () => elem.src = highResUrl)
//     image.src = highResUrl
// }