# utdsgda.club
This website uses [Jekyll] and a modified version of [bulma-clean-theme]. The site is designed to make the implementation of updates easy and accessible for developers of various skill levels. This is done to ease the transition between current and future SGDA officers.

## Sitemap
For reference, here is a map of the site's webpages and the corresponding files for their text content:

| Webpage | File |
|------------|------------------------------|
| Home page | `index.md` |
| Club info & current officers | `about.md` |
| Upcoming events | `events.md` |
| Club merchandise | `merch.md` |
| Discord server redirect | `discord.md` |
| Mailing list redirect | `mailing.md` |
| 404 page | `404.html` |

## Updating the site *(for people who don't want to mess with the code)*
Many aspects of the site are dynamically constructed using data stored in YML files. This allows for easy updates without needing to modify the site's code. Simply add, remove, or modify items in the list of the corresponding file.

|Aspect of the site  |File location  |
|--|--|
|List of club officers  |`/_data/officers.yml`  |
|Merchandise on store page |`/_data/merchandise.yml` |
|List of company collaborators |`/_data/companies.yml` |
|Social media in the footer |`/_data/footer.yml` |
|Discord invite link* |`discord.markdown` |
|Mailing list link* |`mailing.markdown` |
*For the Discord and Mailing links, simply replace the link in the markdown file.

## Installation
The site can be built and tested in a local environment using Jekyll. Jekyll has a helpful installation tutorial available [here](https://jekyllrb.com/tutorials/video-walkthroughs/). 

Once installed, you can host the site locally by running the command `bundle exec jekyll serve` from the project's root directory.

## Helpful documentation
 - [Jekyll documentation]
 - [Bulma Clean Theme documentation]
 - [Bulma documentation]

[Jekyll]: https://jekyllrb.com/
[bulma-clean-theme]: https://github.com/chrisrhymes/bulma-clean-theme
[Jekyll documentation]: https://jekyllrb.com/docs/
[Bulma Clean Theme documentation]: https://github.com/chrisrhymes/bulma-clean-theme
[Bulma documentation]: https://bulma.io/documentation/