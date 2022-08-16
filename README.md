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

Jekyll's [Installation guide](https://jekyllrb.com/docs/installation/) covers this quite well.

1. Install the latest version of [Ruby+Devkit](https://rubyinstaller.org/downloads/) (tested with 3.1.2-1 x64)

2. The documentation component can be leftout, but the others are required.

3. On the last page of the installation wizard, run the `ridk install` step. Select the `MSYS2 and MINGW development tool chain` in the pop-up window.

4. Run `gem install jekyll bundler` in a fresh command prompt.

5. navigate to the root of the project (in command prompt) and run `bundle install`.

Now `bundle exec jekyll serve` may be run (in command prompt) at the root of the project to create a development build of the site, which may be viewed at `http://localhost:4000/` in your browser.

Note: In VSCode, the `bundle exec jekyll serve` command can be exposed as a button in the bottom-right hand corner of the window with the `Jekyll Run` extension.

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

- `stylesheet` (bool): will inline page specific scss from `_includes/css/{page}.scss`
- `not-inline` (bool): instead of inlining `_includes/css/{page}.scss`, `assets/css/pages/{page}.scss` will be linked. This should be used if the stylesheet exceeds 14kb.

## Assets

`_assets` stores all non-`html`, non-`md`, and non-`scss` partial files that should be published with the site. This includes images, javascript, and page specific stylesheets.

## SCSS

`.scss` files in the `_sass` folder are considered 'partial' files. They are not directly used by pages, but rather imported by `.scss` files in `assets/css/` or `_includes/css/` to be used by pages.

`.scss` files in `assets/` need to have

```
---
---
```

at the top to be processed to `css`.

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