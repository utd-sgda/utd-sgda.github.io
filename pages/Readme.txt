Format:

---
layout: layout  (_layouts/layout.html)
title: Page Name
permalink: pagename

callouts: callout   (_data/callout.yml)
sponsors: sponser   (_data/sponser.yml)
products: product   (_data/product.yml)

hero_image: /images/image.png   or   hide_hero: true
---


layout: layout
- Reference the .html file of the same name in _layouts
- Uses it as a base and append the markdown in the .md file

title: Page Name
- The title goes in the top bar with ' - SGDA' appended to it

permalink: pagename
- utdsgda.club/pagename/
- Sets the link name after 'utdsgda.club'
- Can use 'pagename' or '/pagename/'. Either work


callouts, sponsers, and products. All should reference a .yml file in the _data folder.


hero_image: image_location
- The location of the hero image to display as a banner
hide_hero: true
- Alternative to 'hero_image', doesn't show any banner