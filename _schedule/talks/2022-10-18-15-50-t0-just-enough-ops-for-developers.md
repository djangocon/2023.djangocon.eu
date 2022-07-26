---
abstract: "Most developers don't want to think about operations (aka Ops, DevOps…).
  PaaS providers (Heroku, Fly, Render, etc.) do an awesome job of getting your app
  live on the internet, but there's a lot to ops beyond just deployment.\r\n\r\nThis
  talk will answer the following questions:\r\n\r\n* How much CPU and memory should
  I give my services?\r\n* How do I know if the app is overallocated (costing too
  much money) or underallocated (slow/overloaded)?\r\n* How can I make my app faster?\r\n*
  Will autoscaling help me save costs?\r\n* What about serverless?\r\n* How do I store
  files?\r\n* How is the app performing for my users?\r\n* How do I check for errors?\r\n*
  How do I troubleshoot failures (app not starting or periodically crashing)?\r\n\r\nIf
  you're a developer and want to run your applications successfully without deep DevOps
  knowledge, this talk is for you. It will help if you have some basic Django developer
  experience, but other than that, no specific knowledge is necessary!"
accepted: true
category: talks
date: 2022-10-18 15:50:00-07:00
end_date: 2022-10-18 16:35:00-07:00
image: https://v1.screenshot.11ty.dev/https%253A%252F%252F2022.djangocon.us%252Fpresenters%252Fpeter-baumgartner/opengraph/
layout: session-details
permalink: /talks/just-enough-ops-for-developers/
presenter_slugs:
- peter-baumgartner
published: true
room: Salon A-E
sitemap: true
slug: just-enough-ops-for-developers
summary: ''
tags: null
title: Just enough ops for developers
track: t0
---

Draft outline:

* Personal Introduction
* Talk introduction (learnings from building a self-service application platform)
* Preparing your codebase (quick recap of [Prepping Your Project for Production](https://2019.djangocon.us/talks/prepping-your-project-for-production/))
* App Sizing/Tuning
  * CPU
    * Concurrency & processes
  * Memory
    * Out of memory errors
      * Memory leaks
      * Queryset Iterators
  * Tuning worker counts
  * Tuning instance/container counts
    * Scaling step size
  * Adjusting for serverless
* Backing services
  * Database sizing/tuning
  * Caching
* Observability
  * APM
  * Timeouts
  * Logging
* Debugging
  * App won't start
  * App is slow
  * App crashes
  * Static/media files missing
  * TLS warnings
