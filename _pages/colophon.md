---
description: Thank you to those who have inspired us
heading: Colophon
layout: default
permalink: /colophon/
title: Colophon
published: true
---

We are grateful to the past organizers of DjangoCon EU and of other events for their help and inspiration. The following is an incomplete list of organisations and conferences whose positive example, advice, and generosity have helped make DjangoCon EU the welcoming conference it is today.

## Organisation

- [Geek Feminism Wiki](http://geekfeminism.wikia.com/wiki/Conference_anti-harassment/Policy), Code of Conduct
- [AlterConf](https://www.alterconf.com/speak), speaker slide guidelines
- [PyCon UK 2019](https://pretalx.com/pyconuk-2019/talk/K973NJ/), for sprints news wording
- [DjangoCon Europe](https://2023.djangocon.eu), guidances and advice for previous DjangoCon event
- [DjangoCon US](https://2022.djangocon.eu), website inspiration

## Website Design

This website is based on free and open source software, and was designed by our friends at [Torchbox](https://torchbox.com/) and created by [DEFNA](https://www.defna.org/)

- [Jekyll](https://jekyllrb.com/)
- [Foundation](https://foundation.zurb.com/sites/docs/)
- [PyCon Australia](https://2018.pycon-au.org/colophon/), for this colophon
- [Ela Conf](https://elaconf.github.io/), for the Recap page inspiration
- [Styleguide](/styleguide/), to see the fonts and colors used in this website

## Code of Conduct

- [Conduct Hotline](https://conducthotline.com) by [Thea Flowers](https://thea.codes/)

## Image Credits

- [DjangoCon Europe 2019 Group Photo](https://www.flickr.com/photos/djangocon/albums/72157704663920022), Bartosz Pawlik, CC BY-NC-SA 2.0
- [Edinburgh view](https://www.flickr.com/photos/144080672@N05/albums/72157702995974445), TODO
- [Edinburgh skyline](https://www.flickr.com/photos/144080672@N05/albums/72157702995974445), TODO
- [Assembly Room](https://www.marriott.com/hotels/travel/sanmv-san-diego-marriott-mission-valley/), TODO
- [Biscuit Factory](https://www.marriott.com/hotels/travel/sanmv-san-diego-marriott-mission-valley/), TODO
- [The Caves](https://www.marriott.com/hotels/travel/sanmv-san-diego-marriott-mission-valley/), TODO

<div class="partner-footer section-pad">
  <h3 class="v-pad-bottom text-left">Our Sponsors</h3>
  {% assign sponsors_by_level = "Diamond|Platinum|Gold|Lanyard|Silver|Bronze|Opportunity Grant|Community" | split: "|" %}
  {% for level in sponsors_by_level %}
    {% assign sponsors_in_level = site.sponsors | where: 'level', level | where: 'hidden', false %}
    {% assign sponsors_count = sponsors_in_level | size %}
    {% if sponsors_count != 0 %}
    <h4 class="lead min text-center swatch-color-teal">{{ level }}</h4>
    <div class="row partner-list">
      {% for sponsor in sponsors_in_level %}
        {% unless sponsor.hidden %}
        <div class="partner-block text-center">
          <a href="{{ sponsor.url_target }}">
            <img
              class="partner-logo {{ sponsor.logo_orientation }}"
              src="{{ sponsor.logo }}"
              alt="{{ sponsor.name }} Logo" />
          </a>
        </div>
        {% endunless %}
      {% endfor %}
    </div>
    {% endif %}
  {% endfor %}
</div>
