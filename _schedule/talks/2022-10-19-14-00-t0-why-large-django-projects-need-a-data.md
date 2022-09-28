---
abstract: Django REST Framework focus on Don’t Repeat Yourself is useful for code
  simplicity and compatibility with built-in solutions for permissions, pagination,
  filters, etc. However, after projects grow in complexity, DRF’s default architecture
  isn’t enough to ensure code maintainability. Often, any change requires navigating
  through a lot of nesting to ensure all necessary ORM calls and avoid serious performance
  slowdowns. In this talk, you’ll learn how to use a custom data prefetch layer to
  avoid those issues by gathering together code that changes together.
accepted: true
category: talks
date: 2022-10-19 14:00:00-07:00
end_date: 2022-10-19 14:45:00-07:00
group: talks
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fflavio-juvenal%252F/opengraph/
layout: session-details
permalink: /talks/why-large-django-projects-need-a-data/
presenter_slugs:
- flavio-juvenal
published: true
room: Salon A-E
schedule_layout: full
sitemap: true
slug: why-large-django-projects-need-a-data-prefetching-layer
summary: ''
tags: null
title: Why large Django projects need a data (prefetching) layer
track: t0
---

The main building blocks of Django REST Framework projects, i.e. Views, Serializers, Managers, and Querysets allow developers to implement complex APIs with very little code repetition while reusing built-ins for essential API features. Developers feel guided by DRF to architect the project in a “Don’t Repeat Yourself” way by using inheritance, nesting, annotations, and model / app-based separation of concerns. They can group code in viewsets, inherit from base classes, reuse the same serializer across views, nest serializers into others, compute fields dynamically with ORM annotations, select or prefetch relations for performance, organize custom behavior with managers and querysets, and much more. All this DRYness is great because it integrates well with common web API concerns like permissions, pagination, filters, etc.

Based on our multi-year experience in building and maintaining several large Django projects, while using those built-in concepts really yields a DRY code, the overuse also results in a codebase full of complicated bugs and performance issues, especially related to ORM usage. View, serializer, and model methods are often heavily coupled to querysets’ annotations and prefeches, but those methods are spread across the codebase. Django’s default queryset laziness, together with its heavy usage of inheritance and nesting is the perfect recipe for a codebase where N+1 issues and heavy unnecessary queries can happen in any line of code after some less careful change.

For example, to prevent N+1 issues, if a serializer method field uses a filtered relationship, you must ensure this relationship is prefetched in all querysets related to that serializer. But this serializer can be nested into others, so you must now be careful to change all queryset references in seemingly unrelated views. Other sorts of “change amplification” situations also happen on large DRF codebases with heavy ORM usage. Requiring developers to be careful while navigating through lots of files to perform changes isn’t reasonable. Maybe being DRY is leading to the wrong abstraction?

It’s possible to design a better architecture that’s optimized both for enabling changes and avoiding performance regressions. With a new custom data prefetching layer that keeps compatibility with serializers and views, we can respect DRY while keeping performance and maintainability. That’s what we’ve been doing in our Django projects, and we will share our learnings in this talk. Hopefully, that applies to other maintainers of complex DRF projects.

Here's the planned outline:
- [3 minute] Who am I.
- [5 minutes] DRY: the good side
    - Permissions
    - Pagination
    - Filters
    - Exceptions
- [5 minutes] Example: resulting architecture when following DRY in a complex Django REST Framework project
- [10 minutes] Example: when DRY leads to Change Amplification
    - Serializers vs. queryset annotations and prefetches
    - Making things worse with nesting
    - When model logic is coupled to prefetches
    - New code and unexpected new queries, the fragility of prefetches
- [7 minutes] Common solutions that didn’t work for us
   - You can prevent queries, but you can’t prevent nesting
   - You can build the queryset in serializer, but you’ll repeat yourself
   - Fat models and querysets will have cross-cutting concerns
   - Auto-prefetching libraries can’t handle all cases
   - Tests can’t test the future
- [10 minutes] Solving with a data prefetching layer
   - How it looks like
   - The real DRY: gathering together code that changes together
   - How each field contributes to the queryset
   - How to keep it compatible with DRF views and serializers
   - Dealing with cross-model concerns and nesting
- [5 minutes] Questions
