# 2023.djangocon.eu website
[![Contributors](https://img.shields.io/github/contributors/djangocon/2023.djangocon.eu.svg)](https://github.com/djangocon/2023.djangocon.eu/graphs/contributors)
![GitHub](https://img.shields.io/github/license/djangocon/2023.djangocon.eu)

The 2023 djangocon.eu website is a static site compiled with [Jekyll](https://jekyllrb.com/docs/home/) and use the default theme [Minima](https://github.com/jekyll/minima).

## Pre-requisites

- [Bundler](http://bundler.io/)
- [Ruby](https://www.ruby-lang.org)

See the [Jekyll Quickstart Guide](https://jekyllrb.com/docs/quickstart/) for more info.


## Get Started

### via Local Development

For changes that require cloning/running the code locally, follow the above instructions to step 5. Instead of navigating to the file through the browser, open up your computer terminal (you will need to have Git installed locally and a code editor of your choice).

Clone your forked repo locally via the terminal, replacing the username in the URL with your own (note: not all operating systems will use a `$` as a terminal prompt).

```bash
$ git clone https://github.com/<your-username>/2023.djangocon.eu
```

Change directory into the folder

```bash
$ cd 2023.djangocon.eu
```

Verify that you are on the `main` branch

```bash
$ git branch
```

Firstly you need to install Jekyll.

```bash
$ gem install jekyll bundler
$ bundle install
```

Next, you can run Jekyll :
```bash
$ bundle exec jekyll serve
```
You can go to http://localhost:4000 and you'll see the homepage.

### Via Docker

You can use docker to run the website if you prefer, [docker-compose](https://docs.docker.com/compose/install/) is a pre-requisite. there is a `docker-compose.yml` in the folder, you just have to do those following commands to build an run the project:
```bash
$ docker-compose up --build
```

## Contributing
We encourage you to contribute to DjangoCon Europe 2023! Please check out the [Contributing](CONTRIBUTING.md) for guidelines about how to proceed.

As a contributor, you can help us keep the Django community open and inclusive. Please read and follow our [Code of Conduct](https://www.djangoproject.com/conduct/), and report unacceptable behavior to <a href="mailto:conduct@djangocon.eu">Code of Conduct committee</a>.


## License

[MIT License](LICENSE)
