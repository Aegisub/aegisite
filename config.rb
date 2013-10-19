require 'bootstrap-sass'
require 'lib/markdown_extensions'
require 'lib/subdomain_rewriter'

activate :directory_indexes
activate :automatic_image_sizes
activate :livereload

set :css_dir, 'static/css'
set :js_dir, 'static/js'
set :images_dir, 'static/img'

page "/www/changelog/*", layout: 'changelog'
page "/docs/3.1/*", layout: 'manual', app: self

helpers do
  def ticket id
    "<a href='http://devel.aegisub.org/ticket/#{id}'>##{id}</a>"
  end
end

set :markdown_engine, :kramdown
set :markdown,
  input: 'WikiKramdown',
  toc_levels: []
set :haml,
  ugly: true

activate :syntax

configure :build do
  # Needs to be before asset_hash
  activate :subdomain_rewriter

  activate :minify_css
  activate :asset_hash
  activate :gzip
end
