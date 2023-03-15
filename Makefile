
# Replace DOMAIN with your Netlify link if our templates are not deployed yet.
# DOMAIN = https://deploy-preview-58--2023-djangocon-eu-previews.netlify.app
DOMAIN = https://2023.djangocon.eu
IMAGE_SIZE = 1024x512
# IMAGE_SIZE = 1400x700

.PHONY: install
install:
	# may need this on MacOS for current Ruby version
	# brew install ruby
	#
	# ref: https://jekyllrb.com/
	gem install bundler jekyll
	bundle install

.PHONY: run
run:
	bundle exec jekyll serve --watch -l -H 0.0.0.0

.PHONY: build
build:
	bundle exec jekyll build

.PHONY: test
test:
	bundle exec rake test

.PHONY: social
social:
	@echo "check out... https://github.com/sindresorhus/pageres-cli"

	@pageres $(DOMAIN)/presenters/adolfo-fitoria/ $(IMAGE_SIZE) \
		--overwrite \
		--filename=static/img/social/presenters/adolfo-fitoria
