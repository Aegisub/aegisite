module WikiLink
  def page_url page
    resource = current_resource
    prefix = current_resource.url.match(/\/docs\/[^\/]+\//)[0]

    path_parts = page.split '/'
    if path_parts[0] == 'img'
      return prefix + page
    end

    url   = check_node(resource.children, path_parts, prefix)
    url ||= check_node(resource.siblings, path_parts, prefix)
    url ||= check_node(sitemap.resources, path_parts, prefix)

    print "Page not found: #{page}\n" unless url
    url
  end

  def wiki_link page, text
    text = page.gsub('_', ' ') if text.blank?
    link_to(text, page_url(page))
  end

  def wiki_page_name page
    parts = [clean_name(page.url)]
    while page.parent
      parts << link_to(clean_name(page.parent.url), page.parent.url)
      page = page.parent
    end
    parts.reverse.drop(2).join ' / '
  end

  private
  def check_node nodes, parts, prefix
    nodes.each do |c|
      if c.url.start_with? prefix and c.url.split('/').last.casecmp(parts[0]) == 0
        return c.url if parts.length == 1
        return c.url + parts[1] if parts[1].start_with? '#'
        return check_node c.children, parts.drop(1), prefix
      end
    end
    nil
  end

  def clean_name name
    name.gsub(/^.*\/([^\/]+)\/$/, '\1').gsub('_', ' ')
  end
end
