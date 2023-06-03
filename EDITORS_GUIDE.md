# Editors Guide

## Things to Know

- We use Markdown that uses [Jekyll front matter](https://jekyllrb.com/docs/frontmatter/) for most of the content of this website.
- Most of the time, you can write HTML directly into your markdown if you need to customize something.
- We support native Liquid tags.
- Unpublished work should be shared via a pull request. Feedback will be given in comments, and you can push commits to the same branch until your pull request is accepted.

## Front Matter

The front matter for pages like sponsors, blog posts, and organisers contains custom variables for each item, located between the triple-dashed lines. The values should be in quotes, example: `name: "Bugs Bunny"`. Here are a list of possibilities:

### Organisers

Organisers are stored in `_organisers`.

- **layout**: Which HTML layout from `_layouts/` this page should use. Should be `base`
- **name**: Full name as you want it to appear on the website
- **role** Your title for the conference
- **photo_url**: The path to your photo. Use a square image, 320x320, in JPEG format for photography or PNG for computer graphics. Compress with [Squoosh](https://squoosh.app/).
- **github**: Your GitHub username
- **twitter**: Your Twitter handle
- **website**: The URL for your website

### Pages

Pages are stored in `_pages/` and correspond to the different HTML pages on the website, like Speaker Information and FAQs.

- **layout**: Which HTML layout from `_layouts/` this page should use. Most of the time this will be `base`
- **title**: Title of the page. Appears in the browser window.
- **heading**: Title of the page. Appears at the top of the body of the page.
- **permalink**: The URL path
- **testimonial_img**: A path to the image you want to use for the [photo hero section](https://2023.djangocon.eu/styleguide/#photo-hero-section)
- **testimonial_img_mobile**: Same as **testimonial_img**, but for mobile
- **hero_text_align**: How you want the text in the photo hero to be aligned
- **hero-theme**: The [brand color](https://2023.djangocon.eu/styleguide/#color-guide) you want to use for the overlay of the photo hero section (example: `brand-color1` for Brand Color 1)
- **description**: A description of this page

### Sponsors

Each sponsor is storted as its own file in `_sponsors/`. The filename follows this format: `YYYY-MM-DD-name.md` with the date being the date the sponsor signed their contract or paid their invoice, so sponsors are rendered in the order they sign up.

- **layout**: Which HTML layout from `_layouts/` this page should use. Most of the time this will be `base`.
- **hidden**: `true` or `false` for whether this sponsor should be hidden on the website
- **name**: Sponsor name
- **level**: What level the sponsor is sponsoring at
- **logo**: Path to the sponsor's logo
- **logo_orientation**: `landscape` or `portrait` for the orientation of the logo
- **url_target**: The full URL for the sponsor's website
- **url_friendly**: A friendlier-looking URL for the sponsor's website
- **description**: A description of the sponsor

## Markdown Basics

Below are some examples of commonly-used Markdown syntax. If you want to dive deeper, check out this [cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Here-Cheatsheet).

### Bold and Italic

*Italics*: `*asterisks*` or `_underscores_`

**Bold**: `**double asterisks**` or `__double underscores__`

### Links

[DjangoCon US 2022](https::2023.djangocon.eu) - `[DjangoCon US 2022](https::2023.djangocon.eu)`

### Inline Images

![Image of people](/static/img/landing-page/people.jpg)

`![Alt text for image](/path/to/img.ext)`

### Headers

```
# Header 1
## Header 2
### Header 3
#### Header 4
```

# Header 1
## Header 2
### Header 3
#### Header 4

## Liquid Tags

We support native [Liquid tags](https://shopify.github.io/liquid/). The ones you will use most often include:

### `{{ var }}`

The double-moustache indicates a variable. You can use the variables in the front matter, or variables from `_config.yml`. To use variables from `_config.yml`, prefix with `site`:

`{{ site.contact_us_email }}` will render as "hello@djangocon.us"

### `{% if %}`

If you have used Django, you'll be pleased to know the `{% if %}` tag is very similar. Example:

```
{% if sponsor.level == "Gold" %}This is a Gold sponsor{% endif %}
```

### `{% for %}`

The `{% for %}` tag also works very similarly to how it does in Django. To cycle through a collection (like all the places, for example), would look like this:

```
{% for place in site.places %}
  {{ place.name }}, {{ place.location }}
{% endfor %}
```

### Other tags

Look into [assign](https://shopify.github.io/liquid/tags/variable/) and see it used [in the sponsors footer](https://github.com/djangocon/2023.djangocon.eu/blob/develop/_includes/sponsor-footer.html#L3).

_Based on the [Editor's Guide](https://dev.to/p/editor_guide) from Dev.to._

## Images

See all [licensed image assets files](https://drive.google.com/drive/folders/1LVzeqMaXKR3E7PECQrHvv3xtQz2WoMST). Main visuals:

- `city-silhouette.svg`: Edinburgh Skyline silhouette vector art purchased from BerriDesign.
- `djangocon-crowd-hq.jpg`: Photo by [Noah ALorwu / @PlasmaDray](https://twitter.com/PlasmaDray/status/1117143187120885760) with permission to use on 2023.djangocon.eu.
- `edinburgh-skyline-hq.jpg`: `iStock-1001833188 skyline of edinburgh`. iStock access rights purchased.

All images should be encoded in AVIF and WebP so we get the best possible image quality with the lowest file size. Use [Squoosh](https://squoosh.app/ to export images in those formats and optimise JPEG and PNG files.
