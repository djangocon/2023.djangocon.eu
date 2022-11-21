---
description: Meet the people who made DjangoCon EU 2023 possible.
heading: Organizers
layout: page
permalink: /organizers/
published: true
redirect_from:
- /about/organizers/
title: Organizers
---

<header class="subpage-header">
  <h1>{{ page.heading }}</h1>
</header>

<div class="content subpage-content">
  <section class="section-pad">
    <div class="row column">
      <p class="lead">
        There is no "I" in DjangoCon EU. Thank you to all our volunteers who make DjangoCon EU happen!
      </p>
      <div
        class="row small-up-1 smedium-up-2 medium-up-3 large-up-4 organizers">
      {% for organizer in site.organizers %}
        {% unless organizer.hidden %}
          <div
            class="column column-block">
            <div class="profile">
              <img
                class="thumbnail"
                src="{{ organizer.photo_url }}"
                alt="Photo of {{ organizer.name }}" />
              <div class="profile-namecard">
                <h3 class="profile-name">
                  {{ organizer.name }}
                  {% if organizer.pronouns != blank %}
                    ({{ organizer.pronouns }})
                  {% endif %}
                </h3>
                {{ organizer.role }}
              </div>
              <ul class="social-icons">
                {% if organizer.twitter != blank %}
                <li>
                  <a class="twitter" href="https://twitter.com/{{ organizer.twitter }}" target="_blank">
                    <svg class="twitter-icon"><use xlink:href="#twitter-icon"></use></svg>
                  </a>
                </li>
                {% endif %}
                {% if organizer.github != blank %}
                <li>
                  <a class="github" href="https://github.com/{{ organizer.github }}/" target="_blank">
                    <svg class="social-icon"><use xlink:href="#github-icon"></use></svg>
                  </a>
                  </li>
                {% endif %}
                {% if organizer.website != blank %}
                <li>
                  <a class="web" href="{{ organizer.website }}" target="_blank">
                    <svg class="social-icon"><use xlink:href="#web-icon"></use></svg>
                  </a>
                </li>
                {% endif %}
              </ul>
              </div><!--/.profile -->
          </div><!--/.column -->
        {% endunless %}
      {% endfor %}

      </div><!--/.row -->
    </div>
  </section>
</div><!-- end .content -->
