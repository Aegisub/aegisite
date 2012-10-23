module WikiLink
  def page_url page
    path_parts = page.split '/'
    resource = current_resource

    url   = check_node(resource.children, path_parts)
    url ||= check_node(resource.siblings, path_parts)
    url ||= check_node(sitemap.resources, path_parts)

    print "Page not found: #{page}\n" unless url
    url
  end

  def wiki_link page, text
    text = page.gsub('_', ' ') if text.blank?
    link_to(text, page_url(page))
  end

  private
  def check_node nodes, parts
    nodes.each do |c|
      if c.url.split('/').last == parts[0]
        return c.url if parts.length == 1
        return c.url + parts[1] if parts[1].start_with? '#'
        return check_node c.children, parts.drop(1)
      end
    end
    nil
  end
end
