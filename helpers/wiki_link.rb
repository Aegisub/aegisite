module WikiLink
  def page_url page
    path_parts = page.split '/'
    resource = current_resource

    url   = check_node(resource, path_parts)
    url ||= check_node(resource.parent, path_parts)
    url ||= check_node(root_resource(resource), path_parts)

    print "Page not found: #{page}\n" unless url
    url
  end

  def wiki_link page, text
    text = page.gsub('_', ' ') if text.blank?
    link_to(text, page_url(page))
  end

  private
  def check_node node, parts
    return node.url + parts[0] if parts[0].start_with? '#'

    node.children.each do |c|
      if c.url.split('/').last == parts[0]
        return c.url if parts.length == 1
        return check_node c, parts.drop(1)
      end
    end
    nil
  end

  def root_resource node
    node = node.parent while node.parent
    node
  end
end
