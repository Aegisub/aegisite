require 'bootstrap-sass'

activate :directory_indexes
activate :automatic_image_sizes

set :css_dir, 'static/css'
set :js_dir, 'static/js'
set :images_dir, 'static/img'

page "/www/changelog/*", layout: 'changelog'

configure :build do
  activate :minify_javascript
  activate :asset_hash
  activate :gzip
  set :haml, { ugly: true }

  class Middleman::Sitemap::Resource
    def url
      subdomain, _, path = destination_path.partition '/'
      path.sub! 'index.html', ''
      "http://#{subdomain}.aegisub.org/#{path}"
    end
  end
end
