activate :directory_indexes
activate :automatic_image_sizes

set :css_dir, 'css'
set :js_dir, 'js'
set :images_dir, 'img'

page "/changelog/*", layout: 'changelog'

configure :build do
  activate :minify_javascript
  activate :asset_hash
  activate :gzip
  set :haml, { ugly: true }
end
