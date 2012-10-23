module WikiLink
  def page_url page
    suffix = "/#{page}/"
    resource = current_resource
    while resource
      resource.children.each do |r|
        return r.url if r.url.end_with? suffix
      end
      resource = resource.parent
    end
    print "Page not found: #{page}\n"
    nil
  end

  def wiki_link page, text
    text = page.gsub('_', ' ') if text.blank?
    link_to(text, page_url(page))
  end
end
