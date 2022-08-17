# Icons Source

Font Awesome is a great source for icons to use on the web or desktop, but their font/css will contain *a lot* of unused data. The easiest solution is to just deal, but instead I have extracted the icons' svg files and compiled it into a custom font for us. This means, we use Font Awesome's icons without the extra bloat. I more or less followed this [guide](https://blog.webjeda.com/optimize-fontawesome/).

- `fontawesome-free-6.1.2-web/` contains Font Awesome's source files
- `using/` contains `.svg` files from `fontawesome-free-6.1.2-web` being used in our custom font
- `icomoon/` contains output files from `icomoon.io/app`

## Updating the Icon font

1. move desired `.svg` files to `using`.
2. Go to [IcoMoon](https://icomoon.io/app/).
3. Select `Import Icons`
4. Load `icomoon/selection.json`
5. Load desired `.svg`'s
6. Generate Font > Download
7. copy `style.css` to `/_sass/_icons.scss` and `fonts/` to `/assets/fonts`

New icons will be (probably) be accessible with the `icon-{file-name}` class.