# utdsgda.club

This website uses [Jekyll] and [RaisinCSS]. The site is designed to make the implementation of updates easy and accessible for developers of various skill levels. This is done to ease the transition between current and future SGDA officers.

- [Installation](#installation)
- [Updating the site](#updating-the-site)
  - [Redirects](#redirects)
  - [Data](#data)
- [Sitemap](#sitemap)
  - [Using Default Layout](#using-default-layout)
  - [Assets](#assets)
  - [HTML Components (and their SCSS)](#html-components-and-their-scss)
  - [Source](#source)
  - [Repo Map](#repo-map)
- [Helpful documentation](#helpful-documentation)

# Installation

USE [RUBY 2.7.6-1](https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.7.6-1/rubyinstaller-devkit-2.7.6-1-x64.exe) with devkit!

The site can be built and tested in a local environment using Jekyll. Jekyll has a helpful installation tutorial available [here](https://jekyllrb.com/tutorials/video-walkthroughs/).

1. After installing ruby, run `gem install jekyll`.
2. For first time users, `bundle install` should be run while at the root of the repo.

Once installed, you can host the site locally by running the command `bundle exec jekyll serve` from the project's root directory.


# Updating the site

## Redirects

Redirects may be added/removed/modified by adjusting `.md` files in `/redirects/`.

```
---
permalink: /:name:/
redirect_to: website_link
---
```

Example: shirts

```
---
permalink: /shirts/
redirect_to: https://sgda.storenvy.com/products/33422776-sgda-f21
---
```

`permalink: /shirts/`
- Required to use `utdsgda.club/shirts/` or `utdsgda.club/shirts`

`redirect_to: https://sgda.storenvy.com/products/33422776-sgda-f21`
- The redirect link

## Data

| Aspect of the site            | File location           |
| ----------------------------- | ----------------------- |
| List of club officers         | `_data/officers.yml`    |
| Merchandise on store page     | `_data/merchandise.yml` |
| List of company collaborators | `_data/companies.yml`   |
| Social media in the footer    | `_data/socials.yml`     |

`.yml` (data) files may be edited to adjust their corresponding aspects of the site. Make sure follow the exact style of the existing files. `.yml` files are extremely sensitive to incorrect spaces, tabs, new-lines, commas, etc.

See the comments at the top of each file for more information.

# Sitemap

For reference, here is a map of the site's webpages and the corresponding files for their text content:

| Webpage                      | File             |
| ---------------------------- | ---------------- |
| Home page                    | `pages/home.md`  |
| Club info & current officers | `pages/about.md` |
| Club merchandise             | `pages/merch.md` |
| 404 page                     | `pages/404.html` |

## Using Default Layout

The default layout includes basic page elements used on every page, so pages leveraging the `default` layout should minimize their use of `html` and use as much `md` as possible. Though, `.html` components from `_includes.html` (or raw html) may be used within a pages `.md` to allow great customization of layout and styles.

To be more specific, the `default` layout includes a navigation bar at the top and a footer containing links to our socials. The content of the page are inserted as children of `<main>` and having margin applied along the x-axis for basic reponsiveness.

When inserting `.html` into the default template, consider if it needs to override the margin applied to children of `<main>`. If it does, `ignore`, `content-wrapper`, and `content` can be used to manually adjust this.

For example a hero image may use `ignore` to *ignore* the default responsive styling of `<main>`, `content-wrapper` to apply padding to match its siblings horizontal positioning, and `content` to constrain the hero image's text (which is a child of the image).

## Assets

`_assets` stores all non-`html`, non-`md`, and non-`scss` partial files that should be published with the site. This includes images, javascript, and page specific stylesheets.

## SCSS

`.scss` files in the `_sass` folder are considered 'partial' files. They are not directly used by pages, but rather imported by `.scss` files in `assets/css` to be used by pages.

## HTML Components (and their SCSS)

HTML elements can be grouped and extracted to `.html` files in `_includes` to abstract components and introduce reuseability. Additional styling can be extracted to `.scss` files in the `_sass/includes/` folder.

The general workflow of using components already built: use `{% include component.html%}` in the `.md` page and include its stylesheet (if any) in the page's stylesheet using `@import 'includes/component`.

This workflow allows modularity of components by leveraging multiple files that be referenced or deleted as necessary, but Jekyll compilation concatenates these components into a smaller amount of files. At most, there is a `.html` file of the page (created using the page, template, and reference components), the `main.css` containing site-wide styles, and `{page}.css` (containing styles for this specific page and any reference components). This lowers the request count to improve performance and optimize SEO.

## Repo Map

| File/Folder  | Type                                                               |
| ------------ | ------------------------------------------------------------------ |
| `_data`      | Data Files Accessible via `Site.Data`                              |
| `_drafts`    | Drafts of pages (not published)                                    |
| `_includes`  | Reuseable HTML 'Components'                                        |
| `_layouts`   | Reuseable HTML 'Templates'                                         |
| `_pages`     | `.md` and `.html` files built (published)                          |
| `_redirects` | `.md` files designating redirects (published)                      |
| `_sass`      | `.scss` partial files used by `main.scss` or page specific `.scss` |
| `_site`      | local 'Development' build of the site (not published)              |
| `_source`    | any source files to be kept (not published)                        |
| `assets`     | all non-`html` and non-`md` files (published)                      |

1: any folders not prefixed with a `_` are automatically copied to the published build of the site. Folders with a `_` may also be included by modifying the `include` list in `_config.yml`.

2: jekyll has specific configurations to process folders `_data`, `_drafts`, `_includes`, `_layouts`, and `_sass`, so their names should *almost never* be changed.

# Helpful documentation

 - [Jekyll documentation](https://jekyllrb.com/docs/)
 - [RaisinCSS documentation](https://github.com/tretapey/raisincss)

[Jekyll]: https://jekyllrb.com/
[RaisinCSS]: https://github.com/tretapey/raisincss