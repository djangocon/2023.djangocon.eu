---
abstract: "Django's migration system is one of its greatest strengths as a framework.
  \ It can automatically generate migrations based on your changes to your models
  and can detect which migrations need to be applied to a database.  But, as the size
  of your development team and user base scale, there are pitfalls that you need to
  be aware of.  Not all migrations can be safely reversed, and trying to rewind bad
  migrations on a production database can cause a data disaster.  Not all migrations
  can be safely deployed without downtime, and trying to deploy them can give your
  users and your engineers a wall of errors.\r\n\r\nThis talk will cover the following:\r\n1.
  How to manage migrations across multiple code branches\r\n2. Reversible migrations:
  how to write migrations so that they can be safely undone\r\n3. Backwards compatible
  migrations: which migrations can be run as part of a deploy without causing downtime
  or errors\r\n4. Handling failed migrations as part of a deployment"
accepted: true
category: talks
date: 2022-10-18 12:00:00-07:00
end_date: 2022-10-18 12:25:00-07:00
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fbenjamin-zags-zagorsky/opengraph/
layout: session-details
permalink: /talks/django-migrations-pitfalls-and-solutions/
presenter_slugs:
- benjamin-zags-zagorsky
published: true
room: Salon F-H
sitemap: true
slug: django-migrations-pitfalls-and-solutions
summary: ''
tags: null
title: 'Django Migrations: Pitfalls and Solutions'
track: t1
---

## Target audience (Who)

This talk assumes familiarity with the management commands `makemigrations` and `migrate`.  It's likely to be most helpful for people working on a Django project with a multi-person engineering team where there are many branches being worked on simultaneously or for those working on a consumer applications with moderate to high uptime requirements.


## Motivation (Why)

There are complicated issues with Django migrations that show up at codebase scale as well as user scale.  Not all migrations can be safely reversed, and trying to rewind bad migrations on a production database can cause a disaster.  Not all migrations can be safely deployed without downtime, and trying to deploy them can give your users and your engineers a wall of errors.  Knowing about these issues ahead of time can help engineering run smoother and avoid big headaches later.

## Talk format (What)

The talk will begin with a look under the hood at several implementation details of Django migrations that are relevant to understanding the main pitfalls.  Following that, we'll run through each of the big pitfalls, the problem in detail, and how to solve it or work around it.  The four big pitfalls are:
1. Divergent migrations happening across code branches.  Here we'll look at how to manage your local database and migrations on branches to make switching and merging branches easier.
2. Irreversible migrations.  Here, we'll look at how to write migrations so that they can be safely undone
3. Backwards incompatible migrations.  Here, we'll look which migrations can be run as part of a deploy without causing downtime or errors
4. Failed migrations as part of a deployment.  Here, we'll look at why this might happen, how to avoid it, and how to solve it when it happens

## Talk outline (How)

Intro:
* Who I am
* Why I'm giving this talk
* Motivation
* Outline

Migration underpinnings:
* The migration recorder
* Makemigrations in detail
* Migrate in detail
* Reversing migrations

Migrations and branches:
* Merge migrations
* Rewinding migrations before switching (note that your migrations need to be reversible)
* Using SQLite locally allows backing up and restoring

Reversible Migrations:
* Which operations can't be reversed
* How to fix
* Backwards functions for RunPython

Backwards Compatible Migrations:
* The migration deployment race condition
* What makes a migration backwards compatible
* Which operations are backwards compatible
* Decomposing other operations into backwards compatible migration steps
* Non-backwards compatible operations and how to handle them

Failed migrations as part of a deployment:
* How a partial failure can happen
* How to prevent it
* How to fix it
