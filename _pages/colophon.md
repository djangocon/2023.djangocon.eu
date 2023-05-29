---
description: Thank you to those who have inspired us
heading: Colophon
layout: default
permalink: /colophon/
title: Colophon
published: true
---

We are grateful to the past organizers of DjangoCon Europe and of other events for their help and inspiration. The following is an incomplete list of organisations and conferences whose positive example, advice, and generosity have helped make DjangoCon EU the welcoming conference it is today.

## Organisation

- [AlterConf](https://www.alterconf.com/speak), speaker slide guidelines
- [PyCon UK 2019](https://pretalx.com/pyconuk-2019/talk/K973NJ/), for sprints news wording
- [DjangoCon Europe 2022](https://2022.djangocon.eu), guidances and advice for previous DjangoCon event
- [DjangoCon US 2022](https://2022.djangocon.us), website template & inspiration

## Website Design

This website is based on free and open source software, and was designed by our friends at [Torchbox](https://torchbox.com/) according to the designs of the [DjangoCon US 2022](https://2022.djangocon.eu) by [DEFNA](https://www.defna.org/).

Design elements:

- [Visual design by Torchbox](https://www.figma.com/file/v1WfquYwTNSkfKZp5Ny51Z/DjangoCon-Europe-2023-Edinburgh-website-design) – CC0 public domain dedication.
- [Metamorphous font](https://fonts.google.com/specimen/Metamorphous/about) OFL license.
- "Swoosh" vector art. MIT licensed. Copyright DEFNA and contributors.

## Website built

The website is built based on the [2022.djangocon.us repository](https://github.com/djangocon/2022.djangocon.us), using:

- [Jekyll](https://jekyllrb.com/)
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-redirect-from
  - jemoji
- [Zurb Foundation](https://foundation.zurb.com/sites/docs/)
- `hamburgers`
- jQuery
- Motion UI
- `what-input`

## Code of Conduct

- Our code of conduct and the response guidelines are adapted from DjangoCon Europe 2022 – originally based on the [2018 DjangoCon Europe code of conduct](https://github.com/djangocon/2018.djangocon.eu).

## Image Credits

- [DjangoCon Europe 2019 Group Photo](https://twitter.com/PlasmaDray/status/1117143187120885760),
Noah Alorwu (all rights reserved).
- [Edinburgh view](https://www.istockphoto.com/photo/skyline-of-edinburgh-gm1001833188-270772869) iStock Photos license (all rights reserved).
- [Edinburgh skyline](https://www.etsy.com/uk/listing/1170650154/edinburgh-skyline-silhouette-svg-png-eps), BerriDesign (all rights reserved).
- Assembly Rooms venue photos – copyright Assembly Rooms (all rights reserved).
- Biscuit Factory venue photos – copyright Biscuit Factory (all rights reserved).
- The Caves venue photos – copyright The Caves (all rights reserved).
- DjangoCon logo adapted by Torchbox based on assets copyrighted by DEFNA

<div class="partner-footer section-pad">
  <h3 class="v-pad-bottom text-left">Our Sponsors</h3>
  {% comment %}
    {% assign sponsors_by_level = "Diamond|Platinum|Gold|Silver|Bronze|Community|Grants|Supporters" | split: "|" %}
  {% endcomment %}
  {% assign sponsors_by_level = "Platinum|Gold|Silver|Bronze|Community|Grants|Supporters" | split: "|" %}
  {% for level in sponsors_by_level %}
    {% assign sponsors_in_level = site.sponsors | where: 'level', level | where: 'hidden', false %}
    {% assign sponsors_count = sponsors_in_level | size %}
    {% if sponsors_count != 0 %}
    <h4 class="lead min text-center swatch-color-teal">{{ level }}</h4>
    {% if level == "Supporters" %}
      <div class="row partner">
        The following amazing people and companies from the Django community went above and beyond to help make this
        conference possible. With their contribution, we are able to offer additional grants to people from marginalised
        or under-represented groups.
      </div>
    {% endif %}
    <div class="row partner-list">
      {% for sponsor in sponsors_in_level %}
        {% unless sponsor.hidden %}
        {% if level == "Supporters" %}
          <div class="column medium-12 text-center">
            {{ sponsor.name }}
          </div>
        {% else %}
          <div class="partner-block text-center">
            <a href="{{ sponsor.url_target }}">
              <img
                class="partner-logo {{ sponsor.logo_orientation }}"
                src="{{ sponsor.logo }}"
                alt="{{ sponsor.name }} Logo" />
            </a>
          </div>
        {% endif %}
        {% endunless %}
      {% endfor %}
    </div>
    {% endif %}
  {% endfor %}
</div>
