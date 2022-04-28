source "https://rubygems.org"
ruby RUBY_VERSION

gem "jekyll"
gem "mini_magick"
gem "github-pages", group: :jekyll_plugins
gem "webrick" # https://github.com/jekyll/jekyll/issues/8523 Ruby 3.0 removed but jekyll requires

# If you have any plugins, put them here!
group :jekyll_plugins do
    gem 'jekyll-feed'
    gem 'jekyll-redirect-from'
    gem 'jekyll-seo-tag'
    gem 'jekyll-sitemap'
end

group :test do
  gem 'rake'
  gem 'html-proofer'
end
