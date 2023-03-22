---
description: DjangoCon Europe 2023 Venues.
heading: Venues
layout: default
permalink: /venues/
published: true
title: Venues
---

<article>
{% for venue in site.venues %}
  <section class="section-pad {% cycle 'theme-white', 'theme-medium-gray' %}" id="{{ venue.nav_id }}" aria-labelledby="{{ venue.nav_id }}-heading">
  <div class="subpage-header">
    <h2 id="{{ venue.nav_id }}-heading">{{ venue.title }}</h2>
  </div>
  <h3>{{ venue.subtitle }}</h3>
    <div class="row column">
      <div class="medium-6 column">
      <img
        class="thumbnail thumbnail-block"
        src="{{ venue.image_url }}"
        alt="{{ venue.image_alt }}" />
      </div>
      <div class="medium-6 column">
      <iframe
        class="thumbnail thumbnail-block"
        width="600"
        height="380"
        src="{{ venue.embed_url }}" allowfullscreen></iframe>
      <p class="medium-text-center">
        <a
          class="button"
          href="{{ venue.map_url }}" target="_blank">View Larger Map</a>
      </p>
    </div>
    <div class="column">
      <div>
        {{ venue.content }}
      </div>
    </div>
  </div>
  </section>
{% endfor %}
</article>
